import contextlib
import os

from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession
from mcp.types import CallToolResult, TextContent, ToolAnnotations
from slack_bolt import App
from slack_bolt.adapter.starlette import SlackRequestHandler
from slack_bolt.oauth.oauth_settings import OAuthSettings
from slack_sdk.oauth.installation_store import FileInstallationStore
from slack_sdk.oauth.state_store import FileOAuthStateStore
from slack_sdk.signature import SignatureVerifier
from slack_sdk.web import WebClient
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.types import ASGIApp, Receive, Scope, Send

installation_store = FileInstallationStore(base_dir="./data/installations")

"""Creates an MCP server with a profile card tool using Slack identity.

https://github.com/modelcontextprotocol/python-sdk#getting-started
"""

mcp_server = FastMCP("Profile Card", stateless_http=True, json_response=True)


@mcp_server.tool(
    name="get_profile_card",
    title="Get Profile Card",
    description="Get a profile card for a Slack user by their user ID.",
    annotations=ToolAnnotations(readOnlyHint=True),
    meta={"slack": {"supportsBlockKit": True}},
)
async def get_profile_card(
    user_id: str, ctx: Context[ServerSession, None]
) -> CallToolResult:
    meta = ctx.request_context.meta
    model_extra = meta.model_extra if meta else None
    slack = model_extra.get("slack", {}) if model_extra else {}

    if not slack.get("user_id") or not slack.get("team_id"):
        return CallToolResult(
            content=[
                TextContent(
                    type="text",
                    text="Missing Slack identity context. "
                    "This tool must be called from Slack.",
                )
            ],
        )

    team_id = slack["team_id"]
    slack_user_id = slack["user_id"]
    enterprise_id = slack.get("enterprise_id")

    try:
        installation = installation_store.find_installation(
            enterprise_id=enterprise_id,
            team_id=team_id,
            user_id=slack_user_id,
            is_enterprise_install=bool(enterprise_id),
        )
        if not installation or not installation.bot_token:
            raise ValueError("No bot token")
        bot_token = installation.bot_token
    except Exception:
        return CallToolResult(
            content=[
                TextContent(
                    type="text",
                    text="App not installed to this workspace. Please install first.",
                )
            ],
            _meta={
                "slack": {
                    "blocks": [
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": "Please install the *MCP Profile Card* app "
                                "to access profile information.",
                            },
                            "accessory": {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "Install",
                                },
                                "url": f"{os.environ.get('BASE_URL', '')}/slack/install",
                                "action_id": "install_app",
                            },
                        }
                    ]
                }
            },
        )

    try:
        client = WebClient(token=bot_token)
        result = client.users_info(user=user_id)
        profile = result["user"]["profile"]
    except Exception:
        return CallToolResult(
            content=[
                TextContent(
                    type="text",
                    text=f"Failed to fetch profile for {user_id}.",
                )
            ],
        )

    return CallToolResult(
        content=[
            TextContent(
                type="text",
                text=f"Profile card for {profile['real_name']}\n"
                f"Title: {profile.get('title', '')}\n"
                f"Email: {profile.get('email', '')}",
            )
        ],
        _meta={
            "slack": {
                "blocks": [
                    {
                        "type": "card",
                        "icon": {
                            "type": "image",
                            "image_url": profile.get("image_72", ""),
                            "alt_text": profile.get("real_name", ""),
                        },
                        "title": {
                            "type": "mrkdwn",
                            "text": profile.get("real_name", ""),
                        },
                        "subtitle": {
                            "type": "mrkdwn",
                            "text": profile.get("title", ""),
                        },
                        "body": {
                            "type": "mrkdwn",
                            "text": f"*Email:* {profile.get('email', '')}",
                        },
                    }
                ]
            }
        },
    )


"""Creates a Bolt app with OAuth and a custom /mcp route.

https://docs.slack.dev/tools/bolt-python/getting-started
"""

bolt_app = App(
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
    oauth_settings=OAuthSettings(
        client_id=os.environ.get("SLACK_CLIENT_ID"),
        client_secret=os.environ.get("SLACK_CLIENT_SECRET"),
        scopes=["mcp:connect", "users:read", "users:read.email"],
        installation_store=installation_store,
        state_store=FileOAuthStateStore(
            expiration_seconds=600, base_dir="./data/states"
        ),
    ),
)
bolt_handler = SlackRequestHandler(bolt_app)


class SlackSignatureMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app
        self.verifier = SignatureVerifier(
            signing_secret=os.environ["SLACK_SIGNING_SECRET"]
        )

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        request = Request(scope, receive, send)
        body = await request.body()

        if not self.verifier.is_valid_request(body, dict(request.headers)):
            response = JSONResponse(
                {
                    "jsonrpc": "2.0",
                    "error": {"code": -32600, "message": "Invalid request"},
                    "id": None,
                },
                status_code=401,
            )
            await response(scope, receive, send)
            return

        async def replay_receive():
            return {"type": "http.request", "body": body, "more_body": False}

        await self.app(scope, replay_receive, send)


@contextlib.asynccontextmanager
async def lifespan(a):
    async with mcp_server.session_manager.run():
        yield


mcp_app = mcp_server.streamable_http_app()


app = Starlette(
    routes=[
        Route("/slack/events", endpoint=bolt_handler.handle, methods=["POST"]),
        Route("/slack/install", endpoint=bolt_handler.handle, methods=["GET"]),
        Route("/slack/oauth_redirect", endpoint=bolt_handler.handle, methods=["GET"]),
        Route(
            "/mcp",
            endpoint=SlackSignatureMiddleware(mcp_app),
            methods=["POST"],
        ),
    ],
    lifespan=lifespan,
)

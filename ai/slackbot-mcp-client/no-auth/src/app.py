import contextlib
import os
import random

from mcp.server import MCPServer
from mcp.types import CallToolResult, TextContent, ToolAnnotations
from slack_bolt import App
from slack_bolt.adapter.starlette import SlackRequestHandler
from slack_sdk.signature import SignatureVerifier
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.types import ASGIApp, Receive, Scope, Send

"""Creates an MCP server with a dice roller tool.

https://github.com/modelcontextprotocol/python-sdk#quickstart
"""

mcp_server = MCPServer("Dice Game")


@mcp_server.tool(
    name="roll_dice",
    title="Roll Dice",
    description="Roll one or more dice with a configurable number of sides.",
    annotations=ToolAnnotations(read_only_hint=True),
)
def roll_dice(sides: int = 6, count: int = 1) -> CallToolResult:
    rolls = [random.randint(1, sides) for _ in range(count)]
    total = sum(rolls)
    label = f"{count}d{sides}"
    rolls_display = f" [{', '.join(str(r) for r in rolls)}]" if count > 1 else ""

    return CallToolResult(
        content=[
            TextContent(type="text", text=f"Rolled {label}:{rolls_display} = {total}")
        ],
    )


"""Creates a Bolt app with a custom /mcp route.

https://docs.slack.dev/tools/bolt-python/getting-started
"""

bolt_app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)


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


mcp_app = mcp_server.streamable_http_app(stateless_http=True, json_response=True)


app = Starlette(
    routes=[
        Route(
            "/slack/events",
            endpoint=SlackRequestHandler(bolt_app).handle,
            methods=["POST"],
        ),
        Route(
            "/mcp",
            endpoint=SlackSignatureMiddleware(mcp_app),
            methods=["POST"],
        ),
    ],
    lifespan=lifespan,
)

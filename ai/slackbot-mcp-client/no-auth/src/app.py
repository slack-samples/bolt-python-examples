import contextlib
import os
import random
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from mcp.types import CallToolResult, TextContent, ToolAnnotations
from slack_bolt import App
from slack_bolt.adapter.starlette import SlackRequestHandler
from slack_sdk.signature import SignatureVerifier
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.types import ASGIApp, Receive, Scope, Send

DICE_HTML = (Path(__file__).parent / "dice.html").read_text()
RESOURCE_URI = "ui://dice-roller/dice.html"
RESOURCE_MIME_TYPE = "text/html;profile=mcp-app"

"""Creates an MCP server with a dice roller tool and UI resource.

https://github.com/modelcontextprotocol/python-sdk#quickstart
"""

mcp_server = FastMCP("Dice Game", stateless_http=True, json_response=True)


@mcp_server.tool(
    name="roll_dice",
    title="Roll Dice",
    description="Roll one or more dice with a configurable number of sides.",
    annotations=ToolAnnotations(readOnlyHint=True),
    meta={
        "ui": {
            "resourceUri": RESOURCE_URI,
        },
    },
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
        structuredContent={
            "sides": sides,
            "count": count,
            "rolls": rolls,
            "total": total,
        },
    )


@mcp_server.resource(
    RESOURCE_URI,
    name="Dice Roller",
    mime_type=RESOURCE_MIME_TYPE,
    meta={
        "ui": {
            "csp": {
                "resourceDomains": ["https://esm.sh"],
                "connectDomains": ["https://esm.sh"],
            }
        }
    },
)
def dice_resource() -> str:
    return DICE_HTML


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


mcp_app = mcp_server.streamable_http_app()


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

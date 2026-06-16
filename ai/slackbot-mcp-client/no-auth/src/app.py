import contextlib
import os
import random
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from mcp.types import CallToolResult, TextContent
from slack_bolt import App
from slack_bolt.adapter.starlette import SlackRequestHandler
from slack_sdk.signature import SignatureVerifier
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Mount, Route
from starlette.types import ASGIApp, Receive, Scope, Send

DICE_HTML = (Path(__file__).parent / "dice.html").read_text()
RESOURCE_URI = "ui://dice-roller/dice.html"
RESOURCE_MIME_TYPE = "text/html;profile=mcp-app"

# --- Bolt App ---

bolt_app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)
bolt_handler = SlackRequestHandler(bolt_app)

# --- MCP Server ---

mcp_server = FastMCP("Dice Game", stateless_http=True, json_response=True)


@mcp_server.tool(
    name="roll_dice",
    title="Roll Dice",
    description="Roll one or more dice with a configurable number of sides.",
    annotations={"readOnlyHint": True},
    meta={"ui": {"resourceUri": RESOURCE_URI}},
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


@mcp_server.resource(RESOURCE_URI, name="Dice Roller", mime_type=RESOURCE_MIME_TYPE)
def dice_resource() -> str:
    return DICE_HTML


# --- Slack Signature Verification Middleware ---


class SlackSignatureMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app
        self.verifier = SignatureVerifier(
            signing_secret=os.environ.get("SLACK_SIGNING_SECRET", "")
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

        # Replay the consumed body so the downstream app can read it again
        async def replay_receive():
            return {"type": "http.request", "body": body, "more_body": False}

        await self.app(scope, replay_receive, send)


# --- Starlette App ---

mcp_starlette_app = mcp_server.streamable_http_app()


@contextlib.asynccontextmanager
async def lifespan(a):
    async with mcp_server.session_manager.run():
        yield


async def slack_events(request: Request) -> Response:
    return await bolt_handler.handle(request)


app = Starlette(
    routes=[
        Route("/slack/events", endpoint=slack_events, methods=["POST"]),
        Mount("/mcp", app=SlackSignatureMiddleware(mcp_starlette_app)),
    ],
    lifespan=lifespan,
)

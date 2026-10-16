from dataclasses import dataclass
from typing import Any

from slack_sdk.models.blocks import AuthProviderBlock, MarkdownTextObject, SectionBlock
from slack_sdk.models.views import View

ACME_VALUE = "acme"
CONNECT_ACTION_ID = f"auth_provider_connect_{ACME_VALUE}"
DISCONNECT_ACTION_ID = f"auth_provider_disconnect_{ACME_VALUE}"

WELCOME_GREETING = (
    "*Welcome to Acme!* :rocket:\n"
    "Connect your Acme account to start ordering. "
    "Anvils ship same day, gravity permitting."
)
CONNECTED_GREETING = (
    "*You're all set!* :tada:\n"
    "Your Acme account is connected. "
    "Please keep giant magnets away from your laptop."
)


@dataclass(frozen=True)
class Connection:
    identity: str
    context: str


def plain_text(text: str) -> dict[str, str]:
    return {"type": "plain_text", "text": text}


def acme_provider(auth_url: str, connection: Connection | None) -> dict[str, Any]:
    provider: dict[str, Any] = {
        "value": ACME_VALUE,
        "name": plain_text("Acme account"),
        "description": plain_text(
            "Order rocket skates, anvils, and giant magnets without leaving Slack."
        ),
        "auth_url": auth_url,
        "is_connected": connection is not None,
    }
    if connection is not None:
        provider["connected_identity"] = plain_text(connection.identity)
        provider["connected_context"] = plain_text(connection.context)
    return provider


def home_view(provider: dict[str, Any]) -> View:
    greeting = CONNECTED_GREETING if provider["is_connected"] else WELCOME_GREETING
    return View(
        type="home",
        blocks=[
            SectionBlock(text=MarkdownTextObject(text=greeting)),
            AuthProviderBlock(**provider),
        ],
    )

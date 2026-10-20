from typing import Any

from slack_sdk import WebClient
from slack_sdk.models.blocks import AuthProviderBlock, MarkdownTextObject, SectionBlock
from slack_sdk.models.views import View

from src.connections import connections

GREETING = (
    "*Welcome to Acme!* :rocket:\n"
    "Anvils ship same day, gravity permitting. "
    "Please keep giant magnets away from your laptop."
)


def plain_text(text: str) -> dict[str, str]:
    return {"type": "plain_text", "text": text}


def provider(user_id: str) -> dict[str, Any]:
    acme: dict[str, Any] = {
        "value": "acme",
        "name": plain_text("Acme account"),
        "description": plain_text(
            "Order rocket skates, anvils, and giant magnets without leaving Slack."
        ),
        "is_connected": connections.is_connected(user_id),
    }
    if acme["is_connected"]:
        acme["connected_identity"] = plain_text(user_id)
    return acme


def home_view(acme: dict[str, Any]) -> View:
    return View(
        type="home",
        blocks=[
            SectionBlock(text=MarkdownTextObject(text=GREETING)),
            AuthProviderBlock(**acme),
        ],
    )


def report(client: WebClient, user_id: str):
    acme = provider(user_id)
    client.apps_user_connection_requestAuth(user_id=user_id, primary_provider=acme)
    client.views_publish(user_id=user_id, view=home_view(acme))


def connect(client: WebClient, user_id: str):
    connections.connect(user_id)
    report(client, user_id)


def disconnect(client: WebClient, user_id: str):
    connections.disconnect(user_id)
    report(client, user_id)

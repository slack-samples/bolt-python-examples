import os
from typing import Any

from slack_sdk import WebClient
from slack_sdk.models.blocks import AuthProviderBlock, MarkdownTextObject, SectionBlock
from slack_sdk.models.views import View

from src.connections import connections
from src.state import issue

CONNECT_PATH = "/acme/connect"

GREETING = (
    "*Welcome to Acme!* :rocket:\n"
    "Anvils ship same day, gravity permitting. "
    "Please keep giant magnets away from your laptop."
)


def plain_text(text: str) -> dict[str, str]:
    return {"type": "plain_text", "text": text}


def provider(user_id: str) -> dict[str, Any]:
    username = connections.find(user_id)
    acme: dict[str, Any] = {
        "value": "acme",
        "name": plain_text("Acme account"),
        "description": plain_text(
            "Order rocket skates, anvils, and giant magnets without leaving Slack."
        ),
        "auth_url": f"{os.environ['BASE_URL']}{CONNECT_PATH}?state={issue(user_id)}",
        "is_connected": username is not None,
    }
    if username is not None:
        acme["connected_identity"] = plain_text(username)
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


def connect(client: WebClient, user_id: str, username: str):
    connections.connect(user_id, username)
    report(client, user_id)


def disconnect(client: WebClient, user_id: str):
    connections.disconnect(user_id)
    report(client, user_id)

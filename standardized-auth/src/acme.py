from typing import Any

from slack_sdk.models.blocks import AuthProviderBlock, SectionBlock
from slack_sdk.models.views import View

from src import connections


def provider(user_id: str) -> dict[str, Any]:
    acme: dict[str, Any] = {
        "value": "acme",
        "name": {"type": "plain_text", "text": "Acme account"},
        "description": {
            "type": "plain_text",
            "text": "Order rocket skates, anvils, and giant magnets without leaving Slack.",
        },
        "is_connected": connections.is_connected(user_id),
    }
    if acme["is_connected"]:
        acme["connected_identity"] = {"type": "plain_text", "text": user_id}
    return acme


def home_view(acme: dict[str, Any]) -> View:
    return View(
        type="home",
        blocks=[
            SectionBlock(
                text="*Welcome to Acme!* :rocket:\n"
                "Anvils ship same day, gravity permitting. "
                "Please keep giant magnets away from your laptop."
            ),
            AuthProviderBlock(**acme),
        ],
    )

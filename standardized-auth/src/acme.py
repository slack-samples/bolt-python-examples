import os
from typing import Any

from slack_bolt import BoltContext
from slack_sdk import WebClient
from slack_sdk.models.blocks import AuthProviderBlock, MarkdownTextObject, SectionBlock
from slack_sdk.models.views import View
from slack_sdk.oauth.installation_store import FileInstallationStore, Installation

installation_store = FileInstallationStore(base_dir="./data/installations")

GREETING = (
    "*Welcome to Acme!* :rocket:\n"
    "Anvils ship same day, gravity permitting. "
    "Please keep giant magnets away from your laptop."
)


def find_account(context: BoltContext, user_id: str) -> Installation | None:
    installation = installation_store.find_installation(
        enterprise_id=context.enterprise_id,
        team_id=context.team_id,
        user_id=user_id,
        is_enterprise_install=context.is_enterprise_install,
    )
    if installation is None or installation.user_token is None:
        return None
    return installation


def find_user_token(context: BoltContext, user_id: str) -> str | None:
    account = find_account(context, user_id)
    return None if account is None else account.user_token


def forget(context: BoltContext, user_id: str) -> str | None:
    account = find_account(context, user_id)
    if account is None:
        return None
    user_token = account.user_token
    account.user_token = None
    installation_store.save(account)
    return user_token


def plain_text(text: str) -> dict[str, str]:
    return {"type": "plain_text", "text": text}


def provider(client: WebClient, user_token: str | None) -> dict[str, Any]:
    acme: dict[str, Any] = {
        "value": "acme",
        "name": plain_text("Acme account"),
        "description": plain_text(
            "Order rocket skates, anvils, and giant magnets without leaving Slack."
        ),
        "auth_url": f"{os.environ['BASE_URL']}/slack/install",
        "is_connected": user_token is not None,
    }
    if user_token is not None:
        identity = client.auth_test(token=user_token)
        acme["connected_identity"] = plain_text(f"@{identity['user']}")
        acme["connected_context"] = plain_text(identity["team"])
    return acme


def home_view(acme: dict[str, Any]) -> View:
    return View(
        type="home",
        blocks=[
            SectionBlock(text=MarkdownTextObject(text=GREETING)),
            AuthProviderBlock(**acme),
        ],
    )


def report(client: WebClient, user_id: str, user_token: str | None = None):
    acme = provider(client, user_token)
    client.apps_user_connection_requestAuth(user_id=user_id, primary_provider=acme)
    client.views_publish(user_id=user_id, view=home_view(acme))


def disconnect(client: WebClient, context: BoltContext, user_id: str):
    forgotten_token = forget(context, user_id)
    report(client, user_id)
    if forgotten_token is not None:
        client.auth_revoke(token=forgotten_token)

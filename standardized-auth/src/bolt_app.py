import os
from importlib import import_module
from pkgutil import walk_packages

from slack_bolt import App, BoltResponse
from slack_bolt.oauth.callback_options import CallbackOptions, FailureArgs, SuccessArgs
from slack_bolt.oauth.oauth_settings import OAuthSettings
from slack_sdk import WebClient
from slack_sdk.oauth.installation_store import Installation
from slack_sdk.oauth.state_store.stateless import StatelessOAuthStateStore

from src import acme, listeners


def app_home_url(installation: Installation) -> str:
    team_id = installation.team_id or installation.enterprise_id
    return f"slack://app?team={team_id}&id={installation.app_id}&tab=home"


def success_callback(args: SuccessArgs) -> BoltResponse:
    installation = args.installation
    client = WebClient(token=installation.bot_token)
    acme.report(client, installation.user_id, installation.user_token)
    return BoltResponse(status=302, headers={"Location": app_home_url(installation)})


def failure_callback(args: FailureArgs) -> BoltResponse:
    return args.default.failure(args)


app = App(
    oauth_settings=OAuthSettings(
        scopes=["users:read"],
        user_scopes=["users.profile:read"],
        install_page_rendering_enabled=False,
        installation_store=acme.installation_store,
        state_store=StatelessOAuthStateStore(
            expiration_seconds=300,
            signing_secret=os.environ["SLACK_SIGNING_SECRET"],
        ),
        callback_options=CallbackOptions(
            success=success_callback, failure=failure_callback
        ),
    ),
)


def load_listeners() -> None:
    for module_info in walk_packages(listeners.__path__, f"{listeners.__name__}."):
        import_module(module_info.name)


load_listeners()

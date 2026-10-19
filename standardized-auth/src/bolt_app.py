import os
from importlib import import_module
from pathlib import Path

from slack_bolt import App, BoltResponse
from slack_bolt.oauth.callback_options import CallbackOptions, FailureArgs, SuccessArgs
from slack_bolt.oauth.oauth_settings import OAuthSettings
from slack_sdk import WebClient
from slack_sdk.oauth.state_store.stateless import StatelessOAuthStateStore

from src import acme


def success_callback(args: SuccessArgs) -> BoltResponse:
    installation = args.installation
    client = WebClient(token=installation.bot_token)
    acme.report(client, installation.user_id, installation.user_token)
    return args.default.success(args)


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


def import_listeners(directory: Path):
    for path in sorted(directory.glob("**/[!_]*.py")):
        module = path.relative_to(directory.parent).with_suffix("")
        import_module("." + ".".join(module.parts), __package__)


import_listeners(Path(__file__).parent / "listeners")

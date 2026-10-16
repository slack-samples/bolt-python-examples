from slack_bolt import App, BoltResponse
from slack_bolt.oauth.callback_options import CallbackOptions, FailureArgs
from slack_bolt.oauth.oauth_settings import OAuthSettings
from slack_sdk.oauth.installation_store import InstallationStore
from slack_sdk.oauth.state_store import OAuthStateStore

from src.accounts import AcmeAccounts
from src.acme import CONNECT_ACTION_ID, DISCONNECT_ACTION_ID
from src.listeners import AcmeListeners


def show_failure(args: FailureArgs) -> BoltResponse:
    return args.default.failure(args)


def build_app(
    installation_store: InstallationStore,
    state_store: OAuthStateStore,
    base_url: str,
) -> App:
    listeners = AcmeListeners(
        AcmeAccounts(installation_store), auth_url=f"{base_url}/slack/install"
    )
    app = App(
        oauth_settings=OAuthSettings(
            scopes=["users:read"],
            user_scopes=["users.profile:read"],
            install_page_rendering_enabled=False,
            installation_store=installation_store,
            state_store=state_store,
            callback_options=CallbackOptions(
                success=listeners.report_connected, failure=show_failure
            ),
        ),
    )
    app.event("app_home_opened")(listeners.publish_home)
    app.event("user_connection_status_requested")(listeners.answer_status_request)
    app.event("tokens_revoked")(listeners.forget_revoked_users)
    app.action(CONNECT_ACTION_ID)(listeners.acknowledge_connect)
    app.action(DISCONNECT_ACTION_ID)(listeners.acknowledge_disconnect)
    return app

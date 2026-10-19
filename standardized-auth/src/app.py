import os

from slack_bolt import App
from slack_bolt.oauth.oauth_settings import OAuthSettings
from slack_sdk.oauth.state_store.stateless import StatelessOAuthStateStore

from src import acme
from src.listeners import register_listeners
from src.listeners.oauth import callback_options


def build_app() -> App:
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
            callback_options=callback_options,
        ),
    )
    register_listeners(app)
    return app

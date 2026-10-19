from slack_bolt import App

from .app_home_opened import app_home_opened_callback
from .tokens_revoked import tokens_revoked_callback
from .user_connection_status_requested import user_connection_status_requested_callback


def register(app: App):
    app.event("app_home_opened")(app_home_opened_callback)
    app.event("tokens_revoked")(tokens_revoked_callback)
    app.event("user_connection_status_requested")(
        user_connection_status_requested_callback
    )

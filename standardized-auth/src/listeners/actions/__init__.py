from slack_bolt import App

from .connect import connect_callback
from .disconnect import disconnect_callback


def register(app: App):
    app.action("auth_provider_connect_acme")(connect_callback)
    app.action("auth_provider_disconnect_acme")(disconnect_callback)

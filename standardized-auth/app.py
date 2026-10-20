import os

from slack_bolt import Ack, App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient

from src.acme import connect, disconnect, home_view, provider
from src.connections import connections

app = App(token=os.environ["SLACK_BOT_TOKEN"])


@app.action("auth_provider_connect_acme")
def connect_callback(ack: Ack, body: dict, client: WebClient):
    ack()
    connect(client, body["user"]["id"])


@app.action("auth_provider_disconnect_acme")
def disconnect_callback(ack: Ack, body: dict, client: WebClient):
    ack()
    disconnect(client, body["user"]["id"])


@app.action("user_connection")
def user_connection_callback(ack: Ack, body: dict, client: WebClient):
    ack()
    user_id = body["user"]["id"]
    if body["subtype"] == "connect":
        client.apps_user_connection_requestAuth(
            trigger_id=body["trigger_id"], primary_provider=provider(user_id)
        )
    elif body["subtype"] == "disconnect":
        disconnect(client, user_id)


@app.event("app_home_opened")
def app_home_opened_callback(client: WebClient, event: dict):
    client.views_publish(user_id=event["user"], view=home_view(provider(event["user"])))


@app.event("user_connection_status_requested")
def user_connection_status_requested_callback(client: WebClient, event: dict):
    connected = connections.is_connected(event["user"])
    status = "connected" if connected else "disconnected"
    client.apps_user_connection_update(user_id=event["user"], status=status)


if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

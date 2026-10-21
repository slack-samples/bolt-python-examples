import os

from slack_bolt import Ack, App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient

from src import connections
from src.acme import PROVIDER_VALUE, home_view, provider

app = App(token=os.environ["SLACK_BOT_TOKEN"])


@app.event("app_home_opened")
def app_home_opened_callback(client: WebClient, event: dict):
    client.views_publish(user_id=event["user"], view=home_view(provider(event["user"])))


@app.action("auth_provider_connect")
def connect_callback(ack: Ack, body: dict, client: WebClient):
    ack()
    if body["actions"][0]["value"] != PROVIDER_VALUE:
        return
    user_id = body["user"]["id"]
    connections.connect(user_id)
    acme = provider(user_id)
    client.apps_user_connection_requestAuth(user_id=user_id, primary_provider=acme)
    client.views_publish(user_id=user_id, view=home_view(acme))


@app.action("auth_provider_disconnect")
def disconnect_callback(ack: Ack, body: dict, client: WebClient):
    ack()
    if body["actions"][0]["value"] != PROVIDER_VALUE:
        return
    user_id = body["user"]["id"]
    connections.disconnect(user_id)
    acme = provider(user_id)
    client.apps_user_connection_requestAuth(user_id=user_id, primary_provider=acme)
    client.views_publish(user_id=user_id, view=home_view(acme))


@app.event("user_connection")
def user_connection_callback(client: WebClient, event: dict):
    if event["subtype"] == "connect":
        client.apps_user_connection_requestAuth(
            trigger_id=event["trigger_id"], primary_provider=provider(event["user"])
        )


@app.event("user_connection_status_requested")
def user_connection_status_requested_callback(client: WebClient, event: dict):
    status = "connected" if connections.is_connected(event["user"]) else "disconnected"
    client.apps_user_connection_update(user_id=event["user"], status=status)


if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

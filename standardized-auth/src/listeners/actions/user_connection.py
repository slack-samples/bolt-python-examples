from slack_bolt import Ack
from slack_sdk import WebClient

from src.acme import disconnect, provider
from src.bolt_app import app


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

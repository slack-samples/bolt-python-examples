from slack_bolt import Ack, BoltContext
from slack_sdk import WebClient

from src.acme import disconnect, find_user_token, provider
from src.bolt_app import app


@app.action("user_connection")
def user_connection_callback(
    ack: Ack, body: dict, client: WebClient, context: BoltContext
):
    ack()
    user_id = body["user"]["id"]
    if body["subtype"] == "connect":
        user_token = find_user_token(context, user_id)
        client.apps_user_connection_requestAuth(
            trigger_id=body["trigger_id"],
            primary_provider=provider(client, user_token),
        )
    elif body["subtype"] == "disconnect":
        disconnect(client, context, user_id)

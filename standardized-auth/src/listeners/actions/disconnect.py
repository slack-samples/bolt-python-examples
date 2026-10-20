from slack_bolt import Ack
from slack_sdk import WebClient

from src.acme import disconnect
from src.bolt_app import app


@app.action("auth_provider_disconnect_acme")
def disconnect_callback(ack: Ack, body: dict, client: WebClient):
    ack()
    disconnect(client, body["user"]["id"])

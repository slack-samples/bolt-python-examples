from slack_bolt import Ack
from slack_sdk import WebClient

from src.acme import connect
from src.bolt_app import app


@app.action("auth_provider_connect_acme")
def connect_callback(ack: Ack, body: dict, client: WebClient):
    ack()
    connect(client, body["user"]["id"])

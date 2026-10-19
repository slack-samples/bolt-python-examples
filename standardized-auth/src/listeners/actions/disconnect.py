from slack_bolt import Ack, BoltContext
from slack_sdk import WebClient

from src.acme import disconnect


def disconnect_callback(ack: Ack, body: dict, client: WebClient, context: BoltContext):
    ack()
    disconnect(client, context, body["user"]["id"])

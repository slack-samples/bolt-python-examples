from slack_bolt import BoltContext
from slack_sdk import WebClient

from src.acme import forget, report


def tokens_revoked_callback(client: WebClient, context: BoltContext, event: dict):
    for user_id in event["tokens"].get("oauth", []):
        forget(context, user_id)
        report(client, user_id)

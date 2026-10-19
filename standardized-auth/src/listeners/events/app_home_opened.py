from slack_bolt import BoltContext
from slack_sdk import WebClient

from src.acme import find_user_token, home_view, provider


def app_home_opened_callback(client: WebClient, context: BoltContext, event: dict):
    user_token = find_user_token(context, event["user"])
    client.views_publish(
        user_id=event["user"], view=home_view(provider(client, user_token))
    )

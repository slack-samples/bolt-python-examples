from slack_bolt import BoltContext
from slack_sdk import WebClient

from src.acme import find_user_token
from src.app import app


@app.event("user_connection_status_requested")
def user_connection_status_requested_callback(
    client: WebClient, context: BoltContext, event: dict
):
    user_token = find_user_token(context, event["user"])
    status = "disconnected" if user_token is None else "connected"
    client.apps_user_connection_update(user_id=event["user"], status=status)

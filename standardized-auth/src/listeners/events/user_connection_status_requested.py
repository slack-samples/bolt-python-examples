from slack_sdk import WebClient

from src.bolt_app import app
from src.connections import connections


@app.event("user_connection_status_requested")
def user_connection_status_requested_callback(client: WebClient, event: dict):
    connected = connections.is_connected(event["user"])
    status = "connected" if connected else "disconnected"
    client.apps_user_connection_update(user_id=event["user"], status=status)

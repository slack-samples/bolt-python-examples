from slack_sdk import WebClient

from src.acme import home_view, provider
from src.bolt_app import app


@app.event("app_home_opened")
def app_home_opened_callback(client: WebClient, event: dict):
    client.views_publish(user_id=event["user"], view=home_view(provider(event["user"])))

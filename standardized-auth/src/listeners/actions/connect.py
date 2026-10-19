from slack_bolt import Ack

from src.app import app


@app.action("auth_provider_connect_acme")
def connect_callback(ack: Ack):
    ack()

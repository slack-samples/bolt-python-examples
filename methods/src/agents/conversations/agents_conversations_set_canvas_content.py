import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the agents.conversations.setCanvasContent method
response = client.agents_conversations_setCanvasContent(
    channel="C9876543210",
    canvas_id="F1234567890",
    content="# Migration plan\n\n1. Inventory cron jobs\n2. Port billing jobs last\n",
)

# Inspect the response
print(response)

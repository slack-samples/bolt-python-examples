import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the agents.conversations.getCanvas method
response = client.agents_conversations_getCanvas(
    channel="C9876543210",
    canvas_id="F1234567890",
    include_resolved=False,
)

# Inspect the response
print(response)

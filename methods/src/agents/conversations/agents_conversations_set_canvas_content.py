import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the agents.conversations.setCanvasContent method
response = client.agents_conversations_setCanvasContent(
    channel="C123ABC456",
    canvas_id="F123ABC456",
    content="# Plan\n\n1. Reproduce the flaky test\n2. Fix the race\n3. Verify",
)

# Inspect the response
print(response)

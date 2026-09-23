import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the agents.conversations.removeView method
response = client.agents_conversations_removeView(
    channel_id="C123ABC456",
    view_id="V123ABC456",
)

# Inspect the response
print(response)

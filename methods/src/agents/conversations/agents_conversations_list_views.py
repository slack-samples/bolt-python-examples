import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the agents.conversations.listViews method
response = client.agents_conversations_listViews(
    channel_id="C9876543210",
)

# Inspect the response
print(response)

import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the agents.conversations.archive method
response = client.agents_conversations_archive(
    channel_id="C9876543210",
    summary_message_ts="1717182000.456789",
)

# Inspect the response
print(response)

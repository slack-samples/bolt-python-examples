import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the agents.conversations.create method
response = client.agents_conversations_create(
    name="Migrate billing cron to Temporal",
    session_id="ses_8675309",
    origin_channel_id="C0123456789",
    origin_message_ts="1717171717.123456",
)

# Inspect the response
print(response)

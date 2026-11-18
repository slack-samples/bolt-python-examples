import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the admin.conversations.bulkSetProperties method
response = client.admin_conversations_bulkSetProperties(
    channel_ids=["C0123456789"],
    property={
        "exclude_from_slack_ai": True,
    },
)

# Inspect the response
print(response)

import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the agents.conversations.setProperties method
response = client.agents_conversations_setProperties(
    channel_id="C123ABC456",
    code_channel={
        "context_bar_items": [
            {
                "key": "repo",
                "label": "acme/billing",
                "icon": "folder",
                "url": "https://github.com/acme/billing",
            },
        ]
    },
)

# Inspect the response
print(response)

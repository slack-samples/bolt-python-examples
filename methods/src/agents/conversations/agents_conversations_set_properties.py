import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the agents.conversations.setProperties method
response = client.agents_conversations_setProperties(
    channel_id="C9876543210",
    code_channel={
        "context_bar_items": [
            {
                "key": "repo",
                "label": "borant/billing",
                "icon": "folder",
                "url": "https://github.com/borant/billing",
            },
            {
                "key": "branch",
                "label": "agent/migrate-cron",
                "icon": "branch",
                "url": "https://github.com/borant/billing/tree/agent/migrate-cron",
            },
            {
                "key": "pr",
                "label": "PR #42 is open",
                "icon": "hierarchy",
                "url": "https://github.com/borant/billing/pull/42",
            },
            {
                "key": "ci",
                "label": "Tests pending",
                "icon": "terminal",
            },
        ]
    },
)

# Inspect the response
print(response)

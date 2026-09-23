import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the agents.conversations.setView method
response = client.agents_conversations_setView(
    channel_id="C123ABC456",
    type="diff",
    content="diff --git a/cron.py b/cron.py\n--- a/cron.py\n+++ b/cron.py\n@@ ...",
    base_branch="main",
    head_branch="agent/migrate-cron",
)

# Inspect the response
print(response)

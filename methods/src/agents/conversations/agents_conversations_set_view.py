import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the agents.conversations.setView method
response = client.agents_conversations_setView(
    channel_id="C9876543210",
    view_key="reports/coverage.html",
    name="Coverage",
    content="<!doctype html><html><head>…</head><body>…</body></html>",
    csp={
        "resource_domains": ["https://cdn.jsdelivr.net"],
    },
)

# Inspect the response
print(response)

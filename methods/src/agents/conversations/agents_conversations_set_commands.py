import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the agents.conversations.setCommands method
response = client.agents_conversations_setCommands(
    channel_id="C123ABC456",
    commands=[
        {
            "name": "test",
            "description": "Run the test suite",
        },
        {
            "name": "diff",
            "description": "Show the current diff",
        },
    ],
)

# Inspect the response
print(response)

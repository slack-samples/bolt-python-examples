import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the agents.conversations.setCommands method
response = client.agents_conversations_setCommands(
    channel_id="C9876543210",
    commands=[
        {
            "name": "create-pr",
            "description": "Open a pull request for the current branch",
            "argument_hint": "[title]",
        },
        {
            "name": "run-tests",
            "description": "Run the test suite and report back",
        },
        {
            "name": "summarize",
            "description": "Post a summary of the work so far",
        },
    ],
)

# Inspect the response
print(response)

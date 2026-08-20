import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the agents.sessions.rename method
response = client.agents_sessions_rename(
    channel_id="C123ABC456",
    title="Fix flaky login test",
)

# Inspect the response
print(response)

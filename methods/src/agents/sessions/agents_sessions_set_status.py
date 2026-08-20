import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the agents.sessions.setStatus method
response = client.agents_sessions_setStatus(
    channel_id="C123ABC456",
    status="processing",
)

# Inspect the response
print(response)

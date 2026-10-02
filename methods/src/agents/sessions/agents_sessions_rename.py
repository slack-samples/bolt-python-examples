import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the agents.sessions.rename method
response = client.agents_sessions_rename(
    channel_id="C123ABC",
    thread_ts="1717171717.123456",
    title="Bora Bora trip prep",
)

# Inspect the response
print(response)

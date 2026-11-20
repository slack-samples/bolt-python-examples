import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the chat.startStream method
response = client.chat_startStream(
    channel="C123ABC456",
    markdown_text="**This is bold text**",
    thread_ts="1721609600.123456",
    recipient_user_id="U0123456789",
    recipient_team_id="T0123456789",
)

# Inspect the response
print(response)

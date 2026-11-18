import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the chat.stopStream method
response = client.chat_stopStream(
    channel="C123ABC456",
    ts="1234567890.123456",
)

# Inspect the response
print(response)

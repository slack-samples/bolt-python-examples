import os

from slack_sdk import WebClient

# Read a token from the environment variables
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the chat.postMessage method
client.chat_postMessage(
    channel="C123ABC456",
    text="Here's a message for you",
)

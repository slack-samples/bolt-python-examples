import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the chat.startStream method
response = client.chat_startStream(
    channel="C123ABC456",
    thread_ts="1234567890.123456",
    markdown_text="Let me look into that",
)

# Inspect the response
print(response)

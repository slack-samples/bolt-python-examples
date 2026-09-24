import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the chat.appendStream method
response = client.chat_appendStream(
    channel="C123ABC456",
    ts="1234567890.123456",
    markdown_text=" — reading the logs now",
)

# Inspect the response
print(response)

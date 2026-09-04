import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the codeChannels.archive method
response = client.codeChannels_archive(
    channel_id="C123ABC456",
    summary_message_ts="1717171717.123456",
)

# Inspect the response
print(response)

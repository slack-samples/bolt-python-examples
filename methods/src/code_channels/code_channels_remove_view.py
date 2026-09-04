import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the codeChannels.removeView method
response = client.codeChannels_removeView(
    channel_id="C123ABC456",
    view_id="V123ABC456",
)

# Inspect the response
print(response)

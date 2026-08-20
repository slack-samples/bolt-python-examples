import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the codeChannels.getCanvas method
response = client.codeChannels_getCanvas(
    channel_id="C123ABC456",
    canvas_id="F123ABC456",
)

# Inspect the response
print(response)

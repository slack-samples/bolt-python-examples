import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the codeChannels.rename method
response = client.codeChannels_rename(
    channel_id="C123ABC456",
    name="Fix flaky login test v2",
)

# Inspect the response
print(response)

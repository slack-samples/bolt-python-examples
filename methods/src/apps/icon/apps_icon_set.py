import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the apps.icon.set method
response = client.apps_icon_set(
    app_id="A0123456789",
    url="https://example.com/icon.png",
)

# Inspect the response
print(response)

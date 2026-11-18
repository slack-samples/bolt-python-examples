import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the apps.managed.permissions.set method
response = client.apps_managed_permissions_set(
    app_id="A0123456789",
    permissions="everyone",
)

# Inspect the response
print(response)

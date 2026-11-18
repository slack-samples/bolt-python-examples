import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the admin.apps.mcp.servers.permissions.list method
response = client.admin_apps_mcp_servers_permissions_list(
    app_id="A0000000001",
)

# Inspect the response
print(response)

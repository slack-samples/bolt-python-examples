import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the admin.apps.mcp.servers.list method
response = client.admin_apps_mcp_servers_list()

# Inspect the response
print(response)

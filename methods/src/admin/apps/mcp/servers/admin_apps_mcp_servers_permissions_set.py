import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the admin.apps.mcp.servers.permissions.set method
response = client.admin_apps_mcp_servers_permissions_set(
    app_id="A0123ABCD",
    server_id="Amcp0456EFGH",
    permission_type="named_entities",
    user_ids=["U0123ABCD"],
    usergroup_ids=["S0123ABCD"],
)

# Inspect the response
print(response)

import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the admin.apps.mcp.servers.permissions.set method
response = client.admin_apps_mcp_servers_permissions_set(
    app_id="A0000000001",
    server_id="Amcp0000000001",
    permission_type="named_entities",
    user_ids=["U00000001", "U00000002"],
    usergroup_ids=["S00000001", "S00000002"],
)

# Inspect the response
print(response)

from slack_sdk import WebClient

# Initialize
client = WebClient()

# Call the oauth.v2.user.access method
response = client.oauth_v2_user_access(
    client_id="2141029472.691202649728",
    client_secret="e1b9e11dfcd19c1982d5de12921e17e8c",
    code="4724469134.4644010092847.232b4e6d82c333b475fc30f5f5a341d294feb1a94392c2fd791f7ab7731a443d1a",
)

# Inspect the response
print(response)

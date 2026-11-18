from slack_sdk import WebClient

# Initialize
client = WebClient()

# Call the oauth.v2.beginShortTokenRotation method
response = client.oauth_v2_beginShortTokenRotation(
    client_id="4123121235.9872358710",
    client_secret="e1b9e11dfcd19c1982d5de12921e17e8c",
    token="xoxp-12345-67890-1928471-abcdefg",
)

# Inspect the response
print(response)

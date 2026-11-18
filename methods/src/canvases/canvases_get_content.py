import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the canvases.getContent method
response = client.canvases_getContent(
    canvas_id="F1234ABCD",
    content_type="markdown",
)

# Inspect the response
print(response)

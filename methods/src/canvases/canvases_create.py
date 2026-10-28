import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the canvases.create method
response = client.canvases_create(
    title="Your Brilliant Title",
    document_content={
        "type": "markdown",
        "markdown": "> standalone canvas!",
    },
)

# Inspect the response
print(response)

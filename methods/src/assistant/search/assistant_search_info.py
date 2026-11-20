import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the assistant.search.info method
response = client.assistant_search_info()

# Inspect the response
print(response)

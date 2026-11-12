import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the slackbot.skills.list method
response = client.slackbot_skills_list(
    filter="library",
    category="productivity",
    limit=100,
)

# Inspect the response
print(response)

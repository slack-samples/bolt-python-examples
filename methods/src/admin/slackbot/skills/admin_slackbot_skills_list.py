import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the admin.slackbot.skills.list method
response = client.admin_slackbot_skills_list(
    category="productivity",
    creator_ids=["U0123ABCD"],
)

# Inspect the response
print(response)

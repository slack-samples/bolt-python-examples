import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the admin.slackbot.skills.unpublish method
response = client.admin_slackbot_skills_unpublish(
    skill_ids=["F0123ABCD"],
)

# Inspect the response
print(response)

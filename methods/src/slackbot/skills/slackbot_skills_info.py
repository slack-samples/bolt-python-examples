import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the slackbot.skills.info method
response = client.slackbot_skills_info(
    skill_id="F0123ABCD",
)

# Inspect the response
print(response)

import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the slackbot.skills.library.remove method
response = client.slackbot_skills_library_remove(
    skill_id="F0123ABCD",
)

# Inspect the response
print(response)

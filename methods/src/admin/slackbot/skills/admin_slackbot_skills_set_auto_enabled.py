import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the admin.slackbot.skills.setAutoEnabled method
response = client.admin_slackbot_skills_setAutoEnabled(
    skill_id="F0123ABCD",
    permission_type="named_entities",
    usergroup_ids=["S0123ABCD"],
)

# Inspect the response
print(response)

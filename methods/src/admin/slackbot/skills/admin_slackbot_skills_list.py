import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the admin.slackbot.skills.list method
response = client.admin_slackbot_skills_list(
    category="productivity",
    limit=100,
    creator_ids=["U0123ABCD"],
    publish_status="published",
    auto_enabled_status="enabled",
    sort="usage_count",
    sort_dir="desc",
)

# Inspect the response
print(response)

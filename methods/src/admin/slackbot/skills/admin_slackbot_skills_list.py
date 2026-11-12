import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the admin.slackbot.skills.list method
response = client.admin_slackbot_skills_list(
    auto_enabled_status="enabled",
    category="productivity",
    creator_ids=["U0123ABCD"],
    limit=100,
    publish_status="published",
    sort="usage_count",
    sort_dir="desc",
)

# Inspect the response
print(response)

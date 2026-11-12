import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the slackbot.skills.create method
response = client.slackbot_skills_create(
    display_name="Daily priorities",
    instructions="# Purpose\nSuggest the three most important things to work on today.",
    description="Reviews information from Slack and your calendar to suggest priorities for the day.",
    category="productivity",
    example_prompt="Run {skill} for today",
    mcp_servers=[
        {
            "service_type": "app",
            "app_id": "A0123ABCD",
            "server_id": "Amcp0456EFGH",
        },
    ],
)

# Inspect the response
print(response)

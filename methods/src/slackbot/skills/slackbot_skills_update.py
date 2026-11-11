import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the slackbot.skills.update method
response = client.slackbot_skills_update(
    skill_id="F0123ABCD",
    category="productivity",
    description="Reviews information from Slack and your calendar to suggest priorities for the day.",
    display_name="Daily priorities",
    example_prompt="Run {skill} for today",
    instructions="# Purpose\nSuggest the three most important things to work on today.",
    mcp_servers=[
        {
            "app_id": "A0123ABCD",
            "server_id": "Amcp0456EFGH",
            "service_type": "app",
        },
    ],
)

# Inspect the response
print(response)

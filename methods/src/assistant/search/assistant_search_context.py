import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the assistant.search.context method
response = client.assistant_search_context(
    query="What is the latest on project Gizmo?",
    term_clauses=["project gizmo"],
    action_token="12345.98765.abcd2358fdea",
    channel_types=["public_channel", "private_channel", "mpim", "im"],
    content_types=["messages", "files", "channels"],
    include_context_messages=True,
    include_bots=False,
    sort="timestamp",
    sort_dir="asc",
    before=1755191113,
    after=1752512713,
    include_message_blocks=True,
)

# Inspect the response
print(response)

import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the entity.acknowledgeCommentAction method
response = client.entity_acknowledgeCommentAction(
    trigger_id="1234567890123.1234567890123.abcdef01234567890abcdef012345689",
    comment={
        "id": "comment-unique-identifier-003",
        "sender": {
            "user_id": "U123456789",
        },
        "comment": {
            "value": "The saved comment text",
            "format": "markdown",
        },
        "timestamp": 1741164500,
        "url": "your.app/item/1/comment/3",
        "thread_root_id": "comment-unique-identifier-001",
    },
)

# Inspect the response
print(response)

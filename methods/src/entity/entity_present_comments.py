import os

from slack_sdk import WebClient

# Read a token from an environment variable
token = os.environ.get("SLACK_TOKEN")

# Initialize
client = WebClient(token=token)

# Call the entity.presentComments method
response = client.entity_presentComments(
    comments=[
        {
            "sender": {
                "user_id": "U123456789",
            },
            "timestamp": 1741164235,
            "id": "comment-unique-identifier-001",
            "url": "your.app/item/1/comment/1",
            "can_edit": True,
            "can_delete": True,
            "can_reply": True,
            "reply_count": 2,
            "reply_users": [
                {
                    "user_id": "U234567890",
                },
                {
                    "text": "External User",
                    "icon": {
                        "url": "...",
                    },
                },
            ],
            "latest_reply_ts": 1741165000,
            "last_edit_ts": 1741164300,
            "comment": {
                "blocks": {
                    "type": "rich_text",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Check out these different block types with paragraph breaks between them:\n\n",
                                },
                            ],
                        },
                    ],
                },
            },
        },
        {
            "sender": {
                "text": "UserFirstName UserLastName",
                "icon": {
                    "alt_text": "Summary of image's content",
                    "url": "...",
                },
                "url": "your.app/user/userId",
                "email": "firstname.lastname@domain.com",
            },
            "timestamp": 1741164358,
            "id": "comment-unique-identifier-002",
            "url": "your.app/item/1/comment/2",
            "thread_root_id": "comment-unique-identifier-001",
            "comment": {
                "value": "Plain text comment",
                "format": "markdown",
            },
        },
    ],
    trigger_id="1234567890123.1234567890123.abcdef01234567890abcdef012345689",
    can_post_comment=True,
    delete_action_id="your-delete-action-id",
)

# Inspect the response
print(response)

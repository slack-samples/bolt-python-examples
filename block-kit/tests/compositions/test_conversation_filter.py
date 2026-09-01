import json

from src.compositions import conversation_filter


def test_example01():
    view = conversation_filter.example01()
    actual = view.to_dict()
    expected = {
        "title": {
            "type": "plain_text",
            "text": "My App",
            "emoji": True,
        },
        "submit": {
            "type": "plain_text",
            "text": "Submit",
            "emoji": True,
        },
        "type": "modal",
        "close": {
            "type": "plain_text",
            "text": "Cancel",
            "emoji": True,
        },
        "blocks": [
            {
                "type": "input",
                "element": {
                    "type": "conversations_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select a conversation",
                        "emoji": True,
                    },
                    "filter": {
                        "include": ["public", "mpim"],
                        "exclude_bot_users": True,
                    },
                },
                "label": {
                    "type": "plain_text",
                    "text": "Choose the conversation to publish your result to:",
                    "emoji": True,
                },
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

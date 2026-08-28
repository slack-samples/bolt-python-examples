import json

from src.composition_objects import confirmation_dialog


def test_example01():
    block = confirmation_dialog.example01()
    actual = block.to_dict()
    expected = {
        "type": "actions",
        "elements": [
            {
                "type": "button",
                "text": {"type": "plain_text", "emoji": True, "text": "Approve"},
                "confirm": {
                    "title": {"type": "plain_text", "text": "Are you sure?"},
                    "text": {
                        "type": "mrkdwn",
                        "text": "Would you not prefer a good game of _chess_?",
                    },
                    "confirm": {"type": "plain_text", "text": "Do it"},
                    "deny": {
                        "type": "plain_text",
                        "text": "Stop, I changed my mind!",
                    },
                },
                "style": "primary",
                "value": "click_me_123",
            },
            {
                "type": "button",
                "text": {"type": "plain_text", "emoji": True, "text": "Deny"},
                "style": "danger",
                "value": "click_me_123",
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

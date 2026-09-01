import json

from src.elements import overflow_menu


def test_example01():
    block = overflow_menu.example01()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "block_id": "section 890",
        "text": {
            "type": "mrkdwn",
            "text": "This is a section block with an overflow menu.",
        },
        "accessory": {
            "type": "overflow",
            "action_id": "overflow",
            "options": [
                {
                    "text": {
                        "type": "plain_text",
                        "text": "*this is plain_text text*",
                    },
                    "value": "value-0",
                },
                {
                    "text": {
                        "type": "plain_text",
                        "text": "*this is plain_text text*",
                    },
                    "value": "value-1",
                },
                {
                    "text": {
                        "type": "plain_text",
                        "text": "*this is plain_text text*",
                    },
                    "value": "value-2",
                },
                {
                    "text": {
                        "type": "plain_text",
                        "text": "*this is plain_text text*",
                    },
                    "value": "value-3",
                },
                {
                    "text": {
                        "type": "plain_text",
                        "text": "*this is plain_text text*",
                    },
                    "value": "value-4",
                },
            ],
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

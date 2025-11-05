import json

from src.blocks import context_actions


def test_example01():
    block = context_actions.example01()
    actual = block.to_dict()
    expected = {
        "type": "context_actions",
        "elements": [
            {
                "type": "feedback_buttons",
                "action_id": "feedback_buttons_1",
                "positive_button": {
                    "text": {
                        "type": "plain_text",
                        "text": "👍",
                    },
                    "value": "positive_feedback",
                },
                "negative_button": {
                    "text": {
                        "type": "plain_text",
                        "text": "👎",
                    },
                    "value": "negative_feedback",
                },
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example02():
    block = context_actions.example02()
    actual = block.to_dict()
    expected = {
        "type": "context_actions",
        "elements": [
            {
                "type": "icon_button",
                "icon": "trash",
                "text": {
                    "type": "plain_text",
                    "text": "Delete",
                },
                "action_id": "delete_button_1",
                "value": "delete_item",
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

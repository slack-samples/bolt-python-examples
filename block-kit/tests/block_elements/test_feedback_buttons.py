import json

from src.block_elements import feedback_buttons


def test_example01():
    block = feedback_buttons.example01()
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
                        "text": "Good",
                    },
                    "value": "positive_feedback",
                    "accessibility_label": "Mark this response as good",
                },
                "negative_button": {
                    "text": {
                        "type": "plain_text",
                        "text": "Bad",
                    },
                    "value": "negative_feedback",
                    "accessibility_label": "Mark this response as bad",
                },
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

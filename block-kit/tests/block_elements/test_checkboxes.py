import json

from src.block_elements import checkboxes


def test_example01():
    block = checkboxes.example01()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "text": {"type": "plain_text", "text": "Check out these charming checkboxes"},
        "accessory": {
            "type": "checkboxes",
            "action_id": "this_is_an_action_id",
            "initial_options": [
                {"value": "A1", "text": {"type": "plain_text", "text": "Checkbox 1"}},
            ],
            "options": [
                {"value": "A1", "text": {"type": "plain_text", "text": "Checkbox 1"}},
                {
                    "value": "A2",
                    "text": {"type": "plain_text", "text": "Checkbox 2"},
                    "description": {
                        "type": "mrkdwn",
                        "text": "*A description of option two*",
                    },
                },
            ],
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

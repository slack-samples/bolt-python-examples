import json

from src.elements import radio_buttons


def test_example01():
    block = radio_buttons.example01()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "text": {
            "type": "plain_text",
            "text": "Check out these rad radio buttons",
        },
        "accessory": {
            "type": "radio_buttons",
            "action_id": "this_is_an_action_id",
            "initial_option": {
                "value": "A1",
                "text": {
                    "type": "plain_text",
                    "text": "Radio 1",
                },
            },
            "options": [
                {
                    "value": "A1",
                    "text": {
                        "type": "plain_text",
                        "text": "Radio 1",
                    },
                },
                {
                    "value": "A2",
                    "text": {
                        "type": "plain_text",
                        "text": "Radio 2",
                    },
                },
            ],
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

import json

from src.elements import time_picker


def test_example01():
    block = time_picker.example01()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "block_id": "section1234",
        "text": {
            "type": "mrkdwn",
            "text": "Pick a date for the deadline.",
        },
        "accessory": {
            "type": "timepicker",
            "timezone": "America/Los_Angeles",
            "action_id": "timepicker123",
            "initial_time": "11:40",
            "placeholder": {
                "type": "plain_text",
                "text": "Select a time",
            },
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

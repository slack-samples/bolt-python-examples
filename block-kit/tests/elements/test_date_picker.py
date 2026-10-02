import json

from src.elements import date_picker


def test_example01():
    block = date_picker.example01()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "block_id": "section1234",
        "text": {
            "type": "mrkdwn",
            "text": "Pick a date for the deadline.",
        },
        "accessory": {
            "type": "datepicker",
            "action_id": "datepicker123",
            "initial_date": "1990-04-28",
            "placeholder": {
                "type": "plain_text",
                "text": "Select a date",
            },
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

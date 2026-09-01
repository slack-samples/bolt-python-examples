import json

from src.elements import datetime_picker


def test_example01():
    block = datetime_picker.example01()
    actual = block.to_dict()
    expected = {
        "type": "input",
        "element": {
            "type": "datetimepicker",
            "action_id": "datetimepicker-action",
        },
        "hint": {
            "type": "plain_text",
            "text": "This is some hint text",
            "emoji": True,
        },
        "label": {
            "type": "plain_text",
            "text": "Start date",
            "emoji": True,
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

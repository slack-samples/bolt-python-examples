import json

from src.elements import plain_text_input


def test_example01():
    block = plain_text_input.example01()
    actual = block.to_dict()
    expected = {
        "type": "input",
        "element": {
            "type": "plain_text_input",
            "action_id": "plain_text_input-action",
        },
        "label": {
            "type": "plain_text",
            "text": "Label",
            "emoji": True,
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

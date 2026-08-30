import json

from src.elements import url_input


def test_example01():
    block = url_input.example01()
    actual = block.to_dict()
    expected = {
        "type": "input",
        "element": {
            "type": "url_text_input",
            "action_id": "url_text_input-action",
        },
        "label": {
            "type": "plain_text",
            "text": "Label",
            "emoji": True,
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

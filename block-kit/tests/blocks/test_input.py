import json

from src.blocks import input


def test_example01():
    block = input.example01()
    actual = block.to_dict()
    expected = {
        "type": "input",
        "element": {
            "type": "plain_text_input",
        },
        "label": {
            "type": "plain_text",
            "text": "Label",
            "emoji": True,
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

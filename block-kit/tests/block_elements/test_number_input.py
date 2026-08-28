import json

from src.block_elements import number_input


def test_example01():
    block = number_input.example01()
    actual = block.to_dict()
    expected = {
        "type": "input",
        "element": {
            "type": "number_input",
            "is_decimal_allowed": False,
            "action_id": "number_input-action",
        },
        "label": {
            "type": "plain_text",
            "text": "Label",
            "emoji": True,
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

import json

from src.blocks import header


def test_example01():
    block = header.example01()
    actual = block.to_dict()
    expected = {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "A Heartfelt Header",
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

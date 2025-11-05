import json

from src.blocks import divider


def test_example01():
    block = divider.example01()
    actual = block.to_dict()
    expected = {
        "type": "divider",
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

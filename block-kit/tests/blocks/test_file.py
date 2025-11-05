import json

from src.blocks import file


def test_example01():
    block = file.example01()
    actual = block.to_dict()
    expected = {
        "type": "file",
        "external_id": "ABCD1",
        "source": "remote",
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

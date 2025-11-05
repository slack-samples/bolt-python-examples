import json

from src.blocks import markdown


def test_example01():
    block = markdown.example01()
    actual = block.to_dict()
    expected = {
        "type": "markdown",
        "text": "**Lots of information here!!**",
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

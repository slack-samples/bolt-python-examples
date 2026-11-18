import json

from src.compositions import text


def test_example01():
    block = text.example01()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "A message *with some bold text* and _some italicized text_.",
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

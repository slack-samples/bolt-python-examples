import json

from src.blocks import alert


def test_example01():
    block = alert.example01()
    actual = block.to_dict()
    expected = {
        "type": "alert",
        "text": {
            "type": "mrkdwn",
            "text": "The work is mysterious and important.",
        },
        "level": "info",
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

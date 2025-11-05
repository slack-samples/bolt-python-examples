import json

from src.blocks import context


def test_example01():
    block = context.example01()
    actual = block.to_dict()
    expected = {
        "type": "context",
        "elements": [
            {
                "type": "image",
                "image_url": "https://image.freepik.com/free-photo/red-drawing-pin_1156-445.jpg",
                "alt_text": "images",
            },
            {
                "type": "mrkdwn",
                "text": "Location: **Dogpatch**",
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

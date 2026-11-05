import json

from src.elements import channel


def test_example01():
    block = channel.example01()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [
                    {
                        "type": "channel",
                        "channel_id": "C123ABC456",
                    },
                ],
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

import json

from src.block_elements import emoji


def test_example01():
    block = emoji.example01()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [
                    {
                        "type": "emoji",
                        "name": "basketball",
                    },
                    {
                        "type": "text",
                        "text": " ",
                    },
                    {
                        "type": "emoji",
                        "name": "snowboarder",
                    },
                    {
                        "type": "text",
                        "text": " ",
                    },
                    {
                        "type": "emoji",
                        "name": "checkered_flag",
                    },
                ],
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

import json

from src.block_elements import text


def test_example01():
    block = text.example01()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [
                    {
                        "type": "text",
                        "text": "Hello there, ",
                    },
                    {
                        "type": "text",
                        "text": "I am a bold rich text block!",
                        "style": {
                            "bold": True,
                        },
                    },
                ],
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

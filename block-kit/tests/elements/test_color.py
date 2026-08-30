import json

from src.elements import color


def test_example01():
    block = color.example01()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [
                    {
                        "type": "color",
                        "value": "#F405B3",
                    },
                ],
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

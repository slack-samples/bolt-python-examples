import json

from src.elements import date


def test_example01():
    block = date.example01()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [
                    {
                        "type": "date",
                        "timestamp": 1720710212,
                        "format": "{date_num} at {time}",
                        "fallback": "timey",
                    },
                ],
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

import json

from src.elements import link


def test_example01():
    block = link.example01()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [
                    {
                        "type": "link",
                        "url": "https://docs.slack.dev",
                    },
                ],
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

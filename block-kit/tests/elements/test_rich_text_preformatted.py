import json

from src.elements import rich_text_preformatted


def test_example01():
    block = rich_text_preformatted.example01()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_preformatted",
                "border": 0,
                "elements": [
                    {
                        "type": "text",
                        "text": '{\n  "object": {\n    "description": "this is an example of a json object"\n  }\n}',
                    },
                ],
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

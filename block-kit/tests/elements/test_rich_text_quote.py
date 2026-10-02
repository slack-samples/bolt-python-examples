import json

from src.elements import rich_text_quote


def test_example01():
    block = rich_text_quote.example01()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "block_id": "Vrzsu",
        "elements": [
            {
                "type": "rich_text_quote",
                "elements": [
                    {
                        "type": "text",
                        "text": "What we need is good examples in our documentation.",
                    },
                ],
            },
            {
                "type": "rich_text_section",
                "elements": [
                    {
                        "type": "text",
                        "text": "Yes - I completely agree, Luke!",
                    },
                ],
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

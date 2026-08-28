import json

from src.block_elements import attachment_mention


def test_example01():
    block = attachment_mention.example01()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [
                    {
                        "type": "attachment_mention",
                        "url": "https://example.com/attachment",
                    }
                ],
            }
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

import json

from src.blocks import table


def test_example01():
    block = table.example01()
    actual = block.to_dict()
    expected = {
        "type": "table",
        "block_id": "optional_unique_id",
        "column_settings": [
            {"is_wrapped": True, "align": "left"},
            {"align": "right", "is_wrapped": False},
        ],
        "rows": [
            [
                {"type": "raw_text", "text": "Header A"},
                {"type": "raw_text", "text": "Header B"},
            ],
            [
                {"type": "raw_text", "text": "Data 1A"},
                {
                    "type": "rich_text",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "link",
                                    "text": "Data 1B",
                                    "url": "https://slack.com",
                                }
                            ],
                        }
                    ],
                },
            ],
            [
                {"type": "raw_text", "text": "Data 2A"},
                {"type": "raw_number", "text": "12345"},
            ],
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

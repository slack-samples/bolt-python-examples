import json

from src.blocks import data_table


def test_example01():
    block = data_table.example01()
    actual = block.to_dict()
    expected = {
        "type": "data_table",
        "caption": "A Fabulous Table",
        "rows": [
            [
                {"type": "raw_text", "text": "Name"},
                {"type": "raw_text", "text": "Department"},
                {"type": "raw_text", "text": "Badge"},
            ],
            [
                {"type": "raw_text", "text": "Data Refinement Department"},
                {"type": "raw_text", "text": "MDR"},
                {
                    "type": "rich_text",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Blue",
                                    "style": {"bold": True},
                                }
                            ],
                        }
                    ],
                },
            ],
            [
                {"type": "raw_text", "text": "Art Sourcing Department"},
                {"type": "raw_text", "text": "O&D"},
                {
                    "type": "rich_text",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {"type": "text", "text": "Green"},
                                {
                                    "type": "text",
                                    "text": "review",
                                    "style": {"italic": True},
                                },
                            ],
                        }
                    ],
                },
            ],
            [
                {"type": "raw_text", "text": "Wellness Department"},
                {"type": "raw_text", "text": "Wellness Center"},
                {
                    "type": "rich_text",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Limited",
                                    "style": {"bold": True},
                                }
                            ],
                        }
                    ],
                },
            ],
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

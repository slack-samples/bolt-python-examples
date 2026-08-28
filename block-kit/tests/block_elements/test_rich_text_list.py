import json

from src.block_elements import rich_text_list


def test_example01():
    block = rich_text_list.example01()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "block_id": "block1",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [
                    {
                        "type": "text",
                        "text": "My favorite Slack features (in no particular order):",
                    },
                ],
            },
            {
                "type": "rich_text_list",
                "style": "bullet",
                "indent": 0,
                "border": 1,
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": "Huddles",
                            },
                        ],
                    },
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": "Canvas",
                            },
                        ],
                    },
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": "Developing with Block Kit",
                            },
                        ],
                    },
                ],
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example02():
    block = rich_text_list.example02()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "block_id": "block1",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [
                    {
                        "type": "text",
                        "text": "Breakfast foods I enjoy:",
                    },
                ],
            },
            {
                "type": "rich_text_list",
                "style": "bullet",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": "Hashbrowns",
                            },
                        ],
                    },
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": "Eggs",
                            },
                        ],
                    },
                ],
            },
            {
                "type": "rich_text_list",
                "style": "bullet",
                "indent": 1,
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": "Scrambled",
                            },
                        ],
                    },
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": "Over easy",
                            },
                        ],
                    },
                ],
            },
            {
                "type": "rich_text_list",
                "style": "bullet",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": "Pancakes, extra syrup",
                            },
                        ],
                    },
                ],
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

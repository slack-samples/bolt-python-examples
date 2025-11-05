import json

from src.blocks import rich_text


def test_example01():
    blocks = rich_text.example01()
    actual = [block.to_dict() for block in blocks]
    expected = [
        {
            "type": "rich_text",
            "elements": [
                {
                    "type": "rich_text_section",
                    "elements": [
                        {
                            "type": "text",
                            "text": "Hello there, I am a basic rich text block!",
                        }
                    ],
                }
            ],
        },
        {
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
                }
            ],
        },
        {
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
                            "text": "I am an italic rich text block!",
                            "style": {
                                "italic": True,
                            },
                        },
                    ],
                }
            ],
        },
        {
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
                            "text": "I am a strikethrough rich text block!",
                            "style": {
                                "strike": True,
                            },
                        },
                    ],
                }
            ],
        },
    ]
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example02():
    block = rich_text.example02()
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
                    }
                ],
            },
            {
                "type": "rich_text_list",
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
                "style": "bullet",
                "indent": 0,
                "border": 1,
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example03():
    block = rich_text.example03()
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
                    }
                ],
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example04():
    block = rich_text.example04()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_preformatted",
                "elements": [
                    {
                        "type": "text",
                        "text": '{\n  "object": {\n    "description": "this is an example of a json object"\n  }\n}',
                    }
                ],
                "border": 0,
            }
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example05():
    block = rich_text.example05()
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
                    }
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


def test_example06():
    block = rich_text.example06()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [{"type": "broadcast", "range": "everyone"}],
            }
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example07():
    block = rich_text.example07()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [{"type": "color", "value": "#F405B3"}],
            }
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example08():
    block = rich_text.example08()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [{"type": "channel", "channel_id": "C123ABC456"}],
            }
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example09():
    block = rich_text.example09()
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
                    }
                ],
            }
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example10():
    block = rich_text.example10()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [
                    {
                        "type": "emoji",
                        "name": "basketball",
                    },
                    {
                        "type": "text",
                        "text": " ",
                    },
                    {
                        "type": "emoji",
                        "name": "snowboarder",
                    },
                    {
                        "type": "text",
                        "text": " ",
                    },
                    {
                        "type": "emoji",
                        "name": "checkered_flag",
                    },
                ],
            }
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example11():
    block = rich_text.example11()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [{"type": "link", "url": "https://api.slack.com"}],
            }
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example12():
    block = rich_text.example12()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [{"type": "user", "user_id": "U123ABC456"}],
            }
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example13():
    block = rich_text.example13()
    actual = block.to_dict()
    expected = {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [{"type": "usergroup", "usergroup_id": "G123ABC456"}],
            }
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

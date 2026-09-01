import json

from src.elements import rich_text_section


def test_example01():
    blocks = rich_text_section.example01()
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
                        },
                    ],
                },
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
                },
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
                },
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
                },
            ],
        },
    ]
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

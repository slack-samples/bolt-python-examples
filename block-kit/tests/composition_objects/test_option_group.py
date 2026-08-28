import json

from src.composition_objects import option_group


def test_example01():
    blocks = option_group.example01()
    actual = [block.to_dict() for block in blocks]
    expected = [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": ":mag: Search results for *Cata*"},
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*<fakeLink.toYourApp.com|Use Case Catalogue>*\nUse Case Catalogue for the following departments/roles...",
            },
            "accessory": {
                "type": "static_select",
                "placeholder": {"type": "plain_text", "emoji": True, "text": "Manage"},
                "option_groups": [
                    {
                        "label": {"type": "plain_text", "text": "Group 1"},
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "*this is plain_text text*",
                                },
                                "value": "value-0",
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "*this is plain_text text*",
                                },
                                "value": "value-1",
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "*this is plain_text text*",
                                },
                                "value": "value-2",
                            },
                        ],
                    },
                    {
                        "label": {"type": "plain_text", "text": "Group 2"},
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "*this is plain_text text*",
                                },
                                "value": "value-3",
                            },
                        ],
                    },
                ],
            },
        },
    ]
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

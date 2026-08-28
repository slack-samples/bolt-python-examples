import json

from src.composition_objects import option


def test_example01():
    obj = option.example01()
    actual = obj.to_dict()
    expected = {
        "text": {"type": "plain_text", "emoji": True, "text": "Save it"},
        "value": "value-2",
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example02():
    blocks = option.example02()
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
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "emoji": True,
                            "text": "Edit it",
                        },
                        "value": "value-0",
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "emoji": True,
                            "text": "Read it",
                        },
                        "value": "value-1",
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "emoji": True,
                            "text": "Save it",
                        },
                        "value": "value-2",
                    },
                ],
            },
        },
    ]
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

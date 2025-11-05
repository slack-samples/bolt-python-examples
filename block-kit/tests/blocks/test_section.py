import json

from src.blocks import section


def test_example01():
    block = section.example01()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "A message *with some bold text* and _some italicized text_.",
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example02():
    block = section.example02()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "text": {
            "text": "A message *with some bold text* and _some italicized text_.",
            "type": "mrkdwn",
        },
        "fields": [
            {
                "type": "mrkdwn",
                "text": "High",
            },
            {
                "type": "plain_text",
                "emoji": True,
                "text": "Silly",
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example03():
    block = section.example03()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "text": {
            "text": "*Haley* has requested you set a deadline for finding a house",
            "type": "mrkdwn",
        },
        "accessory": {
            "type": "datepicker",
            "action_id": "datepicker123",
            "initial_date": "1990-04-28",
            "placeholder": {
                "type": "plain_text",
                "text": "Select a date",
            },
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

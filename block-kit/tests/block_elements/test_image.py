import json

from src.block_elements import image


def test_example01():
    block = image.example01()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "block_id": "section567",
        "text": {
            "type": "mrkdwn",
            "text": "This is a section block with an accessory image.",
        },
        "accessory": {
            "type": "image",
            "image_url": "https://pbs.twimg.com/profile_images/625633822235693056/lNGUneLX_400x400.jpg",
            "alt_text": "cute cat",
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example02():
    block = image.example02()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "block_id": "section567",
        "text": {
            "type": "mrkdwn",
            "text": "This is a section block with an accessory image.",
        },
        "accessory": {
            "type": "image",
            "slack_file": {
                "url": "https://files.slack.com/files-pri/T0123456-F0123456/xyz.png"
            },
            "alt_text": "Slack file object.",
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example03():
    block = image.example03()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "block_id": "section567",
        "text": {
            "type": "mrkdwn",
            "text": "This is a section block with an accessory image.",
        },
        "accessory": {
            "type": "image",
            "slack_file": {"id": "F01234567"},
            "alt_text": "Slack file object.",
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

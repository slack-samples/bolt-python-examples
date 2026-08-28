import json

from src.block_elements import button


def test_example01():
    element = button.example01()
    actual = element.to_dict()
    expected = {
        "type": "button",
        "text": {"type": "plain_text", "text": "Click Me"},
        "value": "click_me_123",
        "action_id": "button",
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example02():
    element = button.example02()
    actual = element.to_dict()
    expected = {
        "type": "button",
        "text": {"type": "plain_text", "text": "Save"},
        "style": "primary",
        "value": "click_me_123",
        "action_id": "button",
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example03():
    element = button.example03()
    actual = element.to_dict()
    expected = {
        "type": "button",
        "text": {"type": "plain_text", "text": "Link Button"},
        "url": "https://docs.slack.dev/block-kit",
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example04():
    blocks = button.example04()
    actual = [block.to_dict() for block in blocks]
    expected = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "This is a section block with a button.",
            },
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Click Me"},
                "value": "click_me_123",
                "action_id": "button",
            },
        },
        {
            "type": "actions",
            "block_id": "actionblock789",
            "elements": [
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Primary Button"},
                    "style": "primary",
                    "value": "click_me_456",
                },
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Link Button"},
                    "url": "https://api.slack.com/block-kit",
                },
            ],
        },
    ]
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

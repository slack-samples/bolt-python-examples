import json

from src.blocks import card


def test_example01():
    block = card.example01()
    actual = block.to_dict()
    expected = {
        "type": "card",
        "icon": {
            "type": "image",
            "image_url": "https://picsum.photos/36/36",
            "alt_text": "Icon",
        },
        "title": {
            "type": "mrkdwn",
            "text": "Lumon Industries",
            "verbatim": False,
        },
        "subtitle": {
            "type": "mrkdwn",
            "text": "Committed to work-life balance",
            "verbatim": False,
        },
        "hero_image": {
            "type": "image",
            "image_url": "https://picsum.photos/400/300",
            "alt_text": "Sample hero image",
        },
        "body": {
            "type": "mrkdwn",
            "text": "Please enjoy each card equally.",
            "verbatim": False,
        },
        "actions": [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Action Button",
                    "emoji": False,
                },
                "action_id": "button_action",
            }
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example02():
    block = card.example02()
    actual = block.to_dict()
    expected = {
        "type": "card",
        "title": {
            "type": "mrkdwn",
            "text": "Pick your refinement number",
        },
        "actions": [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Refine",
                },
                "action_id": "refine_action",
            }
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

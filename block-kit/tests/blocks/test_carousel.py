import json

from src.blocks import carousel


def test_example01():
    block = carousel.example01()
    actual = block.to_dict()
    expected = {
        "type": "carousel",
        "elements": [
            {
                "type": "card",
                "block_id": "carousel-card-1",
                "icon": {
                    "type": "image",
                    "image_url": "https://picsum.photos/36/36",
                    "alt_text": "Icon",
                },
                "title": {"type": "mrkdwn", "text": "MDR"},
                "subtitle": {"type": "mrkdwn", "text": "Refining data files"},
                "hero_image": {
                    "type": "image",
                    "image_url": "https://picsum.photos/400/300",
                    "alt_text": "Sample hero image",
                },
                "body": {
                    "type": "mrkdwn",
                    "text": "Blue badge required to gain access.",
                },
                "actions": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Action Button",
                            "emoji": False,
                        },
                        "action_id": "button_action_1",
                    }
                ],
            },
            {
                "type": "card",
                "block_id": "carousel-card-2",
                "icon": {
                    "type": "image",
                    "image_url": "https://picsum.photos/36/36",
                    "alt_text": "Icon",
                },
                "title": {"type": "mrkdwn", "text": "O&D"},
                "subtitle": {
                    "type": "mrkdwn",
                    "text": "Storage, maintenance, and rotation of art pieces",
                },
                "hero_image": {
                    "type": "image",
                    "image_url": "https://picsum.photos/400/300",
                    "alt_text": "Sample hero image",
                },
                "body": {
                    "type": "mrkdwn",
                    "text": "Green badge required to gain access.",
                },
                "actions": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Action Button",
                            "emoji": False,
                        },
                        "action_id": "button_action_2",
                    }
                ],
            },
            {
                "type": "card",
                "block_id": "carousel-card-3",
                "icon": {
                    "type": "image",
                    "image_url": "https://picsum.photos/36/36",
                    "alt_text": "Icon",
                },
                "title": {"type": "mrkdwn", "text": "Wellness Center"},
                "subtitle": {"type": "mrkdwn", "text": "Wellness sessions"},
                "hero_image": {
                    "type": "image",
                    "image_url": "https://picsum.photos/400/300",
                    "alt_text": "Sample hero image",
                },
                "body": {
                    "type": "mrkdwn",
                    "text": "Please take a seat in the waiting room until called.",
                },
                "actions": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Action Button",
                            "emoji": False,
                        },
                        "action_id": "button_action_3",
                    }
                ],
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

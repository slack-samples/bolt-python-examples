import json

from src.blocks import actions


def test_example01():
    block = actions.example01()
    actual = block.to_dict()
    expected = {
        "type": "actions",
        "block_id": "actions1",
        "elements": [
            {
                "type": "static_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Which witch is the witchiest witch?",
                },
                "action_id": "select_2",
                "options": [
                    {
                        "text": {"type": "plain_text", "text": "Matilda"},
                        "value": "matilda",
                    },
                    {
                        "text": {"type": "plain_text", "text": "Glinda"},
                        "value": "glinda",
                    },
                    {
                        "text": {"type": "plain_text", "text": "Granny Weatherwax"},
                        "value": "grannyWeatherwax",
                    },
                    {
                        "text": {"type": "plain_text", "text": "Hermione"},
                        "value": "hermione",
                    },
                ],
            },
            {
                "type": "button",
                "text": {"type": "plain_text", "text": "Cancel"},
                "value": "cancel",
                "action_id": "button_1",
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example02():
    block = actions.example02()
    actual = block.to_dict()
    expected = {
        "type": "actions",
        "block_id": "actionblock789",
        "elements": [
            {
                "type": "datepicker",
                "action_id": "datepicker123",
                "initial_date": "1990-04-28",
                "placeholder": {"type": "plain_text", "text": "Select a date"},
            },
            {
                "type": "overflow",
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
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "*this is plain_text text*",
                        },
                        "value": "value-3",
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "*this is plain_text text*",
                        },
                        "value": "value-4",
                    },
                ],
                "action_id": "overflow",
            },
            {
                "type": "button",
                "text": {"type": "plain_text", "text": "Click Me"},
                "value": "click_me_123",
                "action_id": "button",
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

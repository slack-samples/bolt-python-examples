import json

from src.elements import select_menu


def test_example01():
    block = select_menu.example01()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "block_id": "section678",
        "text": {
            "type": "mrkdwn",
            "text": "Pick an item from the dropdown list",
        },
        "accessory": {
            "type": "static_select",
            "action_id": "text1234",
            "placeholder": {
                "type": "plain_text",
                "text": "Select an item",
            },
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
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example02():
    block = select_menu.example02()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "block_id": "section678",
        "text": {
            "type": "mrkdwn",
            "text": "Pick an item from the dropdown list",
        },
        "accessory": {
            "type": "external_select",
            "action_id": "text1234",
            "placeholder": {
                "type": "plain_text",
                "text": "Select an item",
            },
            "min_query_length": 3,
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example03():
    block = select_menu.example03()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "block_id": "section678",
        "text": {
            "type": "mrkdwn",
            "text": "Pick a user from the dropdown list",
        },
        "accessory": {
            "type": "users_select",
            "action_id": "text1234",
            "placeholder": {
                "type": "plain_text",
                "text": "Select an item",
            },
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example04():
    block = select_menu.example04()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "block_id": "section678",
        "text": {
            "type": "mrkdwn",
            "text": "Pick a conversation from the dropdown list",
        },
        "accessory": {
            "type": "conversations_select",
            "action_id": "text1234",
            "placeholder": {
                "type": "plain_text",
                "text": "Select an item",
            },
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example05():
    block = select_menu.example05()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "block_id": "section678",
        "text": {
            "type": "mrkdwn",
            "text": "Pick a channel from the dropdown list",
        },
        "accessory": {
            "type": "channels_select",
            "action_id": "text1234",
            "placeholder": {
                "type": "plain_text",
                "text": "Select an item",
            },
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

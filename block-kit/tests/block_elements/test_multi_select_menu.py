import json

from src.block_elements import multi_select_menu


def test_example01():
    block = multi_select_menu.example01()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "block_id": "section678",
        "text": {"type": "mrkdwn", "text": "Pick items from the list"},
        "accessory": {
            "type": "multi_static_select",
            "action_id": "text1234",
            "placeholder": {"type": "plain_text", "text": "Select items"},
            "options": [
                {
                    "text": {"type": "plain_text", "text": "*this is plain_text text*"},
                    "value": "value-0",
                },
                {
                    "text": {"type": "plain_text", "text": "*this is plain_text text*"},
                    "value": "value-1",
                },
                {
                    "text": {"type": "plain_text", "text": "*this is plain_text text*"},
                    "value": "value-2",
                },
            ],
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example02():
    block = multi_select_menu.example02()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "block_id": "section678",
        "text": {"type": "mrkdwn", "text": "Pick items from the list"},
        "accessory": {
            "type": "multi_external_select",
            "action_id": "text1234",
            "placeholder": {"type": "plain_text", "text": "Select items"},
            "min_query_length": 3,
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example03():
    block = multi_select_menu.example03()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "block_id": "section678",
        "text": {"type": "mrkdwn", "text": "Pick users from the list"},
        "accessory": {
            "type": "multi_users_select",
            "action_id": "text1234",
            "placeholder": {"type": "plain_text", "text": "Select users"},
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example04():
    block = multi_select_menu.example04()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "block_id": "section678",
        "text": {"type": "mrkdwn", "text": "Pick conversations from the list"},
        "accessory": {
            "type": "multi_conversations_select",
            "action_id": "text1234",
            "placeholder": {"type": "plain_text", "text": "Select conversations"},
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example05():
    block = multi_select_menu.example05()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "block_id": "section678",
        "text": {"type": "mrkdwn", "text": "Pick channels from the list"},
        "accessory": {
            "type": "multi_channels_select",
            "action_id": "text1234",
            "placeholder": {"type": "plain_text", "text": "Select channels"},
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

import json

from src.block_elements import icon_button


def test_example01():
    block = icon_button.example01()
    actual = block.to_dict()
    expected = {
        "type": "context_actions",
        "elements": [
            {
                "type": "icon_button",
                "icon": "trash",
                "text": {
                    "type": "plain_text",
                    "text": "Delete",
                },
                "action_id": "delete_button",
                "value": "delete_item",
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

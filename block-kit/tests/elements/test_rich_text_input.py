import json

from src.elements import rich_text_input


def test_example01():
    view = rich_text_input.example01()
    actual = view.to_dict()
    expected = {
        "type": "home",
        "blocks": [
            {
                "type": "input",
                "label": {
                    "type": "plain_text",
                    "text": "Label",
                    "emoji": True,
                },
                "element": {
                    "type": "rich_text_input",
                    "action_id": "rich_text_input-action",
                    "dispatch_action_config": {
                        "trigger_actions_on": [
                            "on_character_entered",
                        ],
                    },
                    "focus_on_load": True,
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Enter text",
                    },
                },
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

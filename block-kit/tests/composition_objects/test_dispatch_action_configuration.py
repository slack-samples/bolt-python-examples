import json

from src.composition_objects import dispatch_action_configuration


def test_example01():
    block = dispatch_action_configuration.example01()
    actual = block.to_dict()
    expected = {
        "type": "input",
        "dispatch_action": True,
        "element": {
            "type": "plain_text_input",
            "multiline": True,
            "dispatch_action_config": {
                "trigger_actions_on": ["on_character_entered"],
            },
        },
        "label": {
            "type": "plain_text",
            "text": "This is a multiline plain-text input",
            "emoji": True,
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

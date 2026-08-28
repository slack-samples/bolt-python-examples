import json

from src.block_elements import email_input


def test_example01():
    block = email_input.example01()
    actual = block.to_dict()
    expected = {
        "type": "input",
        "block_id": "input123",
        "label": {"type": "plain_text", "text": "Email Address"},
        "element": {
            "type": "email_text_input",
            "action_id": "email_text_input-action",
            "placeholder": {"type": "plain_text", "text": "Enter an email"},
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

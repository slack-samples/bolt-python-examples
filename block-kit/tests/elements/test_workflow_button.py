import json

from src.elements import workflow_button


def test_example01():
    block = workflow_button.example01()
    actual = block.to_dict()
    expected = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "A message *with some bold text* and _some italicized text_.",
        },
        "accessory": {
            "type": "workflow_button",
            "text": {
                "type": "plain_text",
                "text": "Run Workflow",
            },
            "action_id": "workflowbutton123",
            "workflow": {
                "trigger": {
                    "url": "https://slack.com/shortcuts/Ft0123ABC456/xyz...zyx",
                    "customizable_input_parameters": [
                        {
                            "name": "input_parameter_a",
                            "value": "Value for input param A",
                        },
                        {
                            "name": "input_parameter_b",
                            "value": "Value for input param B",
                        },
                    ],
                },
            },
        },
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

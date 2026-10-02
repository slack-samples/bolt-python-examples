import json

from src.elements import file_input


def test_example01():
    view = file_input.example01()
    actual = view.to_dict()
    expected = {
        "type": "modal",
        "title": {
            "type": "plain_text",
            "text": "My App",
            "emoji": True,
        },
        "submit": {
            "type": "plain_text",
            "text": "Submit",
            "emoji": True,
        },
        "close": {
            "type": "plain_text",
            "text": "Cancel",
            "emoji": True,
        },
        "blocks": [
            {
                "type": "input",
                "block_id": "input_block_id",
                "label": {
                    "type": "plain_text",
                    "text": "Upload Files",
                },
                "element": {
                    "type": "file_input",
                    "action_id": "file_input_action_id_1",
                    "filetypes": [
                        "jpg",
                        "png",
                    ],
                    "max_files": 5,
                },
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

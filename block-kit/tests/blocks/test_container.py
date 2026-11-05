import json

from src.blocks import container


def test_example01():
    block = container.example01()
    actual = block.to_dict()
    expected = {
        "type": "container",
        "block_id": "bkb_container_bulk_update",
        "title": {
            "type": "plain_text",
            "text": "Bulk update: 2 records selected",
        },
        "subtitle": {
            "type": "plain_text",
            "text": "Review changes before confirming",
        },
        "is_collapsible": True,
        "child_blocks": [
            {
                "type": "section",
                "block_id": "record-row-1",
                "text": {
                    "type": "mrkdwn",
                    "text": "*DCW-1024*\nStatus: Open → Closed\nAssignee: @princessdonut → @carl",
                },
            },
            {
                "type": "divider",
                "block_id": "bulk-div-1",
            },
            {
                "type": "section",
                "block_id": "record-row-2",
                "text": {
                    "type": "mrkdwn",
                    "text": "*DCW-1025*\nStatus: In Progress → Closed\nAssignee: @mordecai → @carl",
                },
            },
            {
                "type": "divider",
                "block_id": "bulk-div-2",
            },
            {
                "type": "context",
                "block_id": "bulk-status-bar",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": ":white_check_mark: 2 records will be updated • Status → Closed • Assignee → @carl",
                    },
                ],
            },
            {
                "type": "actions",
                "block_id": "bulk-actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Confirm All",
                            "emoji": True,
                        },
                        "style": "primary",
                        "action_id": "bulk_confirm",
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Cancel",
                            "emoji": True,
                        },
                        "action_id": "bulk_cancel",
                    },
                ],
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

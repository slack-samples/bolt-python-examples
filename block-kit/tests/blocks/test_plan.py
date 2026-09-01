import json

from src.blocks import plan


def test_example01():
    block = plan.example01()
    actual = block.to_dict()
    expected = {
        "type": "plan",
        "title": "Thinking completed",
        "tasks": [
            {
                "type": "task_card",
                "task_id": "call_001",
                "title": "Fetched user profile information",
                "status": "in_progress",
                "details": {
                    "type": "rich_text",
                    "block_id": "viMWO",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Searched database...",
                                }
                            ],
                        }
                    ],
                },
                "output": {
                    "type": "rich_text",
                    "block_id": "viMWO",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Profile data loaded",
                                }
                            ],
                        }
                    ],
                },
            },
            {
                "type": "task_card",
                "task_id": "call_002",
                "title": "Checked user permissions",
                "status": "pending",
            },
            {
                "type": "task_card",
                "task_id": "call_003",
                "title": "Generated comprehensive user report",
                "status": "complete",
                "output": {
                    "type": "rich_text",
                    "block_id": "crsk",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "15 data points compiled",
                                }
                            ],
                        }
                    ],
                },
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

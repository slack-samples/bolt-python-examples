import json

from src.elements import url_source


def test_example01():
    element = url_source.example01()
    actual = element.to_dict()
    expected = {
        "type": "url",
        "url": "https://docs.slack.dev/",
        "text": "Slack API docs",
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example02():
    block = url_source.example02()
    actual = block.to_dict()
    expected = {
        "type": "task_card",
        "task_id": "task_1",
        "title": "Scientific findings",
        "status": "complete",
        "sources": [
            {
                "type": "url",
                "url": "https://docs.example.com/",
                "text": "Tracy's delightful docs",
            },
            {
                "type": "url",
                "url": "https://research.example.com/",
                "text": "Haley's resourceful research",
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

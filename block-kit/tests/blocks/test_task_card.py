import json

from src.blocks import task_card


def test_example01():
    block = task_card.example01()
    actual = block.to_dict()
    expected = {
        "type": "task_card",
        "task_id": "task_1",
        "title": "Fetching weather data",
        "status": "pending",
        "output": {
            "type": "rich_text",
            "elements": [
                {
                    "type": "rich_text_section",
                    "elements": [
                        {
                            "type": "text",
                            "text": "Found weather data for Chicago from 2 sources",
                        }
                    ],
                }
            ],
        },
        "sources": [
            {
                "type": "url",
                "url": "https://weather.com/",
                "text": "weather.com",
            },
            {
                "type": "url",
                "url": "https://www.accuweather.com/",
                "text": "accuweather.com",
            },
        ],
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

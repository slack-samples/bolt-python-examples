import json

from src.blocks import video


def test_example01():
    block = video.example01()
    actual = block.to_dict()
    expected = {
        "type": "video",
        "title": {
            "type": "plain_text",
            "text": "Use the Events API to create a dynamic App Home",
            "emoji": True,
        },
        "title_url": "https://www.youtube.com/watch?v=8876OZV_Yy0",
        "description": {
            "type": "plain_text",
            "text": "Slack sure is nifty!",
            "emoji": True,
        },
        "video_url": "https://www.youtube.com/embed/8876OZV_Yy0?feature=oembed&autoplay=1",
        "alt_text": "Use the Events API to create a dynamic App Home",
        "thumbnail_url": "https://i.ytimg.com/vi/8876OZV_Yy0/hqdefault.jpg",
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

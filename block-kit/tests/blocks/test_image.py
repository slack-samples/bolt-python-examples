import json

from src.blocks import image


def test_example01():
    block = image.example01()
    actual = block.to_dict()
    expected = {
        "type": "image",
        "title": {
            "type": "plain_text",
            "text": "Please enjoy this photo of a kitten",
        },
        "block_id": "image4",
        "image_url": "http://placekitten.com/500/500",
        "alt_text": "An incredibly cute kitten.",
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example02():
    block = image.example02()
    actual = block.to_dict()
    expected = {
        "type": "image",
        "title": {
            "type": "plain_text",
            "text": "Please enjoy this photo of a kitten",
        },
        "block_id": "image4",
        "slack_file": {
            "url": "https://files.slack.com/files-pri/T0123456-F0123456/xyz.png",
        },
        "alt_text": "An incredibly cute kitten.",
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)


def test_example03():
    block = image.example03()
    actual = block.to_dict()
    expected = {
        "type": "image",
        "title": {
            "type": "plain_text",
            "text": "Please enjoy this photo of a kitten",
        },
        "block_id": "image4",
        "slack_file": {
            "id": "F0123456",
        },
        "alt_text": "An incredibly cute kitten.",
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)

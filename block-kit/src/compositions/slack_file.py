from slack_sdk.models.blocks import ImageBlock
from slack_sdk.models.blocks.basic_components import PlainTextObject, SlackFile


def example01() -> ImageBlock:
    """
    Defines an object containing Slack file information to be used in an image block or image element.
    https://docs.slack.dev/reference/block-kit/composition-objects/slack-file-object/

    An image block using slack_file with a url.
    """
    block = ImageBlock(
        title=PlainTextObject(text="Please enjoy this photo of a kitten"),
        block_id="image4",
        slack_file=SlackFile(
            url="https://files.slack.com/files-pri/T0123456-F0123456/xyz.png"
        ),
        alt_text="An incredibly cute kitten.",
    )
    return block


def example02() -> ImageBlock:
    """
    An image block using slack_file with an id.
    """
    block = ImageBlock(
        title=PlainTextObject(text="Please enjoy this photo of a kitten"),
        block_id="image4",
        slack_file=SlackFile(id="F0123456"),
        alt_text="An incredibly cute kitten.",
    )
    return block

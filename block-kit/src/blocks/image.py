from slack_sdk.models.blocks import ImageBlock
from slack_sdk.models.blocks.basic_components import PlainTextObject, SlackFile


def example01() -> ImageBlock:
    """
    Displays an image.
    https://docs.slack.dev/reference/block-kit/blocks/image-block/

    An image block using image_url.
    """
    block = ImageBlock(
        title=PlainTextObject(text="Please enjoy this photo of a kitten"),
        block_id="image4",
        image_url="http://placekitten.com/500/500",
        alt_text="An incredibly cute kitten.",
    )
    return block


def example02() -> ImageBlock:
    """
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


def example03() -> ImageBlock:
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

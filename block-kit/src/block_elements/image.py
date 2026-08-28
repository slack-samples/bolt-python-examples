from slack_sdk.models.blocks import SectionBlock
from slack_sdk.models.blocks.basic_components import (
    MarkdownTextObject,
    SlackFile,
)
from slack_sdk.models.blocks.block_elements import ImageElement


def example01() -> SectionBlock:
    """
    Displays an image as part of a larger block of content.
    https://docs.slack.dev/reference/block-kit/block-elements/image-element/

    A section block with an accessory image referenced by URL.
    """
    block = SectionBlock(
        block_id="section567",
        text=MarkdownTextObject(
            text="This is a section block with an accessory image."
        ),
        accessory=ImageElement(
            image_url="https://pbs.twimg.com/profile_images/625633822235693056/lNGUneLX_400x400.jpg",
            alt_text="cute cat",
        ),
    )
    return block


def example02() -> SectionBlock:
    """
    A section block with an accessory image referenced by a Slack file URL.
    """
    block = SectionBlock(
        block_id="section567",
        text=MarkdownTextObject(
            text="This is a section block with an accessory image."
        ),
        accessory=ImageElement(
            slack_file=SlackFile(
                url="https://files.slack.com/files-pri/T0123456-F0123456/xyz.png"
            ),
            alt_text="Slack file object.",
        ),
    )
    return block


def example03() -> SectionBlock:
    """
    A section block with an accessory image referenced by a Slack file ID.
    """
    block = SectionBlock(
        block_id="section567",
        text=MarkdownTextObject(
            text="This is a section block with an accessory image."
        ),
        accessory=ImageElement(
            slack_file=SlackFile(id="F01234567"),
            alt_text="Slack file object.",
        ),
    )
    return block

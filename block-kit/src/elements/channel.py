from slack_sdk.models.blocks import RichTextBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextSectionElement,
)


def example01() -> RichTextBlock:
    """
    Renders as a mention of a channel.
    https://docs.slack.dev/reference/block-kit/block-elements/channel-element/

    A rich text block with a channel mention in a section.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.Channel(channel_id="C123ABC456"),
                ]
            )
        ]
    )
    return block

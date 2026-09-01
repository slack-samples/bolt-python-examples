from slack_sdk.models.blocks import RichTextBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextSectionElement,
)


def example01() -> RichTextBlock:
    """
    Displays a broadcast mention such as here, channel, or everyone.
    https://docs.slack.dev/reference/block-kit/block-elements/broadcast-element/

    A rich text block with a broadcast mention in a section.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.Broadcast(range="everyone"),
                ]
            )
        ]
    )
    return block

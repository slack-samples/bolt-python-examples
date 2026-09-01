from slack_sdk.models.blocks import RichTextBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextSectionElement,
)


def example01() -> RichTextBlock:
    """
    Displays a color swatch from a hex value.
    https://docs.slack.dev/reference/block-kit/block-elements/color-element/

    A rich text block with a color element in a section.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.Color(value="#F405B3"),
                ]
            )
        ]
    )
    return block

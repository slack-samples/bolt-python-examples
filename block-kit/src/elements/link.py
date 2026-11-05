from slack_sdk.models.blocks import RichTextBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextSectionElement,
)


def example01() -> RichTextBlock:
    """
    Displays a hyperlink.
    https://docs.slack.dev/reference/block-kit/block-elements/link-element/

    A rich text block with a link element in a section.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.Link(url="https://docs.slack.dev"),
                ]
            )
        ]
    )
    return block

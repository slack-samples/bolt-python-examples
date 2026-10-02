from slack_sdk.models.blocks import RichTextBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextSectionElement,
)


def example01() -> RichTextBlock:
    """
    Displays text, optionally with styling.
    https://docs.slack.dev/reference/block-kit/block-elements/text-element/

    A rich text block with plain and bold text elements in a section.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.Text(text="Hello there, "),
                    RichTextElementParts.Text(
                        text="I am a bold rich text block!",
                        style=RichTextElementParts.TextStyle(bold=True),
                    ),
                ]
            )
        ]
    )
    return block

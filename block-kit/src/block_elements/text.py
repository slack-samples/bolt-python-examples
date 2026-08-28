from slack_sdk.models.blocks import RichTextBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextSectionElement,
)


def example01() -> RichTextBlock:
    """
    Displays text, optionally with styling.
    https://docs.slack.dev/reference/block-kit/block-elements/text-element/

    A rich text block whose section holds plain and bold-styled text elements.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.Text(text="Hello there, "),
                    RichTextElementParts.Text(
                        text="I am a bold rich text block!",
                        style={"bold": True},
                    ),
                ]
            )
        ]
    )
    return block

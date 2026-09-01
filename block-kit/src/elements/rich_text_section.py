from slack_sdk.models.blocks import RichTextBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextSectionElement,
)


def example01() -> list[RichTextBlock]:
    """
    A section element that holds rich text elements.
    https://docs.slack.dev/reference/block-kit/block-elements/rich-text-section-element/

    Rich text blocks showing basic, bold, italic, and strikethrough text sections.
    """
    blocks = [
        RichTextBlock(
            elements=[
                RichTextSectionElement(
                    elements=[
                        RichTextElementParts.Text(
                            text="Hello there, I am a basic rich text block!"
                        ),
                    ]
                )
            ]
        ),
        RichTextBlock(
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
        ),
        RichTextBlock(
            elements=[
                RichTextSectionElement(
                    elements=[
                        RichTextElementParts.Text(text="Hello there, "),
                        RichTextElementParts.Text(
                            text="I am an italic rich text block!",
                            style={"italic": True},
                        ),
                    ]
                )
            ]
        ),
        RichTextBlock(
            elements=[
                RichTextSectionElement(
                    elements=[
                        RichTextElementParts.Text(text="Hello there, "),
                        RichTextElementParts.Text(
                            text="I am a strikethrough rich text block!",
                            style={"strike": True},
                        ),
                    ]
                )
            ]
        ),
    ]
    return blocks

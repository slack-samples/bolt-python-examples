from slack_sdk.models.blocks import RichTextBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextSectionElement,
)


def example01() -> RichTextBlock:
    """
    Displays an emoji.
    https://docs.slack.dev/reference/block-kit/block-elements/emoji-element/

    A rich text block with emoji elements in a section.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.Emoji(name="basketball"),
                    RichTextElementParts.Text(text=" "),
                    RichTextElementParts.Emoji(name="snowboarder"),
                    RichTextElementParts.Text(text=" "),
                    RichTextElementParts.Emoji(name="checkered_flag"),
                ]
            )
        ]
    )
    return block

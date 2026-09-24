from slack_sdk.models.blocks import RichTextBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextSectionElement,
)


def example01() -> RichTextBlock:
    """
    Displays a formatted, localized date.
    https://docs.slack.dev/reference/block-kit/block-elements/date-element/

    A rich text block with a date element in a section.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.Date(
                        timestamp=1720710212,
                        format="{date_num} at {time}",
                        fallback="timey",
                    ),
                ]
            )
        ]
    )
    return block

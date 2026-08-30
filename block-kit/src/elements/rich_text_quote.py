from slack_sdk.models.blocks import RichTextBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextQuoteElement,
    RichTextSectionElement,
)


def example01() -> RichTextBlock:
    """
    Displays a rich text quote block.
    https://docs.slack.dev/reference/block-kit/block-elements/rich-text-quote-element/

    A rich text block with a quote followed by a section.
    """
    block = RichTextBlock(
        block_id="Vrzsu",
        elements=[
            RichTextQuoteElement(
                elements=[
                    RichTextElementParts.Text(
                        text="What we need is good examples in our documentation."
                    ),
                ]
            ),
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.Text(text="Yes - I completely agree, Luke!"),
                ]
            ),
        ],
    )
    return block

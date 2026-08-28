from slack_sdk.models.blocks import RichTextBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextSectionElement,
)


def example01() -> RichTextBlock:
    """
    Renders as a rich app attachment or entity reference.
    https://docs.slack.dev/reference/block-kit/block-elements/attachment-mention-element/

    An attachment mention referencing an app attachment by URL.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.AttachmentMention(
                        url="https://example.com/attachment"
                    )
                ]
            )
        ]
    )
    return block

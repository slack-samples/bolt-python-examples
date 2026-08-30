from slack_sdk.models.blocks import RichTextBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextSectionElement,
)


def example01() -> RichTextBlock:
    """
    Renders as a mention of a user.
    https://docs.slack.dev/reference/block-kit/block-elements/user-element/

    A rich text block whose section holds a user mention element.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.User(user_id="U123ABC456"),
                ]
            )
        ]
    )
    return block

from slack_sdk.models.blocks import RichTextBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextSectionElement,
)


def example01() -> RichTextBlock:
    """
    Renders as a mention of a user group.
    https://docs.slack.dev/reference/block-kit/block-elements/usergroup-element/

    A rich text block with a user group mention in a section.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.UserGroup(usergroup_id="G123ABC456"),
                ]
            )
        ]
    )
    return block

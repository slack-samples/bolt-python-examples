from slack_sdk.models.blocks import SectionBlock
from slack_sdk.models.blocks.basic_components import (
    MarkdownTextObject,
    Option,
    PlainTextObject,
)
from slack_sdk.models.blocks.block_elements import OverflowMenuElement


def example01() -> SectionBlock:
    """
    Allows users to press a button to view a list of options.
    https://docs.slack.dev/reference/block-kit/block-elements/overflow-menu-element/

    A section block with an overflow menu as an accessory.
    """
    block = SectionBlock(
        block_id="section 890",
        text=MarkdownTextObject(text="This is a section block with an overflow menu."),
        accessory=OverflowMenuElement(
            action_id="overflow",
            options=[
                Option(
                    text=PlainTextObject(text="*this is plain_text text*"),
                    value="value-0",
                ),
                Option(
                    text=PlainTextObject(text="*this is plain_text text*"),
                    value="value-1",
                ),
                Option(
                    text=PlainTextObject(text="*this is plain_text text*"),
                    value="value-2",
                ),
                Option(
                    text=PlainTextObject(text="*this is plain_text text*"),
                    value="value-3",
                ),
                Option(
                    text=PlainTextObject(text="*this is plain_text text*"),
                    value="value-4",
                ),
            ],
        ),
    )
    return block

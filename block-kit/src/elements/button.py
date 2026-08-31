from slack_sdk.models.blocks import ActionsBlock, Block, SectionBlock
from slack_sdk.models.blocks.basic_components import MarkdownTextObject, PlainTextObject
from slack_sdk.models.blocks.block_elements import ButtonElement


def example01() -> ButtonElement:
    """
    Allows users a direct path to performing basic actions.
    https://docs.slack.dev/reference/block-kit/block-elements/button-element/

    A regular interactive button.
    """
    element = ButtonElement(
        text=PlainTextObject(text="Click Me"),
        value="click_me_123",
        action_id="button",
    )
    return element


def example02() -> ButtonElement:
    """
    A button with a primary style attribute.
    """
    element = ButtonElement(
        text=PlainTextObject(text="Save"),
        style="primary",
        value="click_me_123",
        action_id="button",
    )
    return element


def example03() -> ButtonElement:
    """
    A link button.
    """
    element = ButtonElement(
        text=PlainTextObject(text="Link Button"),
        url="https://docs.slack.dev/block-kit",
    )
    return element


def example05() -> list[Block]:
    """
    The button element must be used inside either the section or actions block.

    A section block with a button as an accessory, followed by an actions
    block holding a primary button and a link button.
    """
    blocks: list[Block] = [
        SectionBlock(
            text=MarkdownTextObject(text="This is a section block with a button."),
            accessory=ButtonElement(
                text=PlainTextObject(text="Click Me"),
                value="click_me_123",
                action_id="button",
            ),
        ),
        ActionsBlock(
            block_id="actionblock789",
            elements=[
                ButtonElement(
                    text=PlainTextObject(text="Primary Button"),
                    style="primary",
                    value="click_me_456",
                ),
                ButtonElement(
                    text=PlainTextObject(text="Link Button"),
                    url="https://api.slack.com/block-kit",
                ),
            ],
        ),
    ]
    return blocks

from slack_sdk.models.blocks import SectionBlock
from slack_sdk.models.blocks.basic_components import (
    MarkdownTextObject,
    Option,
    PlainTextObject,
)
from slack_sdk.models.blocks.block_elements import (
    ChannelSelectElement,
    ConversationSelectElement,
    ExternalDataSelectElement,
    StaticSelectElement,
    UserSelectElement,
)


def example01() -> SectionBlock:
    """
    Allows users to choose an option from a drop down menu.
    https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element/

    A section block with a static select menu as an accessory.
    """
    block = SectionBlock(
        block_id="section678",
        text=MarkdownTextObject(text="Pick an item from the dropdown list"),
        accessory=StaticSelectElement(
            action_id="text1234",
            placeholder=PlainTextObject(text="Select an item"),
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
            ],
        ),
    )
    return block


def example02() -> SectionBlock:
    """
    A section block with an external data source select menu as an accessory.
    """
    block = SectionBlock(
        block_id="section678",
        text=MarkdownTextObject(text="Pick an item from the dropdown list"),
        accessory=ExternalDataSelectElement(
            action_id="text1234",
            placeholder=PlainTextObject(text="Select an item"),
            min_query_length=3,
        ),
    )
    return block


def example03() -> SectionBlock:
    """
    A section block with a user list select menu as an accessory.
    """
    block = SectionBlock(
        block_id="section678",
        text=MarkdownTextObject(text="Pick a user from the dropdown list"),
        accessory=UserSelectElement(
            action_id="text1234",
            placeholder=PlainTextObject(text="Select an item"),
        ),
    )
    return block


def example04() -> SectionBlock:
    """
    A section block with a conversations list select menu as an accessory.
    """
    block = SectionBlock(
        block_id="section678",
        text=MarkdownTextObject(text="Pick a conversation from the dropdown list"),
        accessory=ConversationSelectElement(
            action_id="text1234",
            placeholder=PlainTextObject(text="Select an item"),
        ),
    )
    return block


def example05() -> SectionBlock:
    """
    A section block with a channels list select menu as an accessory.
    """
    block = SectionBlock(
        block_id="section678",
        text=MarkdownTextObject(text="Pick a channel from the dropdown list"),
        accessory=ChannelSelectElement(
            action_id="text1234",
            placeholder=PlainTextObject(text="Select an item"),
        ),
    )
    return block

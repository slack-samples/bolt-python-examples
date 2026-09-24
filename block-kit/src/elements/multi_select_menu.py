from slack_sdk.models.blocks import SectionBlock
from slack_sdk.models.blocks.basic_components import (
    MarkdownTextObject,
    Option,
    PlainTextObject,
)
from slack_sdk.models.blocks.block_elements import (
    ChannelMultiSelectElement,
    ConversationMultiSelectElement,
    ExternalDataMultiSelectElement,
    StaticMultiSelectElement,
    UserMultiSelectElement,
)


def example01() -> SectionBlock:
    """
    Allows users to select multiple items from a list of options.
    https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element/

    A section block containing a static multi-select menu.
    """
    block = SectionBlock(
        block_id="section678",
        text=MarkdownTextObject(text="Pick items from the list"),
        accessory=StaticMultiSelectElement(
            action_id="text1234",
            placeholder=PlainTextObject(text="Select items"),
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
    A multi-select menu in a section block with an external data source.
    """
    block = SectionBlock(
        block_id="section678",
        text=MarkdownTextObject(text="Pick items from the list"),
        accessory=ExternalDataMultiSelectElement(
            action_id="text1234",
            placeholder=PlainTextObject(text="Select items"),
            min_query_length=3,
        ),
    )
    return block


def example03() -> SectionBlock:
    """
    A multi-select menu in a section block showing a list of users.
    """
    block = SectionBlock(
        block_id="section678",
        text=MarkdownTextObject(text="Pick users from the list"),
        accessory=UserMultiSelectElement(
            action_id="text1234",
            placeholder=PlainTextObject(text="Select users"),
        ),
    )
    return block


def example04() -> SectionBlock:
    """
    A multi-select menu in a section block showing a list of conversations.
    """
    block = SectionBlock(
        block_id="section678",
        text=MarkdownTextObject(text="Pick conversations from the list"),
        accessory=ConversationMultiSelectElement(
            action_id="text1234",
            placeholder=PlainTextObject(text="Select conversations"),
        ),
    )
    return block


def example05() -> SectionBlock:
    """
    A multi-select menu in a section block showing a list of channels.
    """
    block = SectionBlock(
        block_id="section678",
        text=MarkdownTextObject(text="Pick channels from the list"),
        accessory=ChannelMultiSelectElement(
            action_id="text1234",
            placeholder=PlainTextObject(text="Select channels"),
        ),
    )
    return block

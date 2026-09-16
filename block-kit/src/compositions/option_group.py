from slack_sdk.models.blocks import Block, DividerBlock, SectionBlock
from slack_sdk.models.blocks.basic_components import (
    MarkdownTextObject,
    Option,
    OptionGroup,
    PlainTextObject,
)
from slack_sdk.models.blocks.block_elements import StaticSelectElement


def example01() -> list[Block]:
    """
    Defines a way to group options in a menu.
    https://docs.slack.dev/reference/block-kit/composition-objects/option-group-object/

    A static select menu containing the option group object.
    """
    blocks: list[Block] = [
        SectionBlock(
            text=MarkdownTextObject(text=":mag: Search results for *Cata*"),
        ),
        DividerBlock(),
        SectionBlock(
            text=MarkdownTextObject(
                text="*<fakeLink.toYourApp.com|Use Case Catalogue>*\nUse Case Catalogue for the following departments/roles..."
            ),
            accessory=StaticSelectElement(
                placeholder=PlainTextObject(text="Manage", emoji=True),
                option_groups=[
                    OptionGroup(
                        label=PlainTextObject(text="Group 1"),
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
                    OptionGroup(
                        label=PlainTextObject(text="Group 2"),
                        options=[
                            Option(
                                text=PlainTextObject(text="*this is plain_text text*"),
                                value="value-3",
                            ),
                        ],
                    ),
                ],
            ),
        ),
    ]
    return blocks

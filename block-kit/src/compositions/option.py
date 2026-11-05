from slack_sdk.models.blocks import Block, DividerBlock, SectionBlock
from slack_sdk.models.blocks.basic_components import (
    MarkdownTextObject,
    Option,
    PlainTextObject,
)
from slack_sdk.models.blocks.block_elements import StaticSelectElement


def example01() -> Option:
    """
    Defines a single item in a number of item selection elements.
    https://docs.slack.dev/reference/block-kit/composition-objects/option-object/

    A single option object.
    """
    option = Option(
        text=PlainTextObject(text="Save it", emoji=True),
        value="value-2",
    )
    return option


def example02() -> list[Block]:
    """
    A static select menu element with several option objects.
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
                options=[
                    Option(
                        text=PlainTextObject(text="Edit it", emoji=True),
                        value="value-0",
                    ),
                    Option(
                        text=PlainTextObject(text="Read it", emoji=True),
                        value="value-1",
                    ),
                    Option(
                        text=PlainTextObject(text="Save it", emoji=True),
                        value="value-2",
                    ),
                ],
            ),
        ),
    ]
    return blocks

from slack_sdk.models.blocks import SectionBlock
from slack_sdk.models.blocks.basic_components import MarkdownTextObject, PlainTextObject
from slack_sdk.models.blocks.block_elements import DatePickerElement


def example01() -> SectionBlock:
    """
    Displays text, possibly alongside elements.
    https://docs.slack.dev/reference/block-kit/blocks/section-block/

    A text section block.
    """
    block = SectionBlock(
        text=MarkdownTextObject(
            text="A message *with some bold text* and _some italicized text_."
        )
    )
    return block


def example02() -> SectionBlock:
    """
    A section block containing text fields.
    """
    block = SectionBlock(
        text=MarkdownTextObject(
            text="A message *with some bold text* and _some italicized text_."
        ),
        fields=[
            MarkdownTextObject(text="High"),
            PlainTextObject(text="Silly", emoji=True),
        ],
    )
    return block


def example03() -> SectionBlock:
    """
    A section block containing a datepicker element.
    """
    block = SectionBlock(
        text=MarkdownTextObject(
            text="*Haley* has requested you set a deadline for finding a house"
        ),
        accessory=DatePickerElement(
            action_id="datepicker123",
            initial_date="1990-04-28",
            placeholder=PlainTextObject(text="Select a date"),
        ),
    )
    return block

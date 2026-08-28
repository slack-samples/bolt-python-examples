from slack_sdk.models.blocks import SectionBlock
from slack_sdk.models.blocks.basic_components import MarkdownTextObject, PlainTextObject
from slack_sdk.models.blocks.block_elements import DatePickerElement


def example01() -> SectionBlock:
    """
    Allows users to select a date from a calendar style UI.
    https://docs.slack.dev/reference/block-kit/block-elements/date-picker-element/

    A section block with a date picker as an accessory.
    """
    block = SectionBlock(
        block_id="section1234",
        text=MarkdownTextObject(text="Pick a date for the deadline."),
        accessory=DatePickerElement(
            action_id="datepicker123",
            initial_date="1990-04-28",
            placeholder=PlainTextObject(text="Select a date"),
        ),
    )
    return block

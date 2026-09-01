from slack_sdk.models.blocks import SectionBlock
from slack_sdk.models.blocks.basic_components import MarkdownTextObject, PlainTextObject
from slack_sdk.models.blocks.block_elements import TimePickerElement


def example01() -> SectionBlock:
    """
    Allows users to enter numerical data into a single-line field.
    https://docs.slack.dev/reference/block-kit/block-elements/time-picker-element/

    A section block with a time picker accessory.
    """
    block = SectionBlock(
        block_id="section1234",
        text=MarkdownTextObject(text="Pick a date for the deadline."),
        accessory=TimePickerElement(
            timezone="America/Los_Angeles",
            action_id="timepicker123",
            initial_time="11:40",
            placeholder=PlainTextObject(text="Select a time"),
        ),
    )
    return block

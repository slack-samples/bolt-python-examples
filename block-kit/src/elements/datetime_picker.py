from slack_sdk.models.blocks import InputBlock
from slack_sdk.models.blocks.basic_components import PlainTextObject
from slack_sdk.models.blocks.block_elements import DateTimePickerElement


def example01() -> InputBlock:
    """
    Allows users to select both a date and a time of day.
    https://docs.slack.dev/reference/block-kit/block-elements/datetime-picker-element/

    An input block with a datetime picker element.
    """
    block = InputBlock(
        element=DateTimePickerElement(action_id="datetimepicker-action"),
        hint=PlainTextObject(text="This is some hint text", emoji=True),
        label=PlainTextObject(text="Start date", emoji=True),
    )
    return block

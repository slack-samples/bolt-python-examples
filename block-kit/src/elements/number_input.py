from slack_sdk.models.blocks import InputBlock
from slack_sdk.models.blocks.basic_components import PlainTextObject
from slack_sdk.models.blocks.block_elements import NumberInputElement


def example01() -> InputBlock:
    """
    Allows user to enter a number into a single-line field.
    https://docs.slack.dev/reference/block-kit/block-elements/number-input-element/

    An input block with a number input element.
    """
    block = InputBlock(
        element=NumberInputElement(
            is_decimal_allowed=False,
            action_id="number_input-action",
        ),
        label=PlainTextObject(text="Label", emoji=True),
    )
    return block

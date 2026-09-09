from slack_sdk.models.blocks import InputBlock
from slack_sdk.models.blocks.basic_components import PlainTextObject
from slack_sdk.models.blocks.block_elements import PlainTextInputElement


def example01() -> InputBlock:
    """
    Allows users to enter freeform text data into a single-line or multi-line field.
    https://docs.slack.dev/reference/block-kit/block-elements/plain-text-input-element/

    An input block with a plain-text input element.
    """
    block = InputBlock(
        element=PlainTextInputElement(action_id="plain_text_input-action"),
        label=PlainTextObject(text="Label", emoji=True),
    )
    return block

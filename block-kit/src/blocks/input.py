from slack_sdk.models.blocks import InputBlock
from slack_sdk.models.blocks.basic_components import PlainTextObject
from slack_sdk.models.blocks.block_elements import PlainTextInputElement


def example01() -> InputBlock:
    """
    Collects information from users via elements.
    https://docs.slack.dev/reference/block-kit/blocks/input-block/

    An input block containing a plain-text input element.
    """
    block = InputBlock(
        element=PlainTextInputElement(),
        label=PlainTextObject(text="Label", emoji=True),
    )
    return block

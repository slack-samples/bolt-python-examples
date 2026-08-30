from slack_sdk.models.blocks import InputBlock
from slack_sdk.models.blocks.basic_components import PlainTextObject
from slack_sdk.models.blocks.block_elements import EmailInputElement


def example01() -> InputBlock:
    """
    Allows user to enter an email into a single-line field.
    https://docs.slack.dev/reference/block-kit/block-elements/email-input-element/

    An input block with an email input element.
    """
    block = InputBlock(
        block_id="input123",
        label=PlainTextObject(text="Email Address"),
        element=EmailInputElement(
            action_id="email_text_input-action",
            placeholder=PlainTextObject(text="Enter an email"),
        ),
    )
    return block

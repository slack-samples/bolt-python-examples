from slack_sdk.models.blocks import ActionsBlock
from slack_sdk.models.blocks.basic_components import (
    ConfirmObject,
    MarkdownTextObject,
    PlainTextObject,
)
from slack_sdk.models.blocks.block_elements import ButtonElement


def example01() -> ActionsBlock:
    """
    Defines a dialog that adds a confirmation step to interactive elements.
    https://docs.slack.dev/reference/block-kit/composition-objects/confirmation-dialog-object/

    An actions block with a button carrying a confirmation dialog.
    """
    block = ActionsBlock(
        elements=[
            ButtonElement(
                text=PlainTextObject(text="Approve", emoji=True),
                confirm=ConfirmObject(
                    title=PlainTextObject(text="Are you sure?"),
                    text=MarkdownTextObject(
                        text="Would you not prefer a good game of _chess_?"
                    ),
                    confirm=PlainTextObject(text="Do it"),
                    deny=PlainTextObject(text="Stop, I changed my mind!"),
                ),
                style="primary",
                value="click_me_123",
            ),
            ButtonElement(
                text=PlainTextObject(text="Deny", emoji=True),
                style="danger",
                value="click_me_123",
            ),
        ],
    )
    return block

from slack_sdk.models.blocks import ContextActionsBlock
from slack_sdk.models.blocks.basic_components import PlainTextObject
from slack_sdk.models.blocks.block_elements import IconButtonElement


def example01() -> ContextActionsBlock:
    """
    An icon button to perform actions.
    https://docs.slack.dev/reference/block-kit/block-elements/icon-button-element/

    A context actions block with an icon button.
    """
    block = ContextActionsBlock(
        elements=[
            IconButtonElement(
                icon="trash",
                text=PlainTextObject(text="Delete"),
                action_id="delete_button",
                value="delete_item",
            ),
        ]
    )
    return block

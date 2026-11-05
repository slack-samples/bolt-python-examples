from slack_sdk.models.blocks import ContextActionsBlock
from slack_sdk.models.blocks.basic_components import (
    FeedbackButtonObject,
    PlainTextObject,
)
from slack_sdk.models.blocks.block_elements import (
    FeedbackButtonsElement,
    IconButtonElement,
)


def example01() -> ContextActionsBlock:
    """
    Displays actions as contextual info, which can include both feedback buttons and icon buttons.
    https://docs.slack.dev/reference/block-kit/blocks/context-actions-block/

    Context actions block with feedback buttons.
    """
    block = ContextActionsBlock(
        elements=[
            FeedbackButtonsElement(
                action_id="feedback_buttons_1",
                positive_button=FeedbackButtonObject(
                    text=PlainTextObject(text="👍"),
                    value="positive_feedback",
                ),
                negative_button=FeedbackButtonObject(
                    text=PlainTextObject(text="👎"),
                    value="negative_feedback",
                ),
            ),
        ],
    )
    return block


def example02() -> ContextActionsBlock:
    """
    Context actions block with an icon button.
    """
    block = ContextActionsBlock(
        elements=[
            IconButtonElement(
                icon="trash",
                text=PlainTextObject(text="Delete"),
                action_id="delete_button_1",
                value="delete_item",
            ),
        ],
    )
    return block

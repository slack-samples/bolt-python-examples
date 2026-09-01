from slack_sdk.models.blocks import ContextActionsBlock
from slack_sdk.models.blocks.basic_components import (
    FeedbackButtonObject,
    PlainTextObject,
)
from slack_sdk.models.blocks.block_elements import FeedbackButtonsElement


def example01() -> ContextActionsBlock:
    """
    Buttons to indicate positive or negative feedback.
    https://docs.slack.dev/reference/block-kit/block-elements/feedback-buttons-element/

    A context actions block with feedback buttons.
    """
    block = ContextActionsBlock(
        elements=[
            FeedbackButtonsElement(
                action_id="feedback_buttons_1",
                positive_button=FeedbackButtonObject(
                    text=PlainTextObject(text="Good", emoji=None),
                    value="positive_feedback",
                    accessibility_label="Mark this response as good",
                ),
                negative_button=FeedbackButtonObject(
                    text=PlainTextObject(text="Bad", emoji=None),
                    value="negative_feedback",
                    accessibility_label="Mark this response as bad",
                ),
            ),
        ]
    )
    return block

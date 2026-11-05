from slack_sdk.models.blocks import InputBlock
from slack_sdk.models.blocks.basic_components import (
    DispatchActionConfig,
    PlainTextObject,
)
from slack_sdk.models.blocks.block_elements import PlainTextInputElement


def example01() -> InputBlock:
    """
    Defines when a plain-text input element will return a block_actions interaction payload.
    https://docs.slack.dev/reference/block-kit/composition-objects/dispatch-action-configuration-object/

    An input block with a multiline plain-text input carrying a dispatch action configuration.
    """
    block = InputBlock(
        dispatch_action=True,
        element=PlainTextInputElement(
            multiline=True,
            dispatch_action_config=DispatchActionConfig(
                trigger_actions_on=["on_character_entered"],
            ),
        ),
        label=PlainTextObject(text="This is a multiline plain-text input", emoji=True),
    )
    return block

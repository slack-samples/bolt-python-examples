from slack_sdk.models.blocks import InputBlock
from slack_sdk.models.blocks.basic_components import PlainTextObject
from slack_sdk.models.blocks.block_elements import RichTextInputElement
from slack_sdk.models.views import View


def example01() -> View:
    """
    Allows users to enter formatted text in a WYSIWYG composer, offering the same messaging writing experience as in Slack.
    https://docs.slack.dev/reference/block-kit/block-elements/rich-text-input-element/

    A home view with an input block containing a rich text input element.
    """
    view = View(
        type="home",
        blocks=[
            InputBlock(
                element=RichTextInputElement(
                    action_id="rich_text_input-action",
                    dispatch_action_config={
                        "trigger_actions_on": ["on_character_entered"],
                    },
                    focus_on_load=True,
                    placeholder=PlainTextObject(text="Enter text", emoji=None),
                ),
                label=PlainTextObject(text="Label", emoji=True),
            ),
        ],
    )
    return view

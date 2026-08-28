from slack_sdk.models.blocks import SectionBlock
from slack_sdk.models.blocks.basic_components import (
    MarkdownTextObject,
    Option,
    PlainTextObject,
)
from slack_sdk.models.blocks.block_elements import CheckboxesElement


def example01() -> SectionBlock:
    """
    Allows users to choose multiple items from a list of options.
    https://docs.slack.dev/reference/block-kit/block-elements/checkboxes-element/

    A section block with a checkboxes element as an accessory.
    """
    block = SectionBlock(
        text=PlainTextObject(text="Check out these charming checkboxes"),
        accessory=CheckboxesElement(
            action_id="this_is_an_action_id",
            initial_options=[
                Option(value="A1", text=PlainTextObject(text="Checkbox 1")),
            ],
            options=[
                Option(value="A1", text=PlainTextObject(text="Checkbox 1")),
                Option(
                    value="A2",
                    text=PlainTextObject(text="Checkbox 2"),
                    description=MarkdownTextObject(
                        text="*A description of option two*"
                    ),
                ),
            ],
        ),
    )
    return block

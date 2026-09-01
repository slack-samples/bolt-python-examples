from slack_sdk.models.blocks import SectionBlock
from slack_sdk.models.blocks.basic_components import (
    MarkdownTextObject,
    Option,
    PlainTextObject,
)
from slack_sdk.models.blocks.block_elements import CheckboxesElement
from slack_sdk.models.views import View


def example01() -> View:
    """
    Allows users to choose multiple items from a list of options.
    https://docs.slack.dev/reference/block-kit/block-elements/checkboxes-element/

    A section block containing a group of checkboxes.
    """
    view = View(
        type="modal",
        title=PlainTextObject(text="My App", emoji=True),
        submit=PlainTextObject(text="Submit", emoji=True),
        close=PlainTextObject(text="Cancel", emoji=True),
        blocks=[
            SectionBlock(
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
            ),
        ],
    )
    return view

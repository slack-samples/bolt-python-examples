from slack_sdk.models.blocks import SectionBlock
from slack_sdk.models.blocks.basic_components import Option, PlainTextObject
from slack_sdk.models.blocks.block_elements import RadioButtonsElement


def example01() -> SectionBlock:
    """
    Allows users to choose one item from a list of possible options.
    https://docs.slack.dev/reference/block-kit/block-elements/radio-button-group-element/

    A section block with a radio button group element as an accessory.
    """
    block = SectionBlock(
        text=PlainTextObject(text="Check out these rad radio buttons"),
        accessory=RadioButtonsElement(
            action_id="this_is_an_action_id",
            initial_option=Option(value="A1", text=PlainTextObject(text="Radio 1")),
            options=[
                Option(value="A1", text=PlainTextObject(text="Radio 1")),
                Option(value="A2", text=PlainTextObject(text="Radio 2")),
            ],
        ),
    )
    return block

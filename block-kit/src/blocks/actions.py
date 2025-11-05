from slack_sdk.models.blocks import ActionsBlock
from slack_sdk.models.blocks.basic_components import Option, PlainTextObject
from slack_sdk.models.blocks.block_elements import (
    ButtonElement,
    DatePickerElement,
    OverflowMenuElement,
    StaticSelectElement,
)


def example01() -> ActionsBlock:
    """
    Holds multiple interactive elements.
    https://docs.slack.dev/reference/block-kit/blocks/actions-block/

    An actions block with a select menu and a button.
    """
    block = ActionsBlock(
        block_id="actions1",
        elements=[
            StaticSelectElement(
                action_id="select_2",
                placeholder=PlainTextObject(text="Which witch is the witchiest witch?"),
                options=[
                    Option(text=PlainTextObject(text="Matilda"), value="matilda"),
                    Option(text=PlainTextObject(text="Glinda"), value="glinda"),
                    Option(
                        text=PlainTextObject(text="Granny Weatherwax"),
                        value="grannyWeatherwax",
                    ),
                    Option(text=PlainTextObject(text="Hermione"), value="hermione"),
                ],
            ),
            ButtonElement(
                text=PlainTextObject(text="Cancel"),
                value="cancel",
                action_id="button_1",
            ),
        ],
    )
    return block


def example02() -> ActionsBlock:
    """
    An actions block with a datepicker, an overflow, and a button.
    """
    block = ActionsBlock(
        block_id="actionblock789",
        elements=[
            DatePickerElement(
                action_id="datepicker123",
                initial_date="1990-04-28",
                placeholder=PlainTextObject(text="Select a date"),
            ),
            OverflowMenuElement(
                action_id="overflow",
                options=[
                    Option(
                        text=PlainTextObject(text="*this is plain_text text*"),
                        value="value-0",
                    ),
                    Option(
                        text=PlainTextObject(text="*this is plain_text text*"),
                        value="value-1",
                    ),
                    Option(
                        text=PlainTextObject(text="*this is plain_text text*"),
                        value="value-2",
                    ),
                    Option(
                        text=PlainTextObject(text="*this is plain_text text*"),
                        value="value-3",
                    ),
                    Option(
                        text=PlainTextObject(text="*this is plain_text text*"),
                        value="value-4",
                    ),
                ],
            ),
            ButtonElement(
                text=PlainTextObject(text="Click Me"),
                value="click_me_123",
                action_id="button",
            ),
        ],
    )
    return block

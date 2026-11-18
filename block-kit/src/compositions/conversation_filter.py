from slack_sdk.models.blocks import InputBlock
from slack_sdk.models.blocks.basic_components import PlainTextObject
from slack_sdk.models.blocks.block_elements import (
    ConversationFilter,
    ConversationSelectElement,
)
from slack_sdk.models.views import View


def example01() -> View:
    """
    Defines a filter for the list of options in a conversation selector menu.
    https://docs.slack.dev/reference/block-kit/composition-objects/conversation-filter-object/

    A modal view with a conversations select input carrying a conversation filter.
    """
    view = View(
        type="modal",
        title=PlainTextObject(text="My App", emoji=True),
        submit=PlainTextObject(text="Submit", emoji=True),
        close=PlainTextObject(text="Cancel", emoji=True),
        blocks=[
            InputBlock(
                element=ConversationSelectElement(
                    placeholder=PlainTextObject(
                        text="Select a conversation", emoji=True
                    ),
                    filter=ConversationFilter(
                        include=["public", "mpim"],
                        exclude_bot_users=True,
                    ),
                ),
                label=PlainTextObject(
                    text="Choose the conversation to publish your result to:",
                    emoji=True,
                ),
            ),
        ],
    )
    return view

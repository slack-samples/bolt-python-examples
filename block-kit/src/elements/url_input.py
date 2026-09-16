from slack_sdk.models.blocks import InputBlock
from slack_sdk.models.blocks.basic_components import PlainTextObject
from slack_sdk.models.blocks.block_elements import UrlInputElement


def example01() -> InputBlock:
    """
    Allows user to enter a URL into a single-line field.
    https://docs.slack.dev/reference/block-kit/block-elements/url-input-element/

    An input block with a URL input element.
    """
    block = InputBlock(
        element=UrlInputElement(action_id="url_text_input-action"),
        label=PlainTextObject(text="Label", emoji=True),
    )
    return block

from slack_sdk.models.blocks import AlertBlock
from slack_sdk.models.blocks.basic_components import MarkdownTextObject


def example01() -> AlertBlock:
    """
    Displays alerts, warnings, and informational messages.
    https://docs.slack.dev/reference/block-kit/blocks/alert-block/

    An informational alert.
    """
    block = AlertBlock(
        text=MarkdownTextObject(text="The work is mysterious and important."),
        level="info",
    )
    return block

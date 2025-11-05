from slack_sdk.models.blocks import HeaderBlock
from slack_sdk.models.blocks.basic_components import PlainTextObject


def example01() -> HeaderBlock:
    """
    Displays a larger-sized text.
    https://docs.slack.dev/reference/block-kit/blocks/header-block/

    A simple header block.
    """
    block = HeaderBlock(text=PlainTextObject(text="A Heartfelt Header"))
    return block

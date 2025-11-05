from slack_sdk.models.blocks import DividerBlock


def example01() -> DividerBlock:
    """
    Visually separates pieces of info inside of a message.
    https://docs.slack.dev/reference/block-kit/blocks/divider-block/

    A simple divider block.
    """
    block = DividerBlock()
    return block

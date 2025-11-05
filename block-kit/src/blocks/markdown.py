from slack_sdk.models.blocks import MarkdownBlock


def example01() -> MarkdownBlock:
    """
    Displays formatted markdown.
    https://docs.slack.dev/reference/block-kit/blocks/markdown-block/

    A markdown block.
    """
    block = MarkdownBlock(text="**Lots of information here!!**")
    return block

from slack_sdk.models.blocks import SectionBlock
from slack_sdk.models.blocks.basic_components import MarkdownTextObject


def example01() -> SectionBlock:
    """
    Defines an object containing some text.
    https://docs.slack.dev/reference/block-kit/composition-objects/text-object/

    A section block containing an mrkdwn text object.
    """
    block = SectionBlock(
        text=MarkdownTextObject(
            text="A message *with some bold text* and _some italicized text_."
        )
    )
    return block

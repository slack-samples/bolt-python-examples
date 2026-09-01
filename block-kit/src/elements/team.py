from slack_sdk.models.blocks import RichTextBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextSectionElement,
)


def example01() -> RichTextBlock:
    """
    Renders as a mention of a workspace or team.
    https://docs.slack.dev/reference/block-kit/block-elements/team-element/

    A rich text block with a team mention in a section.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.Team(team_id="T123ABC456"),
                ]
            )
        ]
    )
    return block

from slack_sdk.models.blocks import RichTextBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextListElement,
    RichTextSectionElement,
)


def example01() -> RichTextBlock:
    """
    Displays a list of rich text items.
    https://docs.slack.dev/reference/block-kit/block-elements/rich-text-list-element/

    A rich text block with a bordered bullet list.
    """
    block = RichTextBlock(
        block_id="block1",
        elements=[
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.Text(
                        text="My favorite Slack features (in no particular order):"
                    ),
                ]
            ),
            RichTextListElement(
                style="bullet",
                indent=0,
                border=1,
                elements=[
                    RichTextSectionElement(
                        elements=[RichTextElementParts.Text(text="Huddles")]
                    ),
                    RichTextSectionElement(
                        elements=[RichTextElementParts.Text(text="Canvas")]
                    ),
                    RichTextSectionElement(
                        elements=[
                            RichTextElementParts.Text(text="Developing with Block Kit")
                        ]
                    ),
                ],
            ),
        ],
    )
    return block


def example02() -> RichTextBlock:
    """
    A rich text block with a nested bullet list, created by indenting the
    middle list into a sub-list.
    """
    block = RichTextBlock(
        block_id="block1",
        elements=[
            RichTextSectionElement(
                elements=[RichTextElementParts.Text(text="Breakfast foods I enjoy:")]
            ),
            RichTextListElement(
                style="bullet",
                elements=[
                    RichTextSectionElement(
                        elements=[RichTextElementParts.Text(text="Hashbrowns")]
                    ),
                    RichTextSectionElement(
                        elements=[RichTextElementParts.Text(text="Eggs")]
                    ),
                ],
            ),
            RichTextListElement(
                style="bullet",
                indent=1,
                elements=[
                    RichTextSectionElement(
                        elements=[RichTextElementParts.Text(text="Scrambled")]
                    ),
                    RichTextSectionElement(
                        elements=[RichTextElementParts.Text(text="Over easy")]
                    ),
                ],
            ),
            RichTextListElement(
                style="bullet",
                elements=[
                    RichTextSectionElement(
                        elements=[
                            RichTextElementParts.Text(text="Pancakes, extra syrup")
                        ]
                    ),
                ],
            ),
        ],
    )
    return block

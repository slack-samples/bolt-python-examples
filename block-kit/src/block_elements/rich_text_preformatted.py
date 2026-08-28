from slack_sdk.models.blocks import RichTextBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextPreformattedElement,
)


def example01() -> RichTextBlock:
    """
    Displays a preformatted rich text element.
    https://docs.slack.dev/reference/block-kit/block-elements/rich-text-preformatted-element/

    A rich text block with a borderless preformatted code snippet.
    """
    block = RichTextBlock(
        elements=[
            RichTextPreformattedElement(
                border=0,
                elements=[
                    RichTextElementParts.Text(
                        text='{\n  "object": {\n    "description": "this is an example of a json object"\n  }\n}'
                    ),
                ],
            )
        ]
    )
    return block

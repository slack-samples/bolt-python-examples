from slack_sdk.models.blocks import ContextBlock, ImageElement, MarkdownTextObject


def example01() -> ContextBlock:
    """
    Provides contextual info, which can include both images and text.
    https://docs.slack.dev/reference/block-kit/blocks/context-block/

    A context block with an image and text.
    """
    block = ContextBlock(
        elements=[
            ImageElement(
                image_url="https://image.freepik.com/free-photo/red-drawing-pin_1156-445.jpg",
                alt_text="images",
            ),
            MarkdownTextObject(text="Location: **Dogpatch**"),
        ]
    )
    return block

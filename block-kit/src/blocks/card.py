from slack_sdk.models.blocks import CardBlock
from slack_sdk.models.blocks.basic_components import MarkdownTextObject, PlainTextObject
from slack_sdk.models.blocks.block_elements import ButtonElement, ImageElement


def example01() -> CardBlock:
    """
    Displays content in a card.
    https://docs.slack.dev/reference/block-kit/blocks/card-block/

    A card with an icon, title, subtitle, hero image, body, and an action
    button.
    """
    block = CardBlock(
        icon=ImageElement(
            image_url="https://picsum.photos/36/36",
            alt_text="Icon",
        ),
        title=MarkdownTextObject(text="Lumon Industries"),
        subtitle=MarkdownTextObject(text="Committed to work-life balance"),
        hero_image=ImageElement(
            image_url="https://picsum.photos/400/300",
            alt_text="Sample hero image",
        ),
        body=MarkdownTextObject(text="Please enjoy each card equally."),
        actions=[
            ButtonElement(
                text=PlainTextObject(text="Action Button", emoji=False),
                action_id="button_action",
            )
        ],
    )
    return block

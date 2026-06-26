from slack_sdk.models.blocks import ButtonElement, CardBlock, ImageElement
from slack_sdk.models.blocks.basic_components import MarkdownTextObject, PlainTextObject


def example01() -> CardBlock:
    """
    Displays a card, a container for related content with an optional image,
    title, body, and actions.
    https://docs.slack.dev/reference/block-kit/blocks/card-block/

    A full card with an icon, title, subtitle, hero image, body, and an action
    button.
    """
    block = CardBlock(
        icon=ImageElement(  # type: ignore[arg-type]
            image_url="https://picsum.photos/36/36",
            alt_text="Icon",
        ),
        title=MarkdownTextObject(text="Lumon Industries", verbatim=False),
        subtitle=MarkdownTextObject(
            text="Committed to work-life balance", verbatim=False
        ),
        hero_image=ImageElement(  # type: ignore[arg-type]
            image_url="https://picsum.photos/400/300",
            alt_text="Sample hero image",
        ),
        body=MarkdownTextObject(text="Please enjoy each card equally.", verbatim=False),
        actions=[
            ButtonElement(
                text=PlainTextObject(text="Action Button", emoji=False),
                action_id="button_action",
            ),
        ],
    )
    return block


def example02() -> CardBlock:
    """
    A minimal card with only a title and an action button. At least one of
    hero_image, title, actions, or body is required on a card.
    """
    block = CardBlock(
        title=MarkdownTextObject(text="Pick your refinement number"),
        actions=[
            ButtonElement(
                text=PlainTextObject(text="Refine"),
                action_id="refine_action",
            ),
        ],
    )
    return block

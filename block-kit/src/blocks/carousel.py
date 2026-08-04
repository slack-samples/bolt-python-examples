from slack_sdk.models.blocks import CardBlock, CarouselBlock
from slack_sdk.models.blocks.basic_components import MarkdownTextObject, PlainTextObject
from slack_sdk.models.blocks.block_elements import ButtonElement, ImageElement


def example01() -> CarouselBlock:
    """
    Displays a scrollable, horizontal collection of cards.
    https://docs.slack.dev/reference/block-kit/blocks/carousel-block/

    A carousel with three cards, each with an icon, title, subtitle, hero
    image, body, and an action button.
    """
    block = CarouselBlock(
        elements=[
            CardBlock(
                block_id="carousel-card-1",
                icon=ImageElement(  # type: ignore[arg-type]
                    image_url="https://picsum.photos/36/36",
                    alt_text="Icon",
                ),
                title=MarkdownTextObject(text="MDR"),
                subtitle=MarkdownTextObject(text="Refining data files"),
                hero_image=ImageElement(  # type: ignore[arg-type]
                    image_url="https://picsum.photos/400/300",
                    alt_text="Sample hero image",
                ),
                body=MarkdownTextObject(text="Blue badge required to gain access."),
                actions=[
                    ButtonElement(
                        text=PlainTextObject(text="Action Button", emoji=False),
                        action_id="button_action_1",
                    )
                ],
            ),
            CardBlock(
                block_id="carousel-card-2",
                icon=ImageElement(  # type: ignore[arg-type]
                    image_url="https://picsum.photos/36/36",
                    alt_text="Icon",
                ),
                title=MarkdownTextObject(text="O&D"),
                subtitle=MarkdownTextObject(
                    text="Storage, maintenance, and rotation of art pieces"
                ),
                hero_image=ImageElement(  # type: ignore[arg-type]
                    image_url="https://picsum.photos/400/300",
                    alt_text="Sample hero image",
                ),
                body=MarkdownTextObject(text="Green badge required to gain access."),
                actions=[
                    ButtonElement(
                        text=PlainTextObject(text="Action Button", emoji=False),
                        action_id="button_action_2",
                    )
                ],
            ),
            CardBlock(
                block_id="carousel-card-3",
                icon=ImageElement(  # type: ignore[arg-type]
                    image_url="https://picsum.photos/36/36",
                    alt_text="Icon",
                ),
                title=MarkdownTextObject(text="Wellness Center"),
                subtitle=MarkdownTextObject(text="Wellness sessions"),
                hero_image=ImageElement(  # type: ignore[arg-type]
                    image_url="https://picsum.photos/400/300",
                    alt_text="Sample hero image",
                ),
                body=MarkdownTextObject(
                    text="Please take a seat in the waiting room until called."
                ),
                actions=[
                    ButtonElement(
                        text=PlainTextObject(text="Action Button", emoji=False),
                        action_id="button_action_3",
                    )
                ],
            ),
        ],
    )
    return block

from slack_sdk.models.blocks import RichTextBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextListElement,
    RichTextPreformattedElement,
    RichTextQuoteElement,
    RichTextSectionElement,
)


def example01() -> list[RichTextBlock]:
    """
    Displays formatted, structured representation of text.
    https://docs.slack.dev/reference/block-kit/blocks/rich-text-block/

    Four basic rich text section examples (basic, bold, italic, strikethrough).
    """
    blocks = [
        RichTextBlock(
            elements=[
                RichTextSectionElement(
                    elements=[
                        RichTextElementParts.Text(
                            text="Hello there, I am a basic rich text block!"
                        )
                    ]
                )
            ]
        ),
        RichTextBlock(
            elements=[
                RichTextSectionElement(
                    elements=[
                        RichTextElementParts.Text(text="Hello there, "),
                        RichTextElementParts.Text(
                            text="I am a bold rich text block!", style={"bold": True}
                        ),
                    ]
                )
            ]
        ),
        RichTextBlock(
            elements=[
                RichTextSectionElement(
                    elements=[
                        RichTextElementParts.Text(text="Hello there, "),
                        RichTextElementParts.Text(
                            text="I am an italic rich text block!",
                            style={"italic": True},
                        ),
                    ]
                )
            ]
        ),
        RichTextBlock(
            elements=[
                RichTextSectionElement(
                    elements=[
                        RichTextElementParts.Text(text="Hello there, "),
                        RichTextElementParts.Text(
                            text="I am a strikethrough rich text block!",
                            style={"strike": True},
                        ),
                    ]
                )
            ]
        ),
    ]
    return blocks


def example02() -> RichTextBlock:
    """
    A rich text block with a bullet list.
    """
    block = RichTextBlock(
        block_id="block1",
        elements=[
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.Text(
                        text="My favorite Slack features (in no particular order):"
                    )
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


def example03() -> RichTextBlock:
    """
    A rich text block with a nested bullet list.
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
                    )
                ],
            ),
        ],
    )
    return block


def example04() -> RichTextBlock:
    """
    A rich text block with preformatted code.
    """
    block = RichTextBlock(
        elements=[
            RichTextPreformattedElement(
                border=0,
                elements=[
                    RichTextElementParts.Text(
                        text='{\n  "object": {\n    "description": "this is an example of a json object"\n  }\n}'
                    )
                ],
            )
        ]
    )
    return block


def example05() -> RichTextBlock:
    """
    A rich text block with a quote.
    """
    block = RichTextBlock(
        block_id="Vrzsu",
        elements=[
            RichTextQuoteElement(
                elements=[
                    RichTextElementParts.Text(
                        text="What we need is good examples in our documentation."
                    )
                ]
            ),
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.Text(text="Yes - I completely agree, Luke!")
                ]
            ),
        ],
    )
    return block


def example06() -> RichTextBlock:
    """
    A rich text block with a broadcast element.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[RichTextElementParts.Broadcast(range="everyone")]
            )
        ]
    )
    return block


def example07() -> RichTextBlock:
    """
    A rich text block with a color element.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[RichTextElementParts.Color(value="#F405B3")]
            )
        ]
    )
    return block


def example08() -> RichTextBlock:
    """
    A rich text block with a channel element.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[RichTextElementParts.Channel(channel_id="C123ABC456")]
            )
        ]
    )
    return block


def example09() -> RichTextBlock:
    """
    A rich text block with a date element.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.Date(
                        timestamp=1720710212,
                        format="{date_num} at {time}",
                        fallback="timey",
                    )
                ]
            )
        ]
    )
    return block


def example10() -> RichTextBlock:
    """
    A rich text block with emoji elements.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[
                    RichTextElementParts.Emoji(name="basketball"),
                    RichTextElementParts.Text(text=" "),
                    RichTextElementParts.Emoji(name="snowboarder"),
                    RichTextElementParts.Text(text=" "),
                    RichTextElementParts.Emoji(name="checkered_flag"),
                ]
            )
        ]
    )
    return block


def example11() -> RichTextBlock:
    """
    A rich text block with a link element.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[RichTextElementParts.Link(url="https://api.slack.com")]
            )
        ]
    )
    return block


def example12() -> RichTextBlock:
    """
    A rich text block with a user mention element.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[RichTextElementParts.User(user_id="U123ABC456")]
            )
        ]
    )
    return block


def example13() -> RichTextBlock:
    """
    A rich text block with a usergroup mention element.
    """
    block = RichTextBlock(
        elements=[
            RichTextSectionElement(
                elements=[RichTextElementParts.UserGroup(usergroup_id="G123ABC456")]
            )
        ]
    )
    return block

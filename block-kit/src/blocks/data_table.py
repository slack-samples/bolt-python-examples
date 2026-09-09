from slack_sdk.models.blocks import (
    DataTableBlock,
    RawTextObject,
    RichTextBlock,
    RichTextElementParts,
    RichTextSectionElement,
)


def example01() -> DataTableBlock:
    """
    Displays rich tables that support pagination, sorting, filtering, and interactivity.
    https://docs.slack.dev/reference/block-kit/blocks/data-table-block/

    A data table of departments with raw text and rich text cells.
    """
    block = DataTableBlock(
        caption="A Fabulous Table",
        rows=[
            [
                RawTextObject(text="Name"),
                RawTextObject(text="Department"),
                RawTextObject(text="Badge"),
            ],
            [
                RawTextObject(text="Data Refinement Department"),
                RawTextObject(text="MDR"),
                RichTextBlock(
                    elements=[
                        RichTextSectionElement(
                            elements=[
                                RichTextElementParts.Text(
                                    text="Blue",
                                    style=RichTextElementParts.TextStyle(bold=True),
                                ),
                            ],
                        ),
                    ],
                ),
            ],
            [
                RawTextObject(text="Art Sourcing Department"),
                RawTextObject(text="O&D"),
                RichTextBlock(
                    elements=[
                        RichTextSectionElement(
                            elements=[
                                RichTextElementParts.Text(text="Green"),
                                RichTextElementParts.Text(
                                    text="review",
                                    style=RichTextElementParts.TextStyle(italic=True),
                                ),
                            ],
                        ),
                    ],
                ),
            ],
            [
                RawTextObject(text="Wellness Department"),
                RawTextObject(text="Wellness Center"),
                RichTextBlock(
                    elements=[
                        RichTextSectionElement(
                            elements=[
                                RichTextElementParts.Text(
                                    text="Limited",
                                    style=RichTextElementParts.TextStyle(bold=True),
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ],
    )
    return block

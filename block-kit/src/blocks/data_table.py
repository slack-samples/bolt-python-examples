from slack_sdk.models.blocks import (
    DataTableBlock,
    RawTextObject,
    RichTextBlock,
    RichTextElementParts,
    RichTextSectionElement,
)


def _rich_text(*elements: RichTextElementParts.Text) -> RichTextBlock:
    """Wrap rich text elements in a rich_text cell for a data table."""
    return RichTextBlock(elements=[RichTextSectionElement(elements=list(elements))])


def example01() -> DataTableBlock:
    """
    Displays structured, paginated data in rows and columns.
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
                _rich_text(
                    RichTextElementParts.Text(
                        text="Blue",
                        style=RichTextElementParts.TextStyle(bold=True),
                    )
                ),
            ],
            [
                RawTextObject(text="Art Sourcing Department"),
                RawTextObject(text="O&D"),
                _rich_text(
                    RichTextElementParts.Text(text="Green"),
                    RichTextElementParts.Text(
                        text="review",
                        style=RichTextElementParts.TextStyle(italic=True),
                    ),
                ),
            ],
            [
                RawTextObject(text="Wellness Department"),
                RawTextObject(text="Wellness Center"),
                _rich_text(
                    RichTextElementParts.Text(
                        text="Limited",
                        style=RichTextElementParts.TextStyle(bold=True),
                    )
                ),
            ],
        ],
    )
    return block

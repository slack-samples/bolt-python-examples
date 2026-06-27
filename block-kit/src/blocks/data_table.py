from typing import Any, Dict, List, Optional, Set

from slack_sdk.models.blocks import Block


class DataTableBlock(Block):
    """Displays data arranged in rows and columns with built-in pagination.
    https://docs.slack.dev/reference/block-kit/blocks/data-table-block

    The slack_sdk does not yet ship a typed class for this block, so this
    example defines one that mirrors the SDK convention.
    """

    type = "data_table"

    @property
    def attributes(self) -> Set[str]:  # type: ignore[override]
        return super().attributes.union(
            {"rows", "caption", "page_size", "row_header_column_index"}
        )

    def __init__(
        self,
        *,
        rows: List[List[Dict[str, Any]]],
        caption: str,
        page_size: Optional[int] = None,
        row_header_column_index: Optional[int] = None,
        block_id: Optional[str] = None,
    ) -> None:
        """
        Args:
            rows (required): An array of rows, where each row is an array of cell
                objects. Cells may be raw_text, raw_number, or rich_text.
            caption (required): A label for the table, rendered as the HTML caption
                element for accessibility.
            page_size: The number of rows shown per page. Ranges from 1 to 100 and
                defaults to 5.
            row_header_column_index: The zero-based index of the column that
                identifies row headers for accessibility. Defaults to 0.
            block_id: A unique identifier for a block. If not specified, a block_id
                will be generated. Maximum length for this field is 255 characters.
        """
        super().__init__(type=self.type, block_id=block_id)
        self.rows = rows
        self.caption = caption
        self.page_size = page_size
        self.row_header_column_index = row_header_column_index


def example01() -> DataTableBlock:
    """
    Displays data arranged in rows and columns with built-in pagination.
    https://docs.slack.dev/reference/block-kit/blocks/data-table-block/

    A table with a header row and three data rows. The first two columns hold
    raw text, while the third column holds rich text with styled badges.
    """
    block = DataTableBlock(
        caption="A Fabulous Table",
        rows=[
            [
                {"type": "raw_text", "text": "Name"},
                {"type": "raw_text", "text": "Department"},
                {"type": "raw_text", "text": "Badge"},
            ],
            [
                {"type": "raw_text", "text": "Data Refinement Department"},
                {"type": "raw_text", "text": "MDR"},
                {
                    "type": "rich_text",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Blue",
                                    "style": {"bold": True},
                                }
                            ],
                        }
                    ],
                },
            ],
            [
                {"type": "raw_text", "text": "Art Sourcing Department"},
                {"type": "raw_text", "text": "O&D"},
                {
                    "type": "rich_text",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {"type": "text", "text": "Green"},
                                {
                                    "type": "text",
                                    "text": "review",
                                    "style": {"italic": True},
                                },
                            ],
                        }
                    ],
                },
            ],
            [
                {"type": "raw_text", "text": "Wellness Department"},
                {"type": "raw_text", "text": "Wellness Center"},
                {
                    "type": "rich_text",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Limited",
                                    "style": {"bold": True},
                                }
                            ],
                        }
                    ],
                },
            ],
        ],
    )
    return block

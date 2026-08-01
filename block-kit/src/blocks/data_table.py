from slack_sdk.models.blocks import DataTableBlock


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

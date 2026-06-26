from slack_sdk.models.blocks import TableBlock


def example01() -> TableBlock:
    """
    Displays structured data arranged in rows and columns.
    https://docs.slack.dev/reference/block-kit/blocks/table-block/

    A table with header, text, link, and number cells alongside column settings.
    """
    block = TableBlock(
        block_id="optional_unique_id",
        column_settings=[
            {"is_wrapped": True, "align": "left"},
            {"align": "right", "is_wrapped": False},
        ],
        rows=[
            [
                {"type": "raw_text", "text": "Header A"},
                {"type": "raw_text", "text": "Header B"},
            ],
            [
                {"type": "raw_text", "text": "Data 1A"},
                {
                    "type": "rich_text",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "link",
                                    "text": "Data 1B",
                                    "url": "https://slack.com",
                                }
                            ],
                        }
                    ],
                },
            ],
            [
                {"type": "raw_text", "text": "Data 2A"},
                {"type": "raw_number", "text": "12345"},
            ],
        ],
    )
    return block

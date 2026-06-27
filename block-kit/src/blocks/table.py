from slack_sdk.models.blocks import TableBlock


def example01() -> TableBlock:
    """
    Displays data arranged in rows and columns.
    https://docs.slack.dev/reference/block-kit/blocks/table-block/

    A table with a header row and two data rows. The first column is wrapped
    and contains raw text, while the second column is right-aligned and
    contains rich text links.
    """
    block = TableBlock(
        column_settings=[
            {"is_wrapped": True},
            {"align": "right"},
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
                {
                    "type": "rich_text",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "link",
                                    "text": "Data 2B",
                                    "url": "https://slack.com",
                                }
                            ],
                        }
                    ],
                },
            ],
        ],
    )
    return block

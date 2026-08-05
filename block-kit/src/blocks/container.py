from slack_sdk.models.blocks import (
    ActionsBlock,
    ContainerBlock,
    ContextBlock,
    DividerBlock,
    SectionBlock,
)
from slack_sdk.models.blocks.basic_components import MarkdownTextObject
from slack_sdk.models.blocks.block_elements import ButtonElement


def example01() -> ContainerBlock:
    """
    A general-purpose wrapper for grouping child blocks together, with a configurable size.
    https://docs.slack.dev/reference/block-kit/blocks/container-block/

    A collapsible container grouping a bulk-update summary out of section,
    divider, context, and actions child blocks.
    """
    block = ContainerBlock(
        block_id="bkb_container_bulk_update",
        title="Bulk update: 2 records selected",
        subtitle="Review changes before confirming",
        is_collapsible=True,
        child_blocks=[
            SectionBlock(
                block_id="record-row-1",
                text=MarkdownTextObject(
                    text="*DCW-1024*\nStatus: Open → Closed\nAssignee: @princessdonut → @carl"
                ),
            ),
            DividerBlock(block_id="bulk-div-1"),
            SectionBlock(
                block_id="record-row-2",
                text=MarkdownTextObject(
                    text="*DCW-1025*\nStatus: In Progress → Closed\nAssignee: @mordecai → @carl"
                ),
            ),
            DividerBlock(block_id="bulk-div-2"),
            ContextBlock(
                block_id="bulk-status-bar",
                elements=[
                    MarkdownTextObject(
                        text=":white_check_mark: 2 records will be updated • Status → Closed • Assignee → @carl"
                    )
                ],
            ),
            ActionsBlock(
                block_id="bulk-actions",
                elements=[
                    ButtonElement(
                        text="Confirm All",
                        action_id="bulk_confirm",
                        style="primary",
                    ),
                    ButtonElement(text="Cancel", action_id="bulk_cancel"),
                ],
            ),
        ],
    )
    return block

from slack_sdk.models.blocks import PlanBlock, RichTextBlock, TaskCardBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextSectionElement,
)


def example01() -> PlanBlock:
    """
    Displays a collection of related tasks.
    https://docs.slack.dev/reference/block-kit/blocks/plan-block/

    A plan block with multiple task cards in various states.
    """
    block = PlanBlock(
        title="Thinking completed",
        tasks=[
            TaskCardBlock(
                task_id="call_001",
                title="Fetched user profile information",
                status="in_progress",
                details=RichTextBlock(
                    block_id="viMWO",
                    elements=[
                        RichTextSectionElement(
                            elements=[
                                RichTextElementParts.Text(text="Searched database...")
                            ]
                        )
                    ],
                ),
                output=RichTextBlock(
                    block_id="viMWO",
                    elements=[
                        RichTextSectionElement(
                            elements=[
                                RichTextElementParts.Text(text="Profile data loaded")
                            ]
                        )
                    ],
                ),
            ),
            TaskCardBlock(
                task_id="call_002",
                title="Checked user permissions",
                status="pending",
            ),
            TaskCardBlock(
                task_id="call_003",
                title="Generated comprehensive user report",
                status="complete",
                output=RichTextBlock(
                    block_id="crsk",
                    elements=[
                        RichTextSectionElement(
                            elements=[
                                RichTextElementParts.Text(
                                    text="15 data points compiled"
                                )
                            ]
                        )
                    ],
                ),
            ),
        ],
    )
    return block

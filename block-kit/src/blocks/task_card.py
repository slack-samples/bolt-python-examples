from slack_sdk.models.blocks import RichTextBlock, TaskCardBlock
from slack_sdk.models.blocks.block_elements import (
    RichTextElementParts,
    RichTextSectionElement,
    UrlSourceElement,
)


def example01() -> TaskCardBlock:
    """
    Displays a single task which represents a single action.
    This is an experimental block type that requires a toggle to preview.
    https://docs.slack.dev/reference/block-kit/blocks/task-card-block/

    A task card with output and sources.
    """
    block = TaskCardBlock(
        task_id="task_1",
        title="Fetching weather data",
        status="pending",
        output=RichTextBlock(
            elements=[
                RichTextSectionElement(
                    elements=[
                        RichTextElementParts.Text(
                            text="Found weather data for Chicago from 2 sources"
                        )
                    ]
                )
            ]
        ),
        sources=[
            UrlSourceElement(
                url="https://weather.com/",
                text="weather.com",
            ),
            UrlSourceElement(
                url="https://www.accuweather.com/",
                text="accuweather.com",
            ),
        ],
    )
    return block

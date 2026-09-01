from slack_sdk.models.blocks import TaskCardBlock
from slack_sdk.models.blocks.block_elements import UrlSourceElement


def example01() -> UrlSourceElement:
    """
    Displays a URL source with optional icon.
    https://docs.slack.dev/reference/block-kit/block-elements/url-source-element/

    A URL source element.
    """
    element = UrlSourceElement(
        url="https://docs.slack.dev/",
        text="Slack API docs",
    )
    return element


def example02() -> TaskCardBlock:
    """
    A task card block with URL source elements.
    """
    block = TaskCardBlock(
        task_id="task_1",
        title="Scientific findings",
        status="complete",
        sources=[
            UrlSourceElement(
                url="https://docs.example.com/",
                text="Tracy's delightful docs",
            ),
            UrlSourceElement(
                url="https://research.example.com/",
                text="Haley's resourceful research",
            ),
        ],
    )
    return block

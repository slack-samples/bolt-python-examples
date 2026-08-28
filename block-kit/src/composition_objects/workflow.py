from slack_sdk.models.blocks import SectionBlock
from slack_sdk.models.blocks.basic_components import (
    MarkdownTextObject,
    PlainTextObject,
    Workflow,
    WorkflowTrigger,
)
from slack_sdk.models.blocks.block_elements import WorkflowButtonElement


def example01() -> SectionBlock:
    """
    Defines an object containing workflow information.
    https://docs.slack.dev/reference/block-kit/composition-objects/workflow-object/

    A workflow button whose workflow references a configured trigger.
    """
    block = SectionBlock(
        text=MarkdownTextObject(
            text="A message *with some bold text* and _some italicized text_."
        ),
        accessory=WorkflowButtonElement(
            text=PlainTextObject(text="Run Workflow"),
            action_id="workflowbutton123",
            workflow=Workflow(
                trigger=WorkflowTrigger(
                    url="https://slack.com/shortcuts/Ft0123ABC456/xyz...zyx",
                    customizable_input_parameters=[
                        {
                            "name": "input_parameter_a",
                            "value": "Value for input param A",
                        },
                        {
                            "name": "input_parameter_b",
                            "value": "Value for input param B",
                        },
                    ],
                ),
            ),
        ),
    )
    return block

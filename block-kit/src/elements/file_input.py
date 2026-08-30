from slack_sdk.models.blocks import InputBlock
from slack_sdk.models.blocks.basic_components import PlainTextObject
from slack_sdk.models.blocks.block_elements import FileInputElement


def example01() -> InputBlock:
    """
    Allows user to upload files.
    https://docs.slack.dev/reference/block-kit/block-elements/file-input-element/

    An input block with a file input element.
    """
    block = InputBlock(
        block_id="input_block_id",
        label=PlainTextObject(text="Upload Files"),
        element=FileInputElement(
            action_id="file_input_action_id_1",
            filetypes=["jpg", "png"],
            max_files=5,
        ),
    )
    return block

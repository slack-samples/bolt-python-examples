from slack_sdk.models.blocks import InputBlock
from slack_sdk.models.blocks.basic_components import PlainTextObject
from slack_sdk.models.blocks.block_elements import FileInputElement
from slack_sdk.models.views import View


def example01() -> View:
    """
    Allows user to upload files.
    https://docs.slack.dev/reference/block-kit/block-elements/file-input-element/

    A modal view with a file input element hosted in an input block.
    """
    view = View(
        type="modal",
        title=PlainTextObject(text="My App", emoji=True),
        submit=PlainTextObject(text="Submit", emoji=True),
        close=PlainTextObject(text="Cancel", emoji=True),
        blocks=[
            InputBlock(
                block_id="input_block_id",
                label=PlainTextObject(text="Upload Files"),
                element=FileInputElement(
                    action_id="file_input_action_id_1",
                    filetypes=["jpg", "png"],
                    max_files=5,
                ),
            ),
        ],
    )
    return view

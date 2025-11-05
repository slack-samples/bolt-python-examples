from slack_sdk.models.blocks import FileBlock


def example01() -> FileBlock:
    """
    Displays info about remote files.
    https://docs.slack.dev/reference/block-kit/blocks/file-block/

    A file block for a remote file.
    """
    block = FileBlock(external_id="ABCD1", source="remote")
    return block

from slack_sdk.models.blocks import VideoBlock
from slack_sdk.models.blocks.basic_components import PlainTextObject


def example01() -> VideoBlock:
    """
    Displays an embedded video player.
    https://docs.slack.dev/reference/block-kit/blocks/video-block/

    A video block.
    """
    block = VideoBlock(
        title=PlainTextObject(
            text="Use the Events API to create a dynamic App Home", emoji=True
        ),
        title_url="https://www.youtube.com/watch?v=8876OZV_Yy0",
        description=PlainTextObject(text="Slack sure is nifty!", emoji=True),
        video_url="https://www.youtube.com/embed/8876OZV_Yy0?feature=oembed&autoplay=1",
        alt_text="Use the Events API to create a dynamic App Home",
        thumbnail_url="https://i.ytimg.com/vi/8876OZV_Yy0/hqdefault.jpg",
    )
    return block

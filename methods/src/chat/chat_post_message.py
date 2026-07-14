import os

from slack_sdk import WebClient
from slack_sdk.web import SlackResponse


def example01(client: WebClient) -> SlackResponse:
    """
    Sends a message to a channel.
    https://docs.slack.dev/reference/methods/chat.postmessage
    """
    # Call the chat.postMessage method using the WebClient
    response = client.chat_postMessage(
        channel="C123ABC456",
        text="Here's a message for you",
    )
    return response


if __name__ == "__main__":
    # Read a token from the environment variables
    token = os.environ.get("SLACK_TOKEN")

    # Initialize a WebClient with the given token
    client = WebClient(token=token)

    print(example01(client))

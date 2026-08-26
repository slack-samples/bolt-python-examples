# Methods

An interface for querying information from and enacting change in a Slack workspace.

Read the [docs](https://docs.slack.dev/apis/web-api/) for explanations of concepts, or explore [reference](https://docs.slack.dev/reference/methods) pages for specific functionalities.

## Making a request

```sh
$ cd src/chat  # Navigate to a method family
$ slack install --environment local  # Create an app
$ vim chat_post_message.py  # Edit arguments
$ export SLACK_TOKEN=xoxb-example  # Set if unchanged
$ slack run chat_post_message.py  # Make the request
```

## What's on call

### chat

- **[chat.appendStream](https://docs.slack.dev/reference/methods/chat.appendStream)**: Appends text to an existing streaming conversation. [Implementation](./src/chat/chat_append_stream.py).
- **[chat.postMessage](https://docs.slack.dev/reference/methods/chat.postmessage)**: Sends a message to a channel. [Implementation](./src/chat/chat_post_message.py).
- **[chat.startStream](https://docs.slack.dev/reference/methods/chat.startStream)**: Starts a new streaming conversation. [Implementation](./src/chat/chat_start_stream.py).
- **[chat.stopStream](https://docs.slack.dev/reference/methods/chat.stopStream)**: Stops a streaming conversation. [Implementation](./src/chat/chat_stop_stream.py).

# Methods

Individual Slack Web API method calls with the `slack_sdk` `WebClient`.

Read the [docs](https://docs.slack.dev/reference/methods) to explore every method, or explore implementations of specific families.

## What's on display

### chat

- **[chat.postMessage](https://docs.slack.dev/reference/methods/chat.postmessage)**: Sends a message to a channel. [Implementation](./src/chat/chat_post_message.py). Scopes: `chat:write`.

## Running an example

Set a bot token and run an example module directly:

```sh
export SLACK_TOKEN="xoxb-your-token"
python -m src.chat.chat_post_message
```

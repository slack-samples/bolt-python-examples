# Methods

An interface for querying information from and enacting change in a Slack workspace.

Read the [docs](https://docs.slack.dev/apis/web-api/) for explanations of concepts, or explore [reference](https://docs.slack.dev/reference/methods) pages for specific functionalities.

## Making a request

```sh
$ cd src/chat  # Navigate to a method family
$ slack install --environment local  # Create an app
$ vim chat_post_message.py  # Edit arguments
$ export SLACK_TOKEN=xoxb-example  # Set if unchanged
$ slack run chat_post_message  # Make the request
```

## What's on call

### agents.sessions

- **[agents.sessions.rename](https://docs.slack.dev/reference/methods/agents.sessions.rename)**: Renames an agent session. [Implementation](./src/agents_sessions/agents_sessions_rename.py).
- **[agents.sessions.setStatus](https://docs.slack.dev/reference/methods/agents.sessions.setStatus)**: Sets the lifecycle status of an agent session, creating the session if it does not already exist. [Implementation](./src/agents_sessions/agents_sessions_set_status.py).

### chat

- **[chat.postMessage](https://docs.slack.dev/reference/methods/chat.postmessage)**: Sends a message to a channel. [Implementation](./src/chat/chat_post_message.py).

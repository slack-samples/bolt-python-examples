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

### codeChannels

- **[codeChannels.archive](https://docs.slack.dev/reference/methods/codeChannels.archive)**: Archives a code channel, optionally recording a summary message on the channel. [Implementation](./src/code_channels/code_channels_archive.py).
- **[codeChannels.create](https://docs.slack.dev/reference/methods/codeChannels.create)**: Creates a dedicated code channel for an agent session. [Implementation](./src/code_channels/code_channels_create.py).
- **[codeChannels.getCanvas](https://docs.slack.dev/reference/methods/codeChannels.getCanvas)**: Fetches a canvas attached to a code channel — full content plus comment threads — in a single round-trip. [Implementation](./src/code_channels/code_channels_get_canvas.py).
- **[codeChannels.listViews](https://docs.slack.dev/reference/methods/codeChannels.listViews)**: Lists the view tabs attached to a code channel. [Implementation](./src/code_channels/code_channels_list_views.py).
- **[codeChannels.removeView](https://docs.slack.dev/reference/methods/codeChannels.removeView)**: Removes a view from a code channel. [Implementation](./src/code_channels/code_channels_remove_view.py).
- **[codeChannels.rename](https://docs.slack.dev/reference/methods/codeChannels.rename)**: Renames a code channel. [Implementation](./src/code_channels/code_channels_rename.py).
- **[codeChannels.setCanvasContent](https://docs.slack.dev/reference/methods/codeChannels.setCanvasContent)**: Replaces the full markdown content of a canvas attached to a code channel, preserving the comment threads on the sections your agent didn't change. [Implementation](./src/code_channels/code_channels_set_canvas_content.py).
- **[codeChannels.setCommands](https://docs.slack.dev/reference/methods/codeChannels.setCommands)**: Registers the set of slash commands your agent offers in a code channel. [Implementation](./src/code_channels/code_channels_set_commands.py).
- **[codeChannels.setProperties](https://docs.slack.dev/reference/methods/codeChannels.setProperties)**: Sets properties on a code channel: context bar items and external resource details. [Implementation](./src/code_channels/code_channels_set_properties.py).
- **[codeChannels.setView](https://docs.slack.dev/reference/methods/codeChannels.setView)**: Creates or updates a view in a code channel. Views can render HTML, diffs, Block Kit, or canvases as tabs alongside the conversation. [Implementation](./src/code_channels/code_channels_set_view.py).

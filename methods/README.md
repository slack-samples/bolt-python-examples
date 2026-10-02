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

### agents

- **[agents.conversations.archive](https://docs.slack.dev/reference/methods/agents.conversations.archive)**: Archive a code channel. [Implementation](./src/agents/conversations/agents_conversations_archive.py).
- **[agents.conversations.create](https://docs.slack.dev/reference/methods/agents.conversations.create)**: Create a dedicated code channel for an agent session. [Implementation](./src/agents/conversations/agents_conversations_create.py).
- **[agents.conversations.getCanvas](https://docs.slack.dev/reference/methods/agents.conversations.getCanvas)**: Fetch a canvas attached to a code channel. [Implementation](./src/agents/conversations/agents_conversations_get_canvas.py).
- **[agents.conversations.listViews](https://docs.slack.dev/reference/methods/agents.conversations.listViews)**: List the views currently attached to a code channel. [Implementation](./src/agents/conversations/agents_conversations_list_views.py).
- **[agents.conversations.removeView](https://docs.slack.dev/reference/methods/agents.conversations.removeView)**: Remove a view from a code channel. [Implementation](./src/agents/conversations/agents_conversations_remove_view.py).
- **[agents.conversations.setCanvasContent](https://docs.slack.dev/reference/methods/agents.conversations.setCanvasContent)**: Replace the full markdown content of a plan canvas attached to a code channel. [Implementation](./src/agents/conversations/agents_conversations_set_canvas_content.py).
- **[agents.conversations.setCommands](https://docs.slack.dev/reference/methods/agents.conversations.setCommands)**: Register the set of agent-defined slash commands for the calling agent in a code channel. [Implementation](./src/agents/conversations/agents_conversations_set_commands.py).
- **[agents.conversations.setProperties](https://docs.slack.dev/reference/methods/agents.conversations.setProperties)**: Set properties on a code channel. [Implementation](./src/agents/conversations/agents_conversations_set_properties.py).
- **[agents.conversations.setView](https://docs.slack.dev/reference/methods/agents.conversations.setView)**: Create or update a view in a code channel. [Implementation](./src/agents/conversations/agents_conversations_set_view.py).
- **[agents.sessions.rename](https://docs.slack.dev/reference/methods/agents.sessions.rename)**: Rename an agent session. [Implementation](./src/agents/sessions/agents_sessions_rename.py).
- **[agents.sessions.setStatus](https://docs.slack.dev/reference/methods/agents.sessions.setStatus)**: Set an agent session's lifecycle status, creating the session if needed. [Implementation](./src/agents/sessions/agents_sessions_set_status.py).

### blocks

- **[blocks.validate](https://docs.slack.dev/reference/methods/blocks.validate)**: Validates blocks, messages, and views Block Kit JSON payloads. [Implementation](./src/blocks/blocks_validate.py).

### chat

- **[chat.postMessage](https://docs.slack.dev/reference/methods/chat.postmessage)**: Sends a message to a channel. [Implementation](./src/chat/chat_post_message.py).

# Slack Identity

Run an MCP server for the Slackbot MCP client that responds with Block Kit and authenticates against existing installations.

## Setup

```sh
$ ngrok http 3000
$ slack install --app local  # Create a new app
$ slack app settings
$ slack env init  # Update defaults
$ slack manifest  # Validate fields
$ slack run
$ open https://1234-56-78-90-0.ngrok-free.app/slack/install  # Install the app
```

Ask Slackbot: "Make me a profile card using the latest MCP tools"

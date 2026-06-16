# No Auth

Run an unauthenticated MCP server for the Slackbot MCP client that responds with an [interactive UI](https://modelcontextprotocol.io/extensions/apps/overview).

## Setup

```sh
$ ngrok http 3000  # Update manifest with these values
$ slack manifest   # Review values
$ slack install --environment local  # Create a new app
$ slack app settings                 # Gather signing secret
$ slack env set SLACK_SIGNING_SECRET
$ slack run
```

Ask Slackbot: "Roll 2d20"

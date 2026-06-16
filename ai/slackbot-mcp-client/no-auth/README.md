# No Auth

Run an unauthenticated MCP server for the Slackbot MCP client that responds with an [interactive UI](https://modelcontextprotocol.io/extensions/apps/overview).

## Setup

```sh
$ ngrok http 3000 --host-header=rewrite  # Rewrite Host to localhost so the MCP server's DNS-rebinding protection accepts the request; update manifest with these values
$ slack manifest   # Review values
$ slack install --environment local  # Create a new app
$ slack app settings                 # Gather signing secret
$ slack env set SLACK_SIGNING_SECRET
$ slack run
```

Ask Slackbot: "Roll 2d20"

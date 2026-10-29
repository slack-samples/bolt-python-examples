# Manual OAuth

Connect a remote MCP server to the Slackbot MCP client with an external auth provider.

## Setup

> Callback URL: https://oauth2.slack.com/external/auth/callback

```sh
$ open https://github.com/settings/developers # Create GitHub app
$ slack manifest                              # Replace values
$ slack install --environment deployed        # Create Slack app
$ slack external-auth add-secret
```

Ask Slackbot: "Show me my recent GitHub pull requests"

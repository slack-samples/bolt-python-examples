# Slackbot MCP Client

Connect MCP servers to Slackbot with different options for authentication.

Read the [docs](https://docs.slack.dev/ai/slackbot-mcp-client) to explore more concepts around MCP.

## Included examples

### Authentication methods

- **[Dynamic client registration](https://docs.slack.dev/ai/slackbot-mcp-client#dcr)**: Connect a remote MCP server to the Slackbot MCP client using Dynamic Client Registration (DCR). [Implementation](./dynamic-client-registration/).
- **[Manual OAuth](https://docs.slack.dev/ai/slackbot-mcp-client#manual-oauth)**: Connect a remote MCP server to the Slackbot MCP client with an external auth provider. [Implementation](./manual-oauth/).
- **[No auth](https://docs.slack.dev/ai/slackbot-mcp-client#no-auth)**: Run an unauthenticated MCP server for the Slackbot MCP client. [Implementation](./no-auth/).
- **[Slack identity](https://docs.slack.dev/ai/slackbot-mcp-client#slack-identity)**: Run an MCP server for the Slackbot MCP client that authenticates against existing installations. [Implementation](./slack-identity/).

### Rich responses

- **[MCP Apps](https://docs.slack.dev/ai/slackbot-mcp-client/returning-rich-responses#mcp-apps)**: Run an MCP server for the Slackbot MCP client that responds with an interactive UI. [Implementation](./rich-responses/mcp-apps/).

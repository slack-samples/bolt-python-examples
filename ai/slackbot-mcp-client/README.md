# Slackbot MCP Client

Connect MCP servers to Slackbot with different options for authentication.

Read the [docs](https://docs.slack.dev/ai/slackbot-mcp-client) to explore more concepts around MCP.

## Included examples

### Authentication methods

- **[Dynamic client registration](https://docs.slack.dev/ai/slackbot-mcp-client/dynamic-client-registration)**: Connect a remote MCP server to the Slackbot MCP client using Dynamic Client Registration (DCR). [Implementation](./dynamic-client-registration/).
- **[External auth](https://docs.slack.dev/ai/slackbot-mcp-client/external-auth)**: Connect a remote MCP server to the Slackbot MCP client with manual OAuth provider configuration. [Implementation](./external-auth/).
- **[No auth](https://docs.slack.dev/ai/slackbot-mcp-client/no-auth)**: Run an unauthenticated MCP server for the Slackbot MCP client that responds with an interactive UI. [Implementation](./no-auth/).
- **[Slack identity](https://docs.slack.dev/ai/slackbot-mcp-client/slack-identity)**: Run an MCP server for the Slackbot MCP client that responds with Block Kit and authenticates against existing installations. [Implementation](./slack-identity/).

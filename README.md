# Bolt for Python Examples

This collections of examples highlights features of a Slack app in the language of Bolt for Python.

## Available demonstrations

- **[AI in Slack](./ai)**: Agent experiences and MCP features in an interactive conversation interface.
- **[Block Kit](./block-kit)**: The framework of visual components arranged to create app layouts.
- **[Methods](./methods)**: An interface for querying information from and enacting change in a Slack workspace.
- **[Standardized Auth](./standardized-auth)**: Connect user accounts with the Slack-owned Connect and Manage connection controls.

## Claude Code, Codex, Cursor, and Other Coding Agents

Install the [Slack MCP and Skills Plugin](https://docs.slack.dev/ai/slack-skills-plugin/) so your coding agent can create, run, and deploy Slack apps, look up Web API methods and scopes, and build Block Kit without guessing.

### Claude Code

Run this in a Claude Code session:

```
/plugin install slack@claude-plugins-official
```

### Codex

Run this in your terminal:

```sh
codex plugin marketplace add slackapi/slack-skills-plugin
codex plugin add slack@slack
```

### Cursor

Run this in a Cursor Agent chat:

```
/add-plugin slack
```

### Other agents

Install the skills with `npx skills`, using your [agent's identifier](https://github.com/vercel-labs/skills#supported-agents):

```sh
npx skills add slackapi/slack-skills-plugin -y -a <agent>

# For example, OpenCode
npx skills add slackapi/slack-skills-plugin -y -a opencode
```

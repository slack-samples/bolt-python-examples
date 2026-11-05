# Work Objects Showcase

Your app can respond to links being shared in Slack with Work Object metadata to display a link preview. Users can click the preview to view authenticated data in the flexpane. If supported, users can edit app data directly from the flexpane.

You can also [post](https://docs.slack.dev/messaging/work-objects/#implementation-notifications) Work Object metadata directly with `chat.postMessage`, without a link being shared.

Read the [docs](https://docs.slack.dev/messaging/work-objects/) to learn more!

## Setup

### Option 1: Create a new app with the Slack CLI

```bash
slack init && slack run
```

### Option 2: Create a Slack App in the UI and copy over your tokens

Create an app on [https://api.slack.com/apps](https://api.slack.com/apps) from the app manifest in this repo (`manifest.json`).

Configure environment variables:
```bash
# OAuth & Permissions → Bot User OAuth Token
export SLACK_BOT_TOKEN=<your-bot-token>
# Basic Information → App-Level Tokens (create one with the `connections:write` scope)
export SLACK_APP_TOKEN=<your-app-token>
```

Install dependencies and run the app:
```bash
# Setup virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the dependencies
pip install -r requirements.txt

# Start the server
python3 app.py
```

# Work Objects Showcase

Your app can respond to links being shared in Slack with Work Object metadata to display a link preview. Users can click the preview to view authenticated data in the flexpane. If supported, users can edit app data directly from the flexpane.

You can also [post](https://docs.slack.dev/messaging/work-objects/#implementation-notifications) Work Object metadata directly with `chat.postMessage`, without a link being shared.

Read the [docs](https://docs.slack.dev/messaging/work-objects/) to learn more!

## Running locally

### 1. Setup environment variables

```zsh
# Replace with your tokens
export SLACK_BOT_TOKEN=<your-bot-token>
export SLACK_APP_TOKEN=<your-app-level-token>
```

### 2. Setup your local project

```zsh
# Setup virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the dependencies
pip install -r requirements.txt
```

### 3. Start the server
```zsh
python3 src/app.py
```

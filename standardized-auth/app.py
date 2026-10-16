import os

from slack_sdk.oauth.installation_store import FileInstallationStore
from slack_sdk.oauth.state_store.stateless import StatelessOAuthStateStore

from src.app import build_app

if __name__ == "__main__":
    app = build_app(
        installation_store=FileInstallationStore(base_dir="./data/installations"),
        state_store=StatelessOAuthStateStore(
            expiration_seconds=300, signing_secret=os.environ["SLACK_SIGNING_SECRET"]
        ),
        base_url=os.environ["BASE_URL"],
    )
    app.start(port=int(os.environ.get("PORT", "3000")))

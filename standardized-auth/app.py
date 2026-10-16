import os

from slack_sdk.oauth.installation_store import FileInstallationStore
from slack_sdk.oauth.state_store import FileOAuthStateStore

from src.app import build_app

if __name__ == "__main__":
    app = build_app(
        installation_store=FileInstallationStore(base_dir="./data/installations"),
        state_store=FileOAuthStateStore(
            expiration_seconds=600, base_dir="./data/states"
        ),
        base_url=os.environ["BASE_URL"],
    )
    app.start(port=int(os.environ.get("PORT", "3000")))

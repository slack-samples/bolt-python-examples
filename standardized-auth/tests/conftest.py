import os
from unittest.mock import MagicMock

import pytest
from slack_sdk import WebClient
from slack_sdk.oauth.installation_store import FileInstallationStore

from src.acme import installation_store

os.environ["SLACK_CLIENT_ID"] = "111.222"
os.environ["SLACK_CLIENT_SECRET"] = "test_client_secret"
os.environ["SLACK_SIGNING_SECRET"] = "test_signing_secret"
os.environ["BASE_URL"] = "https://acme.example"


@pytest.fixture
def store(tmp_path, monkeypatch) -> FileInstallationStore:
    monkeypatch.setattr(installation_store, "base_dir", str(tmp_path / "installations"))
    return installation_store


@pytest.fixture
def client() -> MagicMock:
    client = MagicMock(spec=WebClient)
    client.auth_test.return_value = {"ok": True, "user": "ada", "team": "Acme Corp"}
    return client

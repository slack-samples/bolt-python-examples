import os
from unittest.mock import MagicMock, patch

import pytest
from slack_sdk import WebClient
from slack_sdk.web import SlackResponse

from src.connections import Connections, connections

os.environ["SLACK_BOT_TOKEN"] = "xoxb-test-bot"
os.environ["BASE_URL"] = "https://acme.example"

patch(
    "slack_sdk.web.client.WebClient.auth_test",
    return_value=SlackResponse(
        client=None,
        http_verb="POST",
        api_url="https://slack.com/api/auth.test",
        req_args={},
        data={"ok": True, "team_id": "T0001", "bot_id": "B0001", "user_id": "U0BOT"},
        headers={},
        status_code=200,
    ),
).start()


@pytest.fixture
def store(tmp_path, monkeypatch) -> Connections:
    monkeypatch.setattr(connections, "path", tmp_path / "acme.db")
    return connections


@pytest.fixture
def client() -> MagicMock:
    return MagicMock(spec=WebClient)

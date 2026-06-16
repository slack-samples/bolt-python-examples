import hashlib
import hmac
import json
import os
import time
from unittest.mock import MagicMock, patch

import pytest
from starlette.testclient import TestClient

os.environ["SLACK_SIGNING_SECRET"] = "test_signing_secret"
os.environ["SLACK_CLIENT_ID"] = "111.222"
os.environ["SLACK_CLIENT_SECRET"] = "client_secret"

from src.app import app  # noqa: E402

SIGNING_SECRET = "test_signing_secret"


@pytest.fixture(scope="module")
def client():
    with TestClient(app, base_url="http://localhost:8000") as c:
        yield c


def test_returns_tool_call_response(client):
    mock_installation = MagicMock()
    mock_installation.bot_token = "xoxb-fake-token"

    body = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/call",
            "params": {
                "name": "get_profile_card",
                "arguments": {"user_id": "U12345"},
                "_meta": {
                    "slack": {
                        "user_id": "U99999",
                        "team_id": "T11111",
                    }
                },
            },
        }
    )
    headers = sign_request(body)

    with (
        patch(
            "src.app.installation_store.find_installation",
            return_value=mock_installation,
        ),
        patch("src.app.WebClient") as MockWebClient,
    ):
        mock_client = MagicMock()
        mock_client.users_info.return_value = {
            "ok": True,
            "user": {
                "profile": {
                    "real_name": "Test User",
                    "title": "Engineer",
                    "email": "test@example.com",
                    "image_72": "https://example.com/avatar.png",
                }
            },
        }
        MockWebClient.return_value = mock_client

        resp = client.post("/mcp", content=body, headers=headers)

    assert resp.status_code == 200
    data = resp.json()
    result = data["result"]
    assert "Test User" in result["content"][0]["text"]
    assert "Engineer" in result["content"][0]["text"]
    blocks = result["_meta"]["slack"]["blocks"]
    assert blocks[0]["type"] == "card"
    assert blocks[0]["title"]["text"] == "Test User"


def test_requires_team_installation(client):
    body = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "get_profile_card",
                "arguments": {"user_id": "U12345"},
                "_meta": {
                    "slack": {
                        "user_id": "U99999",
                        "team_id": "T11111",
                    }
                },
            },
        }
    )
    headers = sign_request(body)

    with patch(
        "src.app.installation_store.find_installation",
        side_effect=Exception("Not found"),
    ):
        resp = client.post("/mcp", content=body, headers=headers)

    assert resp.status_code == 200
    data = resp.json()
    result = data["result"]
    assert "not installed" in result["content"][0]["text"].lower()
    blocks = result["_meta"]["slack"]["blocks"]
    assert blocks[0]["type"] == "section"
    assert blocks[0]["accessory"]["type"] == "button"


def test_rejects_unsigned_requests(client):
    body = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": "get_profile_card",
                "arguments": {"user_id": "U12345"},
            },
        }
    )
    resp = client.post(
        "/mcp", content=body, headers={"content-type": "application/json"}
    )

    assert resp.status_code == 401


def sign_request(body: str, secret: str = SIGNING_SECRET) -> dict:
    timestamp = str(int(time.time()))
    sig_basestring = f"v0:{timestamp}:{body}"
    signature = (
        "v0="
        + hmac.new(secret.encode(), sig_basestring.encode(), hashlib.sha256).hexdigest()
    )
    return {
        "x-slack-request-timestamp": timestamp,
        "x-slack-signature": signature,
        "content-type": "application/json",
        "accept": "application/json",
    }

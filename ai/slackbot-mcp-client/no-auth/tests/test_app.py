import hashlib
import hmac
import json
import os
import time
from unittest.mock import patch

import pytest
from starlette.testclient import TestClient

os.environ["SLACK_BOT_TOKEN"] = "xoxb-test"
os.environ["SLACK_SIGNING_SECRET"] = "test_signing_secret"

_mock_auth = patch(
    "slack_sdk.web.client.WebClient.auth_test",
    return_value={"ok": True, "bot_id": "B123", "user_id": "U123", "team_id": "T123"},
)
_mock_auth.start()

from src.app import app  # noqa: E402

SIGNING_SECRET = "test_signing_secret"


@pytest.fixture(scope="module")
def client():
    with TestClient(app, base_url="http://localhost:8000") as c:
        yield c


def test_returns_tool_call_results(client):
    body = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/call",
            "params": {"name": "roll_dice", "arguments": {"sides": 6, "count": 2}},
        }
    )
    sig = sign_request(body)
    resp = client.post(
        "/mcp",
        content=body,
        headers={
            "content-type": "application/json",
            "accept": "application/json, text/event-stream",
            "x-slack-request-timestamp": sig["timestamp"],
            "x-slack-signature": sig["signature"],
        },
    )

    assert resp.status_code == 200
    data = resp.json()
    assert data["jsonrpc"] == "2.0"
    assert data["id"] == 2
    result = data["result"]
    structured = result["structuredContent"]
    assert structured["sides"] == 6
    assert structured["count"] == 2
    assert len(structured["rolls"]) == 2
    assert all(1 <= r <= 6 for r in structured["rolls"])
    assert structured["total"] == sum(structured["rolls"])


def test_serves_ui_resources(client):
    body = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "resources/read",
            "params": {"uri": "ui://dice-roller/dice.html"},
        }
    )
    sig = sign_request(body)
    resp = client.post(
        "/mcp",
        content=body,
        headers={
            "content-type": "application/json",
            "accept": "application/json, text/event-stream",
            "x-slack-request-timestamp": sig["timestamp"],
            "x-slack-signature": sig["signature"],
        },
    )

    assert resp.status_code == 200
    data = resp.json()
    assert data["jsonrpc"] == "2.0"
    assert data["id"] == 3
    contents = data["result"]["contents"]
    assert contents[0]["uri"] == "ui://dice-roller/dice.html"
    assert contents[0]["mimeType"] == "text/html;profile=mcp-app"
    assert "Dice Roller" in contents[0]["text"]


def test_rejects_unsigned_requests(client):
    body = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {"name": "roll_dice", "arguments": {"sides": 6, "count": 1}},
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
    return {"timestamp": timestamp, "signature": signature}

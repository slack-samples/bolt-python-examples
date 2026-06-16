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
    """Create a TestClient that triggers the app lifespan (starts session manager)."""
    with TestClient(app, base_url="http://localhost:8000") as c:
        yield c


def test_returns_tool_call_results(client):
    """POST to /mcp with a valid signature and tools/call for roll_dice."""
    body = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {"name": "roll_dice", "arguments": {"sides": 6, "count": 2}},
        }
    )
    headers = sign_request(body)
    resp = client.post("/mcp", content=body, headers=headers)

    assert resp.status_code == 200
    data = resp.json()
    assert data["jsonrpc"] == "2.0"
    assert data["id"] == 1
    result = data["result"]
    structured = result["structuredContent"]
    assert structured["sides"] == 6
    assert structured["count"] == 2
    assert len(structured["rolls"]) == 2
    assert all(1 <= r <= 6 for r in structured["rolls"])
    assert structured["total"] == sum(structured["rolls"])


def test_serves_ui_resources(client):
    """POST to /mcp with a valid signature and resources/read for the dice HTML."""
    body = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "resources/read",
            "params": {"uri": "ui://dice-roller/dice.html"},
        }
    )
    headers = sign_request(body)
    resp = client.post("/mcp", content=body, headers=headers)

    assert resp.status_code == 200
    data = resp.json()
    assert data["jsonrpc"] == "2.0"
    assert data["id"] == 1
    contents = data["result"]["contents"]
    assert len(contents) >= 1
    assert "Dice Roller" in contents[0]["text"]


def test_rejects_unsigned_requests(client):
    """POST to /mcp without Slack signature headers returns 401."""
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


# --- Helpers ---


def sign_request(body: str, secret: str = SIGNING_SECRET) -> dict:
    """Generate valid Slack signature headers for the given request body."""
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

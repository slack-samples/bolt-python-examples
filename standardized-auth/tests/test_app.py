import hashlib
import hmac
import json
import time
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from unittest.mock import MagicMock, patch
from urllib.parse import parse_qs, urlencode, urlparse

import pytest
from slack_bolt import App, BoltContext, BoltRequest
from slack_sdk import WebClient

from src.acme import find_user_token
from src.app import build_app
from tests.helpers import installation

SIGNING_SECRET = "test_signing_secret"
BOT_AUTH_TEST = {"ok": True, "team_id": "T0001", "bot_id": "B0001", "user_id": "U0BOT"}
USER_AUTH_TEST = {
    "ok": True,
    "team_id": "T0001",
    "team": "Acme Corp",
    "user_id": "U0ADA",
    "user": "ada",
}


def auth_test(token: str) -> dict:
    return BOT_AUTH_TEST if token.startswith("xoxb-") else USER_AUTH_TEST


@pytest.fixture
def app(store) -> App:
    store.save(installation("U0ADA", user_token="xoxp-test-ada"))
    return build_app()


def test_connect_clicks_are_acknowledged(app):
    with patch.object(WebClient, "auth_test", side_effect=auth_test):
        response = app.dispatch(block_action("auth_provider_connect_acme"))

    assert response.status == 200


def test_clicks_for_other_providers_are_not_handled(app):
    with patch.object(WebClient, "auth_test", side_effect=auth_test):
        response = app.dispatch(block_action("auth_provider_connect_other"))

    assert response.status == 404


def test_disconnect_clicks_forget_the_account(app, store):
    with slack_api() as api:
        response = app.dispatch(block_action("auth_provider_disconnect_acme"))
        wait_until(lambda: api.auth_revoke.called)

    assert response.status == 200
    assert find_user_token(workspace(), "U0ADA") is None


def test_app_home_opened_publishes_the_home_view(app):
    with slack_api() as api:
        response = app.dispatch(event({"type": "app_home_opened", "user": "U0ADA"}))
        wait_until(lambda: api.views_publish.called)

    assert response.status == 200
    assert api.views_publish.call_args.kwargs["user_id"] == "U0ADA"


def test_status_requests_are_answered(app):
    status_requested = {"type": "user_connection_status_requested", "user": "U0ADA"}
    with slack_api() as api:
        response = app.dispatch(event(status_requested))
        wait_until(lambda: api.apps_user_connection_update.called)

    assert response.status == 200
    api.apps_user_connection_update.assert_called_once_with(
        user_id="U0ADA", status="connected"
    )


def test_revoked_user_tokens_are_forgotten(app, store):
    tokens_revoked = {"type": "tokens_revoked", "tokens": {"oauth": ["U0ADA"]}}
    with slack_api() as api:
        response = app.dispatch(event(tokens_revoked))
        wait_until(lambda: api.views_publish.called)

    assert response.status == 200
    assert find_user_token(workspace(), "U0ADA") is None


def test_install_redirects_straight_to_slack_with_the_user_scope(app):
    response = app.oauth_flow.handle_installation(BoltRequest(body="", query={}))

    location = urlparse(response.headers["location"][0])
    assert response.status == 302
    assert parse_qs(location.query)["user_scope"] == ["users.profile:read"]


@contextmanager
def slack_api() -> Iterator[MagicMock]:
    methods = [
        "apps_user_connection_requestAuth",
        "apps_user_connection_update",
        "auth_revoke",
        "views_publish",
    ]
    api = MagicMock()
    with (
        patch.object(WebClient, "auth_test", side_effect=auth_test),
        patch.multiple(
            WebClient, **{method: getattr(api, method) for method in methods}
        ),
    ):
        yield api


def wait_until(condition: Callable[[], bool]) -> None:
    deadline = time.time() + 2
    while not condition():
        assert time.time() < deadline, "timed out waiting for the listener"
        time.sleep(0.01)


def workspace() -> BoltContext:
    return BoltContext({"team_id": "T0001", "is_enterprise_install": False})


def event(body: dict) -> BoltRequest:
    envelope = json.dumps(
        {
            "type": "event_callback",
            "api_app_id": "A0001",
            "team_id": "T0001",
            "event": body,
            "event_id": "Ev0001",
            "event_time": 1700000000,
        }
    )
    headers = signed_headers(envelope)
    headers["content-type"] = ["application/json"]
    return BoltRequest(body=envelope, headers=headers)


def block_action(action_id: str) -> BoltRequest:
    payload = {
        "type": "block_actions",
        "api_app_id": "A0001",
        "team": {"id": "T0001"},
        "user": {"id": "U0ADA", "team_id": "T0001"},
        "trigger_id": "123.456.abc",
        "actions": [
            {
                "type": "button",
                "action_id": action_id,
                "block_id": "acme",
                "action_ts": "1700000000.000001",
            }
        ],
    }
    body = urlencode({"payload": json.dumps(payload)})
    return BoltRequest(body=body, headers=signed_headers(body))


def signed_headers(body: str, secret: str = SIGNING_SECRET) -> dict:
    timestamp = str(int(time.time()))
    sig_basestring = f"v0:{timestamp}:{body}"
    signature = (
        "v0="
        + hmac.new(secret.encode(), sig_basestring.encode(), hashlib.sha256).hexdigest()
    )
    return {
        "content-type": ["application/x-www-form-urlencoded"],
        "x-slack-request-timestamp": [timestamp],
        "x-slack-signature": [signature],
    }

import time
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from unittest.mock import MagicMock, patch

import pytest
from slack_bolt import App, BoltRequest
from slack_sdk import WebClient

from src.bolt_app import app as bolt_app


@pytest.fixture
def app(store) -> App:
    store.connect("U0ADA", "ada")
    return bolt_app


def test_connect_clicks_are_acknowledged(app):
    response = app.dispatch(block_action("auth_provider_connect_acme"))

    assert response.status == 200


def test_clicks_for_other_providers_are_not_handled(app):
    response = app.dispatch(block_action("auth_provider_connect_other"))

    assert response.status == 404


def test_disconnect_clicks_forget_the_account(app, store):
    with slack_api() as api:
        response = app.dispatch(block_action("auth_provider_disconnect_acme"))
        wait_until(lambda: api.views_publish.called)

    assert response.status == 200
    assert store.find("U0ADA") is None


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


@contextmanager
def slack_api() -> Iterator[MagicMock]:
    methods = [
        "apps_user_connection_requestAuth",
        "apps_user_connection_update",
        "views_publish",
    ]
    api = MagicMock()
    with patch.multiple(
        WebClient, **{method: getattr(api, method) for method in methods}
    ):
        yield api


def wait_until(condition: Callable[[], bool]) -> None:
    deadline = time.time() + 2
    while not condition():
        assert time.time() < deadline, "timed out waiting for the listener"
        time.sleep(0.01)


def event(body: dict) -> BoltRequest:
    envelope = {
        "type": "event_callback",
        "api_app_id": "A0001",
        "team_id": "T0001",
        "event": body,
        "event_id": "Ev0001",
        "event_time": 1700000000,
    }
    return BoltRequest(body=envelope, mode="socket_mode")


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
    return BoltRequest(body=payload, mode="socket_mode")

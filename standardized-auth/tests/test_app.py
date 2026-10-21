from unittest.mock import MagicMock

from slack_sdk import WebClient

from app import (
    app_home_opened_callback,
    connect_callback,
    disconnect_callback,
    user_connection_callback,
    user_connection_status_requested_callback,
)
from src import connections
from tests.helpers import TempConnections


def button_click(value: str) -> dict:
    return {"user": {"id": "U0ADA"}, "actions": [{"value": value}]}


class TestApp:
    def setup_method(self):
        self.connections = TempConnections()
        self.ack = MagicMock()
        self.client = MagicMock(spec=WebClient)

    def teardown_method(self):
        self.connections.close()

    def sent_provider(self) -> dict:
        return self.client.apps_user_connection_requestAuth.call_args.kwargs[
            "primary_provider"
        ]

    def home_block(self) -> dict:
        view = self.client.views_publish.call_args.kwargs["view"].to_dict()
        return view["blocks"][-1]

    def test_app_home_opened_shows_the_connection(self):
        connections.connect("U0ADA")

        app_home_opened_callback(client=self.client, event={"user": "U0ADA"})

        assert self.client.views_publish.call_args.kwargs["user_id"] == "U0ADA"
        assert self.home_block()["is_connected"] is True

    def test_connect_saves_and_shows_the_connection(self):
        connect_callback(ack=self.ack, body=button_click("acme"), client=self.client)

        self.ack.assert_called_once_with()
        assert connections.is_connected("U0ADA")
        assert self.sent_provider()["is_connected"] is True
        assert self.home_block()["is_connected"] is True

    def test_disconnect_forgets_and_shows_the_connection(self):
        connections.connect("U0ADA")

        disconnect_callback(ack=self.ack, body=button_click("acme"), client=self.client)

        self.ack.assert_called_once_with()
        assert not connections.is_connected("U0ADA")
        assert self.sent_provider()["is_connected"] is False
        assert self.home_block()["is_connected"] is False

    def test_connect_ignores_another_provider(self):
        connect_callback(
            ack=self.ack, body=button_click("wile-e-coyote"), client=self.client
        )

        self.ack.assert_called_once_with()
        assert not connections.is_connected("U0ADA")
        assert self.client.mock_calls == []

    def test_disconnect_ignores_another_provider(self):
        connections.connect("U0ADA")

        disconnect_callback(
            ack=self.ack, body=button_click("wile-e-coyote"), client=self.client
        )

        self.ack.assert_called_once_with()
        assert connections.is_connected("U0ADA")
        assert self.client.mock_calls == []

    def test_user_connection_connect_opens_the_modal(self):
        event = {"subtype": "connect", "user": "U0ADA", "trigger_id": "123.456.abc"}

        user_connection_callback(client=self.client, event=event)

        kwargs = self.client.apps_user_connection_requestAuth.call_args.kwargs
        assert kwargs["trigger_id"] == "123.456.abc"
        assert kwargs["primary_provider"]["is_connected"] is False

    def test_user_connection_disconnect_is_ignored(self):
        event = {"subtype": "disconnect", "user": "U0ADA", "trigger_id": "123.456.abc"}

        user_connection_callback(client=self.client, event=event)

        assert self.client.mock_calls == []

    def test_status_requested_reports_connected_users(self):
        connections.connect("U0ADA")

        user_connection_status_requested_callback(
            client=self.client, event={"user": "U0ADA"}
        )

        self.client.apps_user_connection_update.assert_called_once_with(
            user_id="U0ADA", status="connected"
        )

    def test_status_requested_reports_unknown_users_as_disconnected(self):
        user_connection_status_requested_callback(
            client=self.client, event={"user": "U0ADA"}
        )

        self.client.apps_user_connection_update.assert_called_once_with(
            user_id="U0ADA", status="disconnected"
        )

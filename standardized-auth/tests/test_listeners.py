from unittest.mock import MagicMock

from slack_sdk import WebClient

from src.acme import provider
from src.connections import connections
from src.listeners import (
    app_home_opened_callback,
    connect_callback,
    disconnect_callback,
    user_connection_callback,
    user_connection_status_requested_callback,
)
from tests.helpers import TempStore, called_methods, expected_home, published_view


def user_connection(subtype: str) -> dict:
    return {
        "type": "user_connection",
        "subtype": subtype,
        "user": {"id": "U0ADA", "team_id": "T0001"},
        "trigger_id": "123.456.abc",
    }


class TestConnect:
    def setup_method(self):
        self.store = TempStore()
        self.client = MagicMock(spec=WebClient)

    def teardown_method(self):
        self.store.close()

    def test_connects_and_reports_the_user(self):
        ack = MagicMock()

        connect_callback(ack=ack, body={"user": {"id": "U0ADA"}}, client=self.client)

        ack.assert_called_once_with()
        assert connections.is_connected("U0ADA")
        assert called_methods(self.client) == [
            "apps_user_connection_requestAuth",
            "views_publish",
        ]
        self.client.apps_user_connection_requestAuth.assert_called_once_with(
            user_id="U0ADA", primary_provider=provider("U0ADA")
        )


class TestDisconnect:
    def setup_method(self):
        self.store = TempStore()
        self.client = MagicMock(spec=WebClient)

    def teardown_method(self):
        self.store.close()

    def test_forgets_then_reports_the_user(self):
        connections.connect("U0ADA")
        ack = MagicMock()

        disconnect_callback(ack=ack, body={"user": {"id": "U0ADA"}}, client=self.client)

        ack.assert_called_once_with()
        assert not connections.is_connected("U0ADA")
        assert called_methods(self.client) == [
            "apps_user_connection_requestAuth",
            "views_publish",
        ]
        self.client.apps_user_connection_requestAuth.assert_called_once_with(
            user_id="U0ADA", primary_provider=provider("U0ADA")
        )

    def test_disconnecting_without_an_account_still_reports_disconnected(self):
        disconnect_callback(
            ack=MagicMock(), body={"user": {"id": "U0ADA"}}, client=self.client
        )

        self.client.apps_user_connection_requestAuth.assert_called_once_with(
            user_id="U0ADA", primary_provider=provider("U0ADA")
        )


class TestUserConnection:
    def setup_method(self):
        self.store = TempStore()
        self.client = MagicMock(spec=WebClient)

    def teardown_method(self):
        self.store.close()

    def test_connect_opens_the_auth_modal(self):
        ack = MagicMock()

        user_connection_callback(
            ack=ack, body=user_connection("connect"), client=self.client
        )

        ack.assert_called_once_with()
        self.client.apps_user_connection_requestAuth.assert_called_once_with(
            trigger_id="123.456.abc", primary_provider=provider("U0ADA")
        )
        assert provider("U0ADA")["is_connected"] is False

    def test_connect_shows_an_existing_connection(self):
        connections.connect("U0ADA")

        user_connection_callback(
            ack=MagicMock(), body=user_connection("connect"), client=self.client
        )

        self.client.apps_user_connection_requestAuth.assert_called_once_with(
            trigger_id="123.456.abc", primary_provider=provider("U0ADA")
        )
        assert provider("U0ADA")["is_connected"] is True

    def test_disconnect_forgets_the_account(self):
        connections.connect("U0ADA")
        ack = MagicMock()

        user_connection_callback(
            ack=ack, body=user_connection("disconnect"), client=self.client
        )

        ack.assert_called_once_with()
        assert not connections.is_connected("U0ADA")

    def test_an_unknown_subtype_is_only_acknowledged(self):
        ack = MagicMock()

        user_connection_callback(
            ack=ack, body=user_connection("reconnect"), client=self.client
        )

        ack.assert_called_once_with()
        assert called_methods(self.client) == []


class TestAppHomeOpened:
    def setup_method(self):
        self.store = TempStore()
        self.client = MagicMock(spec=WebClient)

    def teardown_method(self):
        self.store.close()

    def test_shows_a_connected_account(self):
        connections.connect("U0ADA")

        app_home_opened_callback(client=self.client, event={"user": "U0ADA"})

        assert self.client.views_publish.call_args.kwargs["user_id"] == "U0ADA"
        assert published_view(self.client) == expected_home("U0ADA")

    def test_offers_to_connect_users_without_an_account(self):
        app_home_opened_callback(client=self.client, event={"user": "U0ADA"})

        assert published_view(self.client) == expected_home("U0ADA")


class TestUserConnectionStatusRequested:
    def setup_method(self):
        self.store = TempStore()
        self.client = MagicMock(spec=WebClient)

    def teardown_method(self):
        self.store.close()

    def test_reports_connected_users(self):
        connections.connect("U0ADA")

        user_connection_status_requested_callback(
            client=self.client, event={"user": "U0ADA"}
        )

        self.client.apps_user_connection_update.assert_called_once_with(
            user_id="U0ADA", status="connected"
        )

    def test_reports_users_without_an_account_as_disconnected(self):
        user_connection_status_requested_callback(
            client=self.client, event={"user": "U0ADA"}
        )

        self.client.apps_user_connection_update.assert_called_once_with(
            user_id="U0ADA", status="disconnected"
        )

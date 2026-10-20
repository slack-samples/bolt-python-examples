from unittest.mock import MagicMock

from slack_sdk import WebClient

from src.acme import provider
from src.connections import connections
from src.listeners.actions.user_connection import user_connection_callback
from tests.helpers import TempStore, called_methods


def user_connection(subtype: str) -> dict:
    return {
        "type": "user_connection",
        "subtype": subtype,
        "user": {"id": "U0ADA", "team_id": "T0001"},
        "trigger_id": "123.456.abc",
    }


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

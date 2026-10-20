from unittest.mock import MagicMock

from slack_sdk import WebClient

from src.connections import connections
from src.listeners.events.user_connection_status_requested import (
    user_connection_status_requested_callback,
)
from tests.helpers import TempStore


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

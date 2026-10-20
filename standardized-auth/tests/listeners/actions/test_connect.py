from unittest.mock import MagicMock

from slack_sdk import WebClient

from src.acme import provider
from src.connections import connections
from src.listeners.actions.connect import connect_callback
from tests.helpers import TempStore, called_methods


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

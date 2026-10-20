from unittest.mock import MagicMock

from slack_sdk import WebClient

from src.connections import connections
from src.listeners.events.app_home_opened import app_home_opened_callback
from tests.helpers import TempStore, expected_home, published_view


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

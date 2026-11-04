from src import connections
from src.acme import home_view, provider
from tests.helpers import TempConnections


class TestAcme:
    def setup_method(self):
        self.connections = TempConnections()

    def teardown_method(self):
        self.connections.close()

    def test_disconnected_provider_offers_to_connect(self):
        assert provider("U0ADA") == {
            "value": "acme",
            "name": {"type": "plain_text", "text": "Acme account"},
            "description": {
                "type": "plain_text",
                "text": "Order rocket skates, anvils, and giant magnets without leaving Slack.",
            },
            "is_connected": False,
        }

    def test_connected_provider_names_the_slack_user(self):
        connections.connect("U0ADA")

        acme = provider("U0ADA")

        assert acme["is_connected"] is True
        assert acme["connected_identity"] == {"type": "plain_text", "text": "U0ADA"}

    def test_home_view_renders_the_provider_as_an_auth_provider_block(self):
        acme = provider("U0ADA")

        view = home_view(acme).to_dict()

        assert view["type"] == "home"
        assert view["blocks"][-1] == {"type": "auth_provider", **acme}

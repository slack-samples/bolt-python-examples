from src import connections
from tests.helpers import TempConnections


class TestConnections:
    def setup_method(self):
        self.connections = TempConnections()

    def teardown_method(self):
        self.connections.close()

    def test_remembers_a_connected_user(self):
        connections.connect("U0ADA")

        assert connections.is_connected("U0ADA")

    def test_disconnect_forgets_the_user(self):
        connections.connect("U0ADA")

        connections.disconnect("U0ADA")

        assert not connections.is_connected("U0ADA")

    def test_disconnect_keeps_other_users_connected(self):
        connections.connect("U0ADA")
        connections.connect("U0BOB")

        connections.disconnect("U0ADA")

        assert connections.is_connected("U0BOB")

    def test_disconnecting_an_unknown_user_changes_nothing(self):
        connections.disconnect("U0ADA")

        assert not connections.is_connected("U0ADA")

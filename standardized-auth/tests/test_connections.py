from pathlib import Path
from tempfile import TemporaryDirectory

from src.connections import Connections


class TestConnections:
    def setup_method(self):
        self.dir = TemporaryDirectory()
        self.path = Path(self.dir.name) / "acme.db"
        self.connections = Connections(self.path)

    def teardown_method(self):
        self.dir.cleanup()

    def test_remembers_a_connected_user(self):
        self.connections.connect("U0ADA")

        assert self.connections.is_connected("U0ADA")

    def test_disconnect_forgets_the_user(self):
        self.connections.connect("U0ADA")

        self.connections.disconnect("U0ADA")

        assert not self.connections.is_connected("U0ADA")

    def test_disconnect_keeps_other_users_connected(self):
        self.connections.connect("U0ADA")
        self.connections.connect("U0BOB")

        self.connections.disconnect("U0ADA")

        assert self.connections.is_connected("U0BOB")

    def test_disconnecting_an_unknown_user_changes_nothing(self):
        self.connections.disconnect("U0ADA")

        assert not self.connections.is_connected("U0ADA")

    def test_connections_survive_a_restart(self):
        self.connections.connect("U0ADA")

        assert Connections(self.path).is_connected("U0ADA")

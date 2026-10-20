from src.connections import Connections


def test_remembers_a_connected_username(tmp_path):
    connections = Connections(tmp_path / "acme.db")

    connections.connect("U0ADA", "ada")

    assert connections.find("U0ADA") == "ada"


def test_reconnecting_replaces_the_username(tmp_path):
    connections = Connections(tmp_path / "acme.db")
    connections.connect("U0ADA", "ada")

    connections.connect("U0ADA", "countess")

    assert connections.find("U0ADA") == "countess"


def test_disconnect_forgets_the_user(tmp_path):
    connections = Connections(tmp_path / "acme.db")
    connections.connect("U0ADA", "ada")

    assert connections.disconnect("U0ADA") is True
    assert connections.find("U0ADA") is None


def test_disconnect_keeps_other_users_connected(tmp_path):
    connections = Connections(tmp_path / "acme.db")
    connections.connect("U0ADA", "ada")
    connections.connect("U0BOB", "bob")

    connections.disconnect("U0ADA")

    assert connections.find("U0BOB") == "bob"


def test_disconnecting_an_unknown_user_changes_nothing(tmp_path):
    connections = Connections(tmp_path / "acme.db")

    assert connections.disconnect("U0ADA") is False


def test_connections_survive_a_restart(tmp_path):
    Connections(tmp_path / "acme.db").connect("U0ADA", "ada")

    assert Connections(tmp_path / "acme.db").find("U0ADA") == "ada"

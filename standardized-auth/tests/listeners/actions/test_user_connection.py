from unittest.mock import MagicMock

from src.acme import provider
from src.listeners.actions.user_connection import user_connection_callback
from tests.helpers import called_methods


def user_connection(subtype: str) -> dict:
    return {
        "type": "user_connection",
        "subtype": subtype,
        "user": {"id": "U0ADA", "team_id": "T0001"},
        "trigger_id": "123.456.abc",
    }


def test_connect_opens_the_auth_modal(store, client):
    ack = MagicMock()

    user_connection_callback(ack=ack, body=user_connection("connect"), client=client)

    ack.assert_called_once_with()
    client.apps_user_connection_requestAuth.assert_called_once_with(
        trigger_id="123.456.abc", primary_provider=provider("U0ADA")
    )
    assert provider("U0ADA")["is_connected"] is False


def test_connect_shows_an_existing_connection(store, client):
    store.connect("U0ADA", "ada")

    user_connection_callback(
        ack=MagicMock(), body=user_connection("connect"), client=client
    )

    client.apps_user_connection_requestAuth.assert_called_once_with(
        trigger_id="123.456.abc", primary_provider=provider("U0ADA")
    )
    assert provider("U0ADA")["is_connected"] is True


def test_disconnect_forgets_the_account(store, client):
    store.connect("U0ADA", "ada")
    ack = MagicMock()

    user_connection_callback(ack=ack, body=user_connection("disconnect"), client=client)

    ack.assert_called_once_with()
    assert store.find("U0ADA") is None


def test_an_unknown_subtype_is_only_acknowledged(store, client):
    ack = MagicMock()

    user_connection_callback(ack=ack, body=user_connection("reconnect"), client=client)

    ack.assert_called_once_with()
    assert called_methods(client) == []

from unittest.mock import MagicMock

from src.acme import find_user_token
from src.listeners.actions.user_connection import user_connection_callback
from tests.helpers import called_methods, context, expected_provider, installation


def user_connection(subtype: str) -> dict:
    return {
        "type": "user_connection",
        "subtype": subtype,
        "user": {"id": "U0ADA", "team_id": "T0001"},
        "trigger_id": "123.456.abc",
    }


def test_connect_opens_the_auth_modal(store, client):
    ack = MagicMock()

    user_connection_callback(
        ack=ack, body=user_connection("connect"), client=client, context=context()
    )

    ack.assert_called_once_with()
    client.apps_user_connection_requestAuth.assert_called_once_with(
        trigger_id="123.456.abc", primary_provider=expected_provider()
    )


def test_connect_shows_an_existing_connection(store, client):
    store.save(installation("U0ADA", user_token="xoxp-test-ada"))

    user_connection_callback(
        ack=MagicMock(),
        body=user_connection("connect"),
        client=client,
        context=context(),
    )

    client.apps_user_connection_requestAuth.assert_called_once_with(
        trigger_id="123.456.abc", primary_provider=expected_provider("xoxp-test-ada")
    )


def test_disconnect_forgets_the_account(store, client):
    store.save(installation("U0ADA", user_token="xoxp-test-ada"))
    ack = MagicMock()

    user_connection_callback(
        ack=ack, body=user_connection("disconnect"), client=client, context=context()
    )

    ack.assert_called_once_with()
    assert find_user_token(context(), "U0ADA") is None
    client.auth_revoke.assert_called_once_with(token="xoxp-test-ada")


def test_an_unknown_subtype_is_only_acknowledged(store, client):
    ack = MagicMock()

    user_connection_callback(
        ack=ack, body=user_connection("reconnect"), client=client, context=context()
    )

    ack.assert_called_once_with()
    assert called_methods(client) == []

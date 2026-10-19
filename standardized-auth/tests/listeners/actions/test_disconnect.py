from unittest.mock import MagicMock

from src.acme import find_user_token
from src.listeners.actions.disconnect import disconnect_callback
from tests.helpers import called_methods, context, expected_provider, installation


def test_forgets_reports_then_revokes(store, client):
    store.save(installation("U0ADA", user_token="xoxp-test-ada"))
    ack = MagicMock()

    disconnect_callback(
        ack=ack, body={"user": {"id": "U0ADA"}}, client=client, context=context()
    )

    ack.assert_called_once_with()
    assert find_user_token(context(), "U0ADA") is None
    assert called_methods(client) == [
        "apps_user_connection_requestAuth",
        "views_publish",
        "auth_revoke",
    ]
    client.apps_user_connection_requestAuth.assert_called_once_with(
        user_id="U0ADA", primary_provider=expected_provider()
    )
    client.auth_revoke.assert_called_once_with(token="xoxp-test-ada")


def test_disconnecting_without_an_account_still_reports_disconnected(store, client):
    disconnect_callback(
        ack=MagicMock(),
        body={"user": {"id": "U0ADA"}},
        client=client,
        context=context(),
    )

    client.apps_user_connection_requestAuth.assert_called_once_with(
        user_id="U0ADA", primary_provider=expected_provider()
    )
    client.auth_revoke.assert_not_called()

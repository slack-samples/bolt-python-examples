from unittest.mock import MagicMock

from src.acme import provider
from src.listeners.actions.disconnect import disconnect_callback
from tests.helpers import called_methods


def test_forgets_then_reports_the_user(store, client):
    store.connect("U0ADA", "ada")
    ack = MagicMock()

    disconnect_callback(ack=ack, body={"user": {"id": "U0ADA"}}, client=client)

    ack.assert_called_once_with()
    assert store.find("U0ADA") is None
    assert called_methods(client) == [
        "apps_user_connection_requestAuth",
        "views_publish",
    ]
    client.apps_user_connection_requestAuth.assert_called_once_with(
        user_id="U0ADA", primary_provider=provider("U0ADA")
    )


def test_disconnecting_without_an_account_still_reports_disconnected(store, client):
    disconnect_callback(ack=MagicMock(), body={"user": {"id": "U0ADA"}}, client=client)

    client.apps_user_connection_requestAuth.assert_called_once_with(
        user_id="U0ADA", primary_provider=provider("U0ADA")
    )

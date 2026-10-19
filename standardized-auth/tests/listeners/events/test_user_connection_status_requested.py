from src.listeners.events.user_connection_status_requested import (
    user_connection_status_requested_callback,
)
from tests.helpers import context, installation


def test_reports_connected_users(store, client):
    store.save(installation("U0ADA", user_token="xoxp-test-ada"))

    user_connection_status_requested_callback(
        client=client, context=context(), event={"user": "U0ADA"}
    )

    client.apps_user_connection_update.assert_called_once_with(
        user_id="U0ADA", status="connected"
    )


def test_reports_users_without_an_account_as_disconnected(store, client):
    user_connection_status_requested_callback(
        client=client, context=context(), event={"user": "U0ADA"}
    )

    client.apps_user_connection_update.assert_called_once_with(
        user_id="U0ADA", status="disconnected"
    )

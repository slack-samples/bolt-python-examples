from src.listeners.events.app_home_opened import app_home_opened_callback
from tests.helpers import context, expected_home, installation, published_view


def test_shows_a_connected_account(store, client):
    store.save(installation("U0ADA", user_token="xoxp-test-ada"))

    app_home_opened_callback(client=client, context=context(), event={"user": "U0ADA"})

    assert client.views_publish.call_args.kwargs["user_id"] == "U0ADA"
    assert published_view(client) == expected_home("xoxp-test-ada")


def test_offers_to_connect_users_without_an_account(store, client):
    app_home_opened_callback(client=client, context=context(), event={"user": "U0ADA"})

    client.auth_test.assert_not_called()
    assert published_view(client) == expected_home()

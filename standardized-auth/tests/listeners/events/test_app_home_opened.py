from src.listeners.events.app_home_opened import app_home_opened_callback
from tests.helpers import expected_home, published_view


def test_shows_a_connected_account(store, client):
    store.connect("U0ADA", "ada")

    app_home_opened_callback(client=client, event={"user": "U0ADA"})

    assert client.views_publish.call_args.kwargs["user_id"] == "U0ADA"
    assert published_view(client) == expected_home("U0ADA")


def test_offers_to_connect_users_without_an_account(store, client):
    app_home_opened_callback(client=client, event={"user": "U0ADA"})

    assert published_view(client) == expected_home("U0ADA")

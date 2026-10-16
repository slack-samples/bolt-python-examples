from src.acme import (
    CONNECT_ACTION_ID,
    CONNECTED_GREETING,
    DISCONNECT_ACTION_ID,
    WELCOME_GREETING,
    Connection,
    acme_provider,
    home_view,
)

AUTH_URL = "https://acme.example/slack/install"


def test_action_ids_follow_the_provider_value():
    assert CONNECT_ACTION_ID == "auth_provider_connect_acme"
    assert DISCONNECT_ACTION_ID == "auth_provider_disconnect_acme"


def test_disconnected_provider_offers_the_acme_sign_in():
    assert acme_provider(AUTH_URL, None) == {
        "value": "acme",
        "name": {"type": "plain_text", "text": "Acme account"},
        "description": {
            "type": "plain_text",
            "text": "Order rocket skates, anvils, and giant magnets without leaving Slack.",
        },
        "auth_url": AUTH_URL,
        "is_connected": False,
    }


def test_connected_provider_names_the_connected_account():
    provider = acme_provider(AUTH_URL, Connection(identity="@ada", context="Acme Corp"))

    assert provider["is_connected"] is True
    assert provider["connected_identity"] == {"type": "plain_text", "text": "@ada"}
    assert provider["connected_context"] == {"type": "plain_text", "text": "Acme Corp"}


def test_home_view_renders_the_provider_as_an_auth_provider_block():
    provider = acme_provider(AUTH_URL, None)

    view = home_view(provider).to_dict()

    assert view["type"] == "home"
    assert view["blocks"][-1] == {"type": "auth_provider", **provider}


def test_home_view_welcomes_users_who_are_not_connected():
    view = home_view(acme_provider(AUTH_URL, None)).to_dict()

    assert view["blocks"][0]["text"]["text"] == WELCOME_GREETING


def test_home_view_celebrates_users_who_are_connected():
    connection = Connection(identity="@ada", context="Acme Corp")

    view = home_view(acme_provider(AUTH_URL, connection)).to_dict()

    assert view["blocks"][0]["text"]["text"] == CONNECTED_GREETING

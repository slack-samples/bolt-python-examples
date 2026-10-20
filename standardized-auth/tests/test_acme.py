from src.acme import home_view, provider
from src.state import issue


def test_disconnected_provider_offers_the_acme_sign_in(store):
    assert provider("U0ADA") == {
        "value": "acme",
        "name": {"type": "plain_text", "text": "Acme account"},
        "description": {
            "type": "plain_text",
            "text": "Order rocket skates, anvils, and giant magnets without leaving Slack.",
        },
        "auth_url": f"https://acme.example/acme/connect?state={issue('U0ADA')}",
        "is_connected": False,
    }


def test_connected_provider_names_the_acme_account(store):
    store.connect("U0ADA", "ada")

    acme = provider("U0ADA")

    assert acme["is_connected"] is True
    assert acme["connected_identity"] == {"type": "plain_text", "text": "ada"}


def test_home_view_renders_the_provider_as_an_auth_provider_block(store):
    acme = provider("U0ADA")

    view = home_view(acme).to_dict()

    assert view["type"] == "home"
    assert view["blocks"][-1] == {"type": "auth_provider", **acme}

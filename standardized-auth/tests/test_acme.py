from src.acme import find_user_token, forget, home_view, provider
from tests.helpers import context, installation


def org_wide_installation():
    return installation(
        "U0ADA",
        user_token="xoxp-test-ada",
        team_id=None,
        enterprise_id="E0001",
        is_enterprise_install=True,
    )


def org_context():
    return context(team_id="T0002", enterprise_id="E0001", is_enterprise_install=True)


def test_users_who_never_installed_have_no_token(store):
    assert find_user_token(context(), "U0ADA") is None


def test_installations_without_a_user_token_are_not_accounts(store):
    store.save(installation("U0ADA"))

    assert find_user_token(context(), "U0ADA") is None


def test_finds_the_token_of_a_user_who_connected(store):
    store.save(installation("U0ADA", user_token="xoxp-test-ada"))

    assert find_user_token(context(), "U0ADA") == "xoxp-test-ada"


def test_finds_org_wide_accounts_from_any_workspace_in_the_org(store):
    store.save(org_wide_installation())

    assert find_user_token(org_context(), "U0ADA") == "xoxp-test-ada"


def test_forget_returns_the_token_and_keeps_other_users_connected(store):
    store.save(installation("U0ADA", user_token="xoxp-test-ada"))
    store.save(installation("U0BOB", user_token="xoxp-test-bob"))

    assert forget(context(), "U0ADA") == "xoxp-test-ada"
    assert find_user_token(context(), "U0ADA") is None
    assert find_user_token(context(), "U0BOB") == "xoxp-test-bob"


def test_forgets_org_wide_accounts(store):
    store.save(org_wide_installation())

    assert forget(org_context(), "U0ADA") == "xoxp-test-ada"
    assert find_user_token(org_context(), "U0ADA") is None


def test_forgetting_a_user_without_an_account_returns_nothing(store):
    assert forget(context(), "U0ADA") is None


def test_disconnected_provider_offers_the_acme_sign_in(client):
    assert provider(client, None) == {
        "value": "acme",
        "name": {"type": "plain_text", "text": "Acme account"},
        "description": {
            "type": "plain_text",
            "text": "Order rocket skates, anvils, and giant magnets without leaving Slack.",
        },
        "auth_url": "https://acme.example/slack/install",
        "is_connected": False,
    }
    client.auth_test.assert_not_called()


def test_connected_provider_names_the_account_behind_the_token(client):
    acme = provider(client, "xoxp-test-ada")

    client.auth_test.assert_called_once_with(token="xoxp-test-ada")
    assert acme["is_connected"] is True
    assert acme["connected_identity"] == {"type": "plain_text", "text": "@ada"}
    assert acme["connected_context"] == {"type": "plain_text", "text": "Acme Corp"}


def test_home_view_renders_the_provider_as_an_auth_provider_block(client):
    acme = provider(client, None)

    view = home_view(acme).to_dict()

    assert view["type"] == "home"
    assert view["blocks"][-1] == {"type": "auth_provider", **acme}

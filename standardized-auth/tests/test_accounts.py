from src.accounts import AcmeAccounts
from tests.helpers import context, installation


def test_users_who_never_installed_have_no_account(store):
    assert AcmeAccounts(store).find(context(), "U0ADA") is None


def test_installations_without_a_user_token_are_not_accounts(store):
    store.save(installation("U0ADA"))

    assert AcmeAccounts(store).find(context(), "U0ADA") is None


def test_finds_the_account_of_a_user_who_connected(store):
    store.save(installation("U0ADA", user_token="xoxp-test-ada"))

    account = AcmeAccounts(store).find(context(), "U0ADA")

    assert account is not None
    assert account.user_token == "xoxp-test-ada"


def test_finds_org_wide_accounts_from_any_workspace_in_the_org(store):
    store.save(
        installation(
            "U0ADA",
            user_token="xoxp-test-ada",
            team_id=None,
            enterprise_id="E0001",
            is_enterprise_install=True,
        )
    )
    org_context = context(
        team_id="T0002", enterprise_id="E0001", is_enterprise_install=True
    )

    assert AcmeAccounts(store).find(org_context, "U0ADA") is not None


def test_forget_returns_the_token_and_keeps_other_users_connected(store):
    store.save(installation("U0ADA", user_token="xoxp-test-ada"))
    store.save(installation("U0BOB", user_token="xoxp-test-bob"))
    accounts = AcmeAccounts(store)

    assert accounts.forget(context(), "U0ADA") == "xoxp-test-ada"
    assert accounts.find(context(), "U0ADA") is None
    assert accounts.find(context(), "U0BOB") is not None


def test_forgets_org_wide_accounts(store):
    store.save(
        installation(
            "U0ADA",
            user_token="xoxp-test-ada",
            team_id=None,
            enterprise_id="E0001",
            is_enterprise_install=True,
        )
    )
    org_context = context(
        team_id="T0002", enterprise_id="E0001", is_enterprise_install=True
    )
    accounts = AcmeAccounts(store)

    assert accounts.forget(org_context, "U0ADA") == "xoxp-test-ada"
    assert accounts.find(org_context, "U0ADA") is None


def test_forgetting_a_user_without_an_account_returns_nothing(store):
    assert AcmeAccounts(store).forget(context(), "U0ADA") is None

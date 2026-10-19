from src.acme import find_user_token
from src.listeners.events.tokens_revoked import tokens_revoked_callback
from tests.helpers import called_methods, context, installation


def test_forgets_revoked_users_and_reports_them_disconnected(store, client):
    store.save(installation("U0ADA", user_token="xoxp-test-ada"))

    tokens_revoked_callback(
        client=client, context=context(), event={"tokens": {"oauth": ["U0ADA"]}}
    )

    assert find_user_token(context(), "U0ADA") is None
    assert called_methods(client) == [
        "apps_user_connection_requestAuth",
        "views_publish",
    ]


def test_ignores_revoked_bot_tokens(store, client):
    tokens_revoked_callback(
        client=client, context=context(), event={"tokens": {"bot": ["U0BOT"]}}
    )

    assert called_methods(client) == []

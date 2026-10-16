from unittest.mock import MagicMock, patch

import pytest
from slack_bolt.oauth.callback_options import SuccessArgs
from slack_sdk import WebClient

from src.accounts import AcmeAccounts
from src.acme import Connection, acme_provider, home_view
from src.listeners import AcmeListeners
from tests.helpers import context, installation

AUTH_URL = "https://acme.example/slack/install"
ADA = Connection(identity="@ada", context="Acme Corp")


@pytest.fixture
def client() -> MagicMock:
    client = MagicMock(spec=WebClient)
    client.auth_test.return_value = {"ok": True, "user": "ada", "team": "Acme Corp"}
    return client


@pytest.fixture
def listeners(store) -> AcmeListeners:
    return AcmeListeners(AcmeAccounts(store), AUTH_URL)


def published_view(client: MagicMock) -> dict:
    return client.views_publish.call_args.kwargs["view"].to_dict()


def called_methods(client: MagicMock) -> list:
    return [name for name, _, _ in client.mock_calls]


def user_connection(subtype: str) -> dict:
    return {
        "type": "user_connection",
        "subtype": subtype,
        "user": {"id": "U0ADA", "team_id": "T0001"},
        "trigger_id": "123.456.abc",
    }


def test_report_connected_records_the_connection_then_shows_the_success_page(
    listeners, client
):
    args = SuccessArgs(
        request=MagicMock(),
        installation=installation("U0ADA", user_token="xoxp-test-ada"),
        settings=MagicMock(),
        default=MagicMock(),
    )

    with patch("src.listeners.WebClient", return_value=client) as client_class:
        response = listeners.report_connected(args)

    client_class.assert_called_once_with(token="xoxb-test-bot")
    client.auth_test.assert_called_once_with(token="xoxp-test-ada")
    client.apps_user_connection_requestAuth.assert_called_once_with(
        user_id="U0ADA", primary_provider=acme_provider(AUTH_URL, ADA)
    )
    assert published_view(client) == home_view(acme_provider(AUTH_URL, ADA)).to_dict()
    args.default.success.assert_called_once_with(args)
    assert response == args.default.success.return_value


def test_publish_home_shows_a_connected_account(store, listeners, client):
    store.save(installation("U0ADA", user_token="xoxp-test-ada"))

    listeners.publish_home(client=client, context=context(), event={"user": "U0ADA"})

    assert client.views_publish.call_args.kwargs["user_id"] == "U0ADA"
    assert published_view(client) == home_view(acme_provider(AUTH_URL, ADA)).to_dict()


def test_publish_home_offers_to_connect_users_without_an_account(listeners, client):
    listeners.publish_home(client=client, context=context(), event={"user": "U0ADA"})

    client.auth_test.assert_not_called()
    assert published_view(client) == home_view(acme_provider(AUTH_URL, None)).to_dict()


def test_acknowledge_connect_leaves_the_sign_in_to_the_auth_url(listeners):
    ack = MagicMock()

    listeners.acknowledge_connect(ack=ack)

    ack.assert_called_once_with()


def test_acknowledge_disconnect_forgets_reports_then_revokes(store, listeners, client):
    store.save(installation("U0ADA", user_token="xoxp-test-ada"))
    ack = MagicMock()

    listeners.acknowledge_disconnect(
        ack=ack, body={"user": {"id": "U0ADA"}}, client=client, context=context()
    )

    ack.assert_called_once_with()
    assert AcmeAccounts(store).find(context(), "U0ADA") is None
    assert called_methods(client) == [
        "apps_user_connection_requestAuth",
        "views_publish",
        "auth_revoke",
    ]
    client.apps_user_connection_requestAuth.assert_called_once_with(
        user_id="U0ADA", primary_provider=acme_provider(AUTH_URL, None)
    )
    client.auth_revoke.assert_called_once_with(token="xoxp-test-ada")


def test_disconnecting_without_an_account_still_reports_disconnected(listeners, client):
    listeners.acknowledge_disconnect(
        ack=MagicMock(),
        body={"user": {"id": "U0ADA"}},
        client=client,
        context=context(),
    )

    client.apps_user_connection_requestAuth.assert_called_once_with(
        user_id="U0ADA", primary_provider=acme_provider(AUTH_URL, None)
    )
    client.auth_revoke.assert_not_called()


def test_answer_status_request_reports_connected_users(store, listeners, client):
    store.save(installation("U0ADA", user_token="xoxp-test-ada"))

    listeners.answer_status_request(
        client=client, context=context(), event={"user": "U0ADA"}
    )

    client.apps_user_connection_update.assert_called_once_with(
        user_id="U0ADA", status="connected"
    )


def test_answer_status_request_reports_users_without_an_account_as_disconnected(
    listeners, client
):
    listeners.answer_status_request(
        client=client, context=context(), event={"user": "U0ADA"}
    )

    client.apps_user_connection_update.assert_called_once_with(
        user_id="U0ADA", status="disconnected"
    )


def test_forget_revoked_users_reports_them_disconnected(store, listeners, client):
    store.save(installation("U0ADA", user_token="xoxp-test-ada"))

    listeners.forget_revoked_users(
        client=client, context=context(), event={"tokens": {"oauth": ["U0ADA"]}}
    )

    assert AcmeAccounts(store).find(context(), "U0ADA") is None
    assert called_methods(client) == [
        "apps_user_connection_requestAuth",
        "views_publish",
    ]


def test_forget_revoked_users_ignores_revoked_bot_tokens(listeners, client):
    listeners.forget_revoked_users(
        client=client, context=context(), event={"tokens": {"bot": ["U0BOT"]}}
    )

    assert called_methods(client) == []


def test_user_connection_connect_opens_the_auth_modal(listeners, client):
    ack = MagicMock()

    listeners.handle_user_connection(
        ack=ack, body=user_connection("connect"), client=client, context=context()
    )

    ack.assert_called_once_with()
    client.apps_user_connection_requestAuth.assert_called_once_with(
        trigger_id="123.456.abc", primary_provider=acme_provider(AUTH_URL, None)
    )


def test_user_connection_connect_shows_an_existing_connection(store, listeners, client):
    store.save(installation("U0ADA", user_token="xoxp-test-ada"))

    listeners.handle_user_connection(
        ack=MagicMock(),
        body=user_connection("connect"),
        client=client,
        context=context(),
    )

    client.apps_user_connection_requestAuth.assert_called_once_with(
        trigger_id="123.456.abc", primary_provider=acme_provider(AUTH_URL, ADA)
    )


def test_user_connection_disconnect_forgets_the_account(store, listeners, client):
    store.save(installation("U0ADA", user_token="xoxp-test-ada"))
    ack = MagicMock()

    listeners.handle_user_connection(
        ack=ack, body=user_connection("disconnect"), client=client, context=context()
    )

    ack.assert_called_once_with()
    assert AcmeAccounts(store).find(context(), "U0ADA") is None
    client.auth_revoke.assert_called_once_with(token="xoxp-test-ada")


def test_user_connection_with_an_unknown_subtype_is_only_acknowledged(
    listeners, client
):
    ack = MagicMock()

    listeners.handle_user_connection(
        ack=ack, body=user_connection("reconnect"), client=client, context=context()
    )

    ack.assert_called_once_with()
    assert called_methods(client) == []

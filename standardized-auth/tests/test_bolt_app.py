from unittest.mock import MagicMock, patch

from slack_bolt.oauth.callback_options import SuccessArgs
from slack_sdk.oauth.installation_store import Installation

from src.bolt_app import success_callback
from tests.helpers import expected_home, expected_provider, installation, published_view


def success_args(connected: Installation) -> SuccessArgs:
    return SuccessArgs(
        request=MagicMock(),
        installation=connected,
        settings=MagicMock(),
        default=MagicMock(),
    )


def test_reports_the_connection_then_returns_to_app_home(client):
    args = success_args(installation("U0ADA", user_token="xoxp-test-ada"))

    with patch("src.bolt_app.WebClient", return_value=client) as client_class:
        response = success_callback(args)

    client_class.assert_called_once_with(token="xoxb-test-bot")
    client.auth_test.assert_called_once_with(token="xoxp-test-ada")
    client.apps_user_connection_requestAuth.assert_called_once_with(
        user_id="U0ADA", primary_provider=expected_provider("xoxp-test-ada")
    )
    assert published_view(client) == expected_home("xoxp-test-ada")
    assert response.status == 302
    assert response.headers["location"] == ["slack://app?team=T0001&id=A0001&tab=home"]


def test_org_wide_connections_return_to_app_home_in_the_org(client):
    args = success_args(
        installation(
            "U0ADA",
            user_token="xoxp-test-ada",
            team_id=None,
            enterprise_id="E0001",
            is_enterprise_install=True,
        )
    )

    with patch("src.bolt_app.WebClient", return_value=client):
        response = success_callback(args)

    assert response.headers["location"] == ["slack://app?team=E0001&id=A0001&tab=home"]

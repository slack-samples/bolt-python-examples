from unittest.mock import MagicMock, patch

from slack_bolt.oauth.callback_options import SuccessArgs

from src.listeners.oauth.success import success_callback
from tests.helpers import expected_home, expected_provider, installation, published_view


def test_reports_the_connection_then_shows_the_success_page(client):
    args = SuccessArgs(
        request=MagicMock(),
        installation=installation("U0ADA", user_token="xoxp-test-ada"),
        settings=MagicMock(),
        default=MagicMock(),
    )

    with patch(
        "src.listeners.oauth.success.WebClient", return_value=client
    ) as client_class:
        response = success_callback(args)

    client_class.assert_called_once_with(token="xoxb-test-bot")
    client.auth_test.assert_called_once_with(token="xoxp-test-ada")
    client.apps_user_connection_requestAuth.assert_called_once_with(
        user_id="U0ADA", primary_provider=expected_provider("xoxp-test-ada")
    )
    assert published_view(client) == expected_home("xoxp-test-ada")
    args.default.success.assert_called_once_with(args)
    assert response == args.default.success.return_value

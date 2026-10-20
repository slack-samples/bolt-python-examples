from unittest.mock import MagicMock

from src.acme import home_view, provider


def published_view(client: MagicMock) -> dict:
    return client.views_publish.call_args.kwargs["view"].to_dict()


def called_methods(client: MagicMock) -> list:
    return [name for name, _, _ in client.mock_calls]


def expected_home(user_id: str) -> dict:
    return home_view(provider(user_id)).to_dict()

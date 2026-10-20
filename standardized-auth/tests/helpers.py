from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import MagicMock

from src.acme import home_view, provider
from src.connections import connections


class TempStore:
    def __init__(self):
        self.saved_path = connections.path
        self.dir = TemporaryDirectory()
        connections.path = Path(self.dir.name) / "acme.db"

    def close(self):
        connections.path = self.saved_path
        self.dir.cleanup()


def published_view(client: MagicMock) -> dict:
    return client.views_publish.call_args.kwargs["view"].to_dict()


def called_methods(client: MagicMock) -> list:
    return [name for name, _, _ in client.mock_calls]


def expected_home(user_id: str) -> dict:
    return home_view(provider(user_id)).to_dict()

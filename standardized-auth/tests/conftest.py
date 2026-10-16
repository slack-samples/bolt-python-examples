import pytest
from slack_sdk.oauth.installation_store import FileInstallationStore


@pytest.fixture
def store(tmp_path) -> FileInstallationStore:
    return FileInstallationStore(base_dir=str(tmp_path / "installations"))

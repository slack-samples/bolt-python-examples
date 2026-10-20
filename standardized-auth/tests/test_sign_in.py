from collections.abc import Iterator
from threading import Thread
from unittest.mock import MagicMock
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen

import pytest

from src.sign_in import SignInServer
from src.state import issue
from tests.helpers import called_methods


@pytest.fixture
def base_url(client) -> Iterator[str]:
    server = SignInServer(0, client)
    Thread(target=server.serve_forever, daemon=True).start()
    yield f"http://localhost:{server.server_port}"
    server.shutdown()
    server.server_close()


def get(url: str) -> str:
    with urlopen(url) as response:
        return response.read().decode()


def post(url: str, form: dict) -> str:
    with urlopen(url, data=urlencode(form).encode()) as response:
        return response.read().decode()


def status_of(error: pytest.ExceptionInfo[HTTPError]) -> int:
    return error.value.code


def test_shows_the_sign_in_form(store, base_url):
    state = issue("U0ADA")

    page = get(f"{base_url}/acme/connect?state={state}")

    assert "Sign in to Acme" in page
    assert f'value="{state}"' in page


def test_signing_in_connects_and_reports_the_user(store, base_url, client: MagicMock):
    page = post(
        f"{base_url}/acme/connect", {"state": issue("U0ADA"), "username": "ada"}
    )

    assert "Connected to Acme" in page
    assert store.find("U0ADA") == "ada"
    assert called_methods(client) == [
        "apps_user_connection_requestAuth",
        "views_publish",
    ]


def test_signing_in_with_a_forged_state_connects_nobody(
    store, base_url, client: MagicMock
):
    with pytest.raises(HTTPError) as error:
        post(f"{base_url}/acme/connect", {"state": "U0ADA.forged", "username": "ada"})

    assert status_of(error) == 400
    assert store.find("U0ADA") is None
    assert called_methods(client) == []


def test_signing_in_requires_a_username(store, base_url, client: MagicMock):
    with pytest.raises(HTTPError) as error:
        post(f"{base_url}/acme/connect", {"state": issue("U0ADA"), "username": " "})

    assert status_of(error) == 400
    assert store.find("U0ADA") is None


def test_other_paths_are_not_found(base_url):
    with pytest.raises(HTTPError) as error:
        get(f"{base_url}/slack/events")

    assert status_of(error) == 404

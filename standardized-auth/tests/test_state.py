import time

from src.state import issue, redeem


def test_redeems_the_user_it_was_issued_for():
    assert redeem(issue("U0ADA")) == "U0ADA"


def test_rejects_a_state_issued_for_someone_else():
    token, _, _ = issue("U0ADA").rpartition(".")

    assert redeem(f"{token}.U0EVE") is None


def test_rejects_a_state_without_a_signature():
    assert redeem("U0ADA") is None


def test_rejects_a_non_ascii_signature():
    assert redeem("U0ADA.é") is None


def test_rejects_an_expired_state(monkeypatch):
    state = issue("U0ADA")
    later = time.time() + 301
    monkeypatch.setattr(time, "time", lambda: later)

    assert redeem(state) is None

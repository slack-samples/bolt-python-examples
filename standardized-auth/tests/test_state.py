from src.state import issue, redeem


def test_redeems_the_user_it_was_issued_for():
    assert redeem(issue("U0ADA")) == "U0ADA"


def test_rejects_a_state_issued_for_someone_else():
    _, _, signature = issue("U0ADA").partition(".")

    assert redeem(f"U0EVE.{signature}") is None


def test_rejects_a_state_without_a_signature():
    assert redeem("U0ADA") is None


def test_rejects_a_non_ascii_signature():
    assert redeem("U0ADA.é") is None

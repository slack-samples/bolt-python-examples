from unittest.mock import MagicMock

from src.listeners.actions.connect import connect_callback


def test_leaves_the_sign_in_to_the_auth_url():
    ack = MagicMock()

    connect_callback(ack=ack)

    ack.assert_called_once_with()

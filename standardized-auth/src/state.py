import secrets

from slack_sdk.oauth.state_store import StatelessOAuthStateStore

key = secrets.token_hex(32)


def store_for(user_id: str) -> StatelessOAuthStateStore:
    return StatelessOAuthStateStore(
        expiration_seconds=300, signing_secret=key + user_id
    )


def issue(user_id: str) -> str:
    return f"{store_for(user_id).issue()}.{user_id}"


def redeem(state: str) -> str | None:
    token, _, user_id = state.rpartition(".")
    return user_id if store_for(user_id).consume(token) else None

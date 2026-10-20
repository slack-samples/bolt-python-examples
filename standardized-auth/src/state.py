import hmac
import secrets
from hashlib import sha256

key = secrets.token_bytes(32)


def sign(user_id: str) -> str:
    return hmac.new(key, user_id.encode(), sha256).hexdigest()


def issue(user_id: str) -> str:
    return f"{user_id}.{sign(user_id)}"


def redeem(state: str) -> str | None:
    user_id, _, signature = state.partition(".")
    if hmac.compare_digest(signature.encode(), sign(user_id).encode()):
        return user_id
    return None

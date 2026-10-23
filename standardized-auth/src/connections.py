import shelve

FILENAME = "acme.db"


def connect(user_id: str) -> None:
    with shelve.open(FILENAME) as db:
        db[user_id] = True


def disconnect(user_id: str) -> None:
    with shelve.open(FILENAME) as db:
        db.pop(user_id, None)


def is_connected(user_id: str) -> bool:
    with shelve.open(FILENAME) as db:
        return user_id in db

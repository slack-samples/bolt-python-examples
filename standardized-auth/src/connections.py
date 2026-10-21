import shelve
from pathlib import Path


class Connections:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def connect(self, user_id: str) -> None:
        with shelve.open(str(self.path)) as db:
            db[user_id] = True

    def disconnect(self, user_id: str) -> None:
        with shelve.open(str(self.path)) as db:
            db.pop(user_id, None)

    def is_connected(self, user_id: str) -> bool:
        with shelve.open(str(self.path)) as db:
            return user_id in db


connections = Connections(Path("data/acme.db"))

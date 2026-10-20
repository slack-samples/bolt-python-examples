import shelve
from pathlib import Path


class Connections:
    def __init__(self, path: Path):
        self.path = path

    def connect(self, user_id: str) -> None:
        with self._open() as db:
            db[user_id] = True

    def disconnect(self, user_id: str) -> None:
        with self._open() as db:
            db.pop(user_id, None)

    def is_connected(self, user_id: str) -> bool:
        with self._open() as db:
            return user_id in db

    def _open(self) -> shelve.Shelf[bool]:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        return shelve.open(str(self.path))


connections = Connections(Path("data/acme.db"))

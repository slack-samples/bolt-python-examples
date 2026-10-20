import shelve
from pathlib import Path


class Connections:
    def __init__(self, path: Path):
        self.path = path

    def connect(self, user_id: str, username: str) -> None:
        with self._open() as db:
            db[user_id] = username

    def disconnect(self, user_id: str) -> None:
        with self._open() as db:
            db.pop(user_id, None)

    def find(self, user_id: str) -> str | None:
        with self._open() as db:
            return db.get(user_id)

    def _open(self) -> shelve.Shelf[str]:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        return shelve.open(str(self.path))


connections = Connections(Path("data/acme.db"))

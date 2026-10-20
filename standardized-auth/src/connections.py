import sqlite3
from contextlib import closing
from pathlib import Path


class Connections:
    def __init__(self, path: Path):
        self.path = path

    def connect(self, user_id: str, username: str) -> None:
        self._write(
            "INSERT OR REPLACE INTO connections (user_id, username) VALUES (?, ?)",
            (user_id, username),
        )

    def disconnect(self, user_id: str) -> bool:
        return self._write("DELETE FROM connections WHERE user_id = ?", (user_id,)) > 0

    def find(self, user_id: str) -> str | None:
        with closing(self._open()) as db:
            row = db.execute(
                "SELECT username FROM connections WHERE user_id = ?", (user_id,)
            ).fetchone()
        return None if row is None else row[0]

    def _write(self, sql: str, parameters: tuple[str, ...]) -> int:
        with closing(self._open()) as db, db:
            return db.execute(sql, parameters).rowcount

    def _open(self) -> sqlite3.Connection:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        db = sqlite3.connect(self.path)
        db.execute(
            "CREATE TABLE IF NOT EXISTS connections"
            " (user_id TEXT PRIMARY KEY, username TEXT NOT NULL)"
        )
        return db


connections = Connections(Path("data/acme.db"))

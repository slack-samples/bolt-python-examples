from tempfile import TemporaryDirectory
from unittest.mock import patch


class TempConnections:
    def __init__(self):
        self.dir = TemporaryDirectory()
        self.filename = patch("src.connections.FILENAME", f"{self.dir.name}/acme.db")
        self.filename.start()

    def close(self):
        self.filename.stop()
        self.dir.cleanup()

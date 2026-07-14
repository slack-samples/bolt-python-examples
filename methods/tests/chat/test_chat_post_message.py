import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from slack_sdk import WebClient

from src.chat import chat_post_message


class _CapturingHandler(BaseHTTPRequestHandler):
    captured: dict = {}

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        _CapturingHandler.captured = {
            "path": self.path,
            "body": self.rfile.read(length).decode(),
        }
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"ok": true}')

    def log_message(self, *args):
        pass


def test_example01():
    server = HTTPServer(("127.0.0.1", 0), _CapturingHandler)
    port = server.server_address[1]
    threading.Thread(target=server.handle_request, daemon=True).start()

    client = WebClient(token="xoxb-test", base_url=f"http://127.0.0.1:{port}/api/")
    response = chat_post_message.example01(client)

    assert response["ok"] is True

    captured = _CapturingHandler.captured
    assert captured["path"] == "/api/chat.postMessage"
    assert json.loads(captured["body"]) == {
        "channel": "C123ABC456",
        "text": "Here's a message for you",
    }

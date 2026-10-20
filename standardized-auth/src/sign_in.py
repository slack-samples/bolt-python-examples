from html import escape
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import cast
from urllib.parse import parse_qs, urlsplit

from slack_sdk import WebClient

from src.acme import CONNECT_PATH, connect
from src.state import redeem

CONNECTED_PAGE = """<!doctype html>
<title>Connected to Acme</title>
<h1>Connected to Acme</h1>
<p>You can close this tab and return to Slack.</p>
"""


def sign_in_page(state: str) -> str:
    return f"""<!doctype html>
<title>Sign in to Acme</title>
<h1>Sign in to Acme</h1>
<form method="post" action="{CONNECT_PATH}">
  <input type="hidden" name="state" value="{escape(state)}">
  <label>Username <input name="username" required autofocus></label>
  <button>Sign in</button>
</form>
"""


def field(fields: dict[str, list[str]], name: str) -> str:
    return fields.get(name, [""])[0]


class SignInServer(ThreadingHTTPServer):
    def __init__(self, port: int, client: WebClient):
        super().__init__(("", port), SignInHandler)
        self.client = client


class SignInHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlsplit(self.path)
        if url.path != CONNECT_PATH:
            return self.send_error(HTTPStatus.NOT_FOUND)
        self.send_page(sign_in_page(field(parse_qs(url.query), "state")))

    def do_POST(self):
        if self.path != CONNECT_PATH:
            return self.send_error(HTTPStatus.NOT_FOUND)
        form = self.read_form()
        user_id = redeem(field(form, "state"))
        username = field(form, "username").strip()
        if user_id is None or not username:
            return self.send_error(HTTPStatus.BAD_REQUEST)
        connect(cast(SignInServer, self.server).client, user_id, username)
        self.send_page(CONNECTED_PAGE)

    def read_form(self) -> dict[str, list[str]]:
        length = int(self.headers.get("Content-Length", 0))
        return parse_qs(self.rfile.read(length).decode())

    def send_page(self, html: str):
        body = html.encode()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

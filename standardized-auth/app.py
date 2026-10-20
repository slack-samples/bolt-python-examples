import os
from threading import Thread

from slack_bolt.adapter.socket_mode import SocketModeHandler

from src.bolt_app import app
from src.sign_in import SignInServer

if __name__ == "__main__":
    sign_in = SignInServer(int(os.environ.get("PORT", "3000")), app.client)
    Thread(target=sign_in.serve_forever, daemon=True).start()
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

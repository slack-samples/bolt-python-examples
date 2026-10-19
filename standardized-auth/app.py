import os

from src.app import build_app

if __name__ == "__main__":
    build_app().start(port=int(os.environ.get("PORT", "3000")))

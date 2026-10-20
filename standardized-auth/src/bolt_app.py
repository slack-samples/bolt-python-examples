import os
from importlib import import_module
from pkgutil import walk_packages

from slack_bolt import App

from src import listeners

app = App(token=os.environ["SLACK_BOT_TOKEN"])


def load_listeners() -> None:
    for module_info in walk_packages(listeners.__path__, f"{listeners.__name__}."):
        import_module(module_info.name)


load_listeners()

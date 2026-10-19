from slack_bolt import App

from src.listeners import actions, events


def register_listeners(app: App):
    actions.register(app)
    events.register(app)

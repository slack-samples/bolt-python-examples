from slack_bolt import Ack


def connect_callback(ack: Ack):
    ack()

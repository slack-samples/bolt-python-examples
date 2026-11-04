import os
from unittest.mock import patch

os.environ["SLACK_BOT_TOKEN"] = "xoxb-test-bot"

patch("slack_sdk.WebClient.auth_test").start()

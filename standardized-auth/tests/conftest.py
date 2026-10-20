import os
from unittest.mock import patch

from slack_sdk.web import SlackResponse

os.environ["SLACK_BOT_TOKEN"] = "xoxb-test-bot"

patch(
    "slack_sdk.web.client.WebClient.auth_test",
    return_value=SlackResponse(
        client=None,
        http_verb="POST",
        api_url="https://slack.com/api/auth.test",
        req_args={},
        data={"ok": True, "team_id": "T0001", "bot_id": "B0001", "user_id": "U0BOT"},
        headers={},
        status_code=200,
    ),
).start()

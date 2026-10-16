from slack_bolt import BoltContext
from slack_sdk.oauth.installation_store import Installation


def installation(
    user_id: str,
    user_token: str | None = None,
    team_id: str | None = "T0001",
    enterprise_id: str | None = None,
    is_enterprise_install: bool = False,
) -> Installation:
    return Installation(
        app_id="A0001",
        enterprise_id=enterprise_id,
        team_id=team_id,
        user_id=user_id,
        user_token=user_token,
        bot_token="xoxb-test-bot",
        bot_id="B0001",
        bot_user_id="U0BOT",
        is_enterprise_install=is_enterprise_install,
    )


def context(
    team_id: str | None = "T0001",
    enterprise_id: str | None = None,
    is_enterprise_install: bool = False,
) -> BoltContext:
    return BoltContext(
        {
            "team_id": team_id,
            "enterprise_id": enterprise_id,
            "is_enterprise_install": is_enterprise_install,
        }
    )

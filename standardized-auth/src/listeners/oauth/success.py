from slack_bolt import BoltResponse
from slack_bolt.oauth.callback_options import SuccessArgs
from slack_sdk import WebClient

from src.acme import report


def success_callback(args: SuccessArgs) -> BoltResponse:
    installation = args.installation
    client = WebClient(token=installation.bot_token)
    report(client, installation.user_id, installation.user_token)
    return args.default.success(args)

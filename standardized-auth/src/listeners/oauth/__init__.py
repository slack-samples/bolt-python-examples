from slack_bolt import BoltResponse
from slack_bolt.oauth.callback_options import CallbackOptions, FailureArgs

from .success import success_callback


def failure_callback(args: FailureArgs) -> BoltResponse:
    return args.default.failure(args)


callback_options = CallbackOptions(success=success_callback, failure=failure_callback)

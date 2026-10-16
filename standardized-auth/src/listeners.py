from slack_bolt import Ack, BoltContext, BoltResponse
from slack_bolt.oauth.callback_options import SuccessArgs
from slack_sdk import WebClient
from slack_sdk.oauth.installation_store import Installation

from src.accounts import AcmeAccounts
from src.acme import Connection, acme_provider, home_view


def connection_of(client: WebClient, account: Installation | None) -> Connection | None:
    if account is None:
        return None
    identity = client.auth_test(token=account.user_token)
    return Connection(identity=f"@{identity['user']}", context=identity["team"])


class AcmeListeners:
    def __init__(self, accounts: AcmeAccounts, auth_url: str):
        self.accounts = accounts
        self.auth_url = auth_url

    def report_connected(self, args: SuccessArgs) -> BoltResponse:
        account = args.installation
        client = WebClient(token=account.bot_token)
        self.report(client, account.user_id, connection_of(client, account))
        return args.default.success(args)

    def publish_home(self, client: WebClient, context: BoltContext, event: dict):
        account = self.accounts.find(context, event["user"])
        provider = acme_provider(self.auth_url, connection_of(client, account))
        client.views_publish(user_id=event["user"], view=home_view(provider))

    def acknowledge_connect(self, ack: Ack):
        ack()

    def acknowledge_disconnect(
        self, ack: Ack, body: dict, client: WebClient, context: BoltContext
    ):
        ack()
        self.disconnect(client, context, body["user"]["id"])

    def answer_status_request(
        self, client: WebClient, context: BoltContext, event: dict
    ):
        account = self.accounts.find(context, event["user"])
        status = "disconnected" if account is None else "connected"
        client.apps_user_connection_update(user_id=event["user"], status=status)

    def forget_revoked_users(
        self, client: WebClient, context: BoltContext, event: dict
    ):
        for user_id in event["tokens"].get("oauth", []):
            self.accounts.forget(context, user_id)
            self.report(client, user_id, None)

    def handle_user_connection(
        self, ack: Ack, body: dict, client: WebClient, context: BoltContext
    ):
        ack()
        user_id = body["user"]["id"]
        if body["subtype"] == "connect":
            self.open_connect_modal(client, context, user_id, body["trigger_id"])
        elif body["subtype"] == "disconnect":
            self.disconnect(client, context, user_id)

    def open_connect_modal(
        self, client: WebClient, context: BoltContext, user_id: str, trigger_id: str
    ):
        account = self.accounts.find(context, user_id)
        client.apps_user_connection_requestAuth(
            trigger_id=trigger_id,
            primary_provider=acme_provider(
                self.auth_url, connection_of(client, account)
            ),
        )

    def disconnect(self, client: WebClient, context: BoltContext, user_id: str):
        forgotten_token = self.accounts.forget(context, user_id)
        self.report(client, user_id, None)
        if forgotten_token is not None:
            client.auth_revoke(token=forgotten_token)

    def report(self, client: WebClient, user_id: str, connection: Connection | None):
        provider = acme_provider(self.auth_url, connection)
        client.apps_user_connection_requestAuth(
            user_id=user_id, primary_provider=provider
        )
        client.views_publish(user_id=user_id, view=home_view(provider))

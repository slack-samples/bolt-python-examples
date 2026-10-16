from slack_bolt import BoltContext
from slack_sdk.oauth.installation_store import Installation, InstallationStore


class AcmeAccounts:
    def __init__(self, installation_store: InstallationStore):
        self.installation_store = installation_store

    def find(self, context: BoltContext, user_id: str) -> Installation | None:
        installation = self.installation_store.find_installation(
            enterprise_id=context.enterprise_id,
            team_id=context.team_id,
            user_id=user_id,
            is_enterprise_install=context.is_enterprise_install,
        )
        if installation is None or installation.user_token is None:
            return None
        return installation

    def forget(self, context: BoltContext, user_id: str) -> str | None:
        account = self.find(context, user_id)
        if account is None:
            return None
        self.installation_store.delete_installation(
            enterprise_id=account.enterprise_id,
            team_id=account.team_id,
            user_id=user_id,
        )
        return account.user_token

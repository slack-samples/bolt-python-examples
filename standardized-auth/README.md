# Standardized Auth

Connect your Acme account to Slack with the Slack-owned **Connect** and **Manage connection** controls. Rocket skates, anvils, and giant magnets not included.

Read the docs: https://docs.slack.dev/authentication/standardized-auth

## How it works

Acme keeps every connection in Bolt's installation store: a user is connected when the store holds their user token.

- **Connect** opens `/slack/install`. When the OAuth flow saves the user's token, the app reports the connection with `apps.user.connection.requestAuth` and refreshes App Home.
- **Disconnect** forgets the user's token, reports the user as disconnected, then revokes the token.
- **`user_connection_status_requested`** answers with `apps.user.connection.update` whenever Slack asks about a user it doesn't know yet.
- **`tokens_revoked`** forgets users who remove Acme from their Slack settings and reports them as disconnected.
- **App Home** shows an `auth_provider` block with the user's current connection.

## Setup

```sh
$ ngrok http 3000  # Replace 1234-56-78-90-0.ngrok-free.app in manifest.json
$ slack install --environment local  # Create a new app
$ slack app settings  # Gather the client ID, client secret, and signing secret
$ slack env init  # Update defaults with them and your ngrok URL
$ slack manifest  # Validate fields
$ slack run
$ open https://1234-56-78-90-0.ngrok-free.app/slack/install  # Install the app
```

Then open the app's **Home** tab and click **Connect**.

Swap the `users:read` and `users.profile:read` scopes for the ones your connection needs.

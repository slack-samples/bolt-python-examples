# Standardized Auth

Connect your Acme account to Slack with the Slack-owned **Connect** and **Manage connection** controls. Rocket skates, anvils, and giant magnets not included.

Read the docs: https://docs.slack.dev/authentication/standardized-auth

## How it works

Acme runs over Socket Mode and keeps every connection in a local `shelve` file ([`src/connections.py`](./src/connections.py)): a user is connected when their Slack user ID is in it. Shared helpers live in [`src/acme.py`](./src/acme.py), and the app and every listener live in [`app.py`](./app.py).

- **Connect** connects the Slack user who clicked it, with their user ID as the connected identity. It reports the connection with `apps.user.connection.requestAuth` and refreshes App Home.
- **Disconnect** forgets the connection and reports the user as disconnected.
- **`user_connection_status_requested`** answers with `apps.user.connection.update` whenever Slack asks about a user it doesn't know yet.
- **App Home** shows an `auth_provider` block with the user's current connection.

Connecting in one click stands in for your service's real login. Slack requires at least one host in the manifest's `features.user_connections.auth_hosts`, so `example.com` holds the place until you have one. To sign users in to your own service, set `auth_url` on the provider to your OAuth or SSO page, replace `example.com` with its host, and carry the Slack user through the browser in a signed `state` (the SDK's `StatelessOAuthStateStore` works for this) so a connection always lands on the user who clicked **Connect**.

## Setup

Everything arrives over Socket Mode, so the app needs no public URL. Use a Slack CLI newer than v4.10.0: older versions don't send `features.user_connections` with the manifest.

```sh
$ slack run
```

Then open the app's **Home** tab and click **Connect**.

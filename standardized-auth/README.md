# Standardized Auth

Connect your Acme account to Slack with the Slack-owned **Connect** and **Manage connection** controls. Rocket skates, anvils, and giant magnets not included.

Read the docs: https://docs.slack.dev/authentication/standardized-auth

## How it works

Acme runs over Socket Mode and keeps every connection in a local SQLite database ([`src/connections.py`](./src/connections.py)): a user is connected when it holds their Acme username. Shared helpers live in [`src/acme.py`](./src/acme.py), and each listener has its own file under [`src/listeners`](./src/listeners) that registers itself with `@app.action` or `@app.event`. [`src/bolt_app.py`](./src/bolt_app.py) imports every file in that directory when it builds the app, so a new listener only needs a new file.

- **Connect** opens Acme's sign-in page ([`src/sign_in.py`](./src/sign_in.py)) with a signed `state` ([`src/state.py`](./src/state.py)) naming the Slack user. Signing in saves the connection, reports it with `apps.user.connection.requestAuth`, and refreshes App Home.
- **Disconnect** ([`actions/disconnect.py`](./src/listeners/actions/disconnect.py)) forgets the connection and reports the user as disconnected.
- **`user_connection_status_requested`** ([`events/user_connection_status_requested.py`](./src/listeners/events/user_connection_status_requested.py)) answers with `apps.user.connection.update` whenever Slack asks about a user it doesn't know yet.
- **App Home** ([`events/app_home_opened.py`](./src/listeners/events/app_home_opened.py)) shows an `auth_provider` block with the user's current connection.

The sign-in page stands in for your service's real login. Swap it for your own OAuth or SSO flow, and keep the signed `state` so a connection always lands on the Slack user who clicked **Connect**.

## Setup

Events arrive over Socket Mode, so only the sign-in page needs a public HTTPS URL.

```sh
$ ngrok http 3000  # Replace 1234-56-78-90-0.ngrok-free.app in manifest.json
$ slack env init   # Set BASE_URL to your ngrok URL
$ slack run
```

Then open the app's **Home** tab and click **Connect**.

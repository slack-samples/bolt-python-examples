# Maintainers Guide

Let's hope to have matching examples of documentation and reference for various runtimes be consistent!

- **[Development](#development)**: Making changes alongside the Node Slack SDK.
- **[Commands](#commands)**: Reference to running example code of this project.
- **[Structure](#structure)**: Adding examples for features of the Slack Platform.

## Development

Bringing ongoing changes from the [Python Slack SDK](https://github.com/slackapi/python-slack-sdk) requires building from source with these commands:

```sh
$ git clone git@github.com:slackapi/python-slack-sdk.git
$ cd python-slack-sdk
$ python -m venv .venv
$ source .venv/bin/activate
(.venv) $ ./scripts/build_pypi_package.sh
```

This bundles a compilation as a `slack_sdk-*-py2.py3-none-any.whl` file that is used to replace previous installations:

```sh
$ git clone git@github.com:slack-samples/bolt-python-examples.git
$ cd bolt-python-examples
$ cd block-kit       # Navigate to an example to change
$ python -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install -r requirements.txt
(.venv) $ pip install /path/to/python-slack-sdk/dist/slack_sdk-*-py2.py3-none-any.whl --force-reinstall
```

## Commands

Each example has matching commands to run tests:

```sh
$ ruff check
$ ruff format --diff --check
$ mypy ./**/*.py
$ pytest -v
```

## Structure

New code snippets or samples added should match the structure of the [docs.slack.dev](https://docs.slack.dev) site:

```txt
|- .github
   |- dependabot.yml  # https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/controlling-dependencies-updated#defining-multiple-locations-for-manifest-files
|- block-kit
   |- blocks          # https://docs.slack.dev/reference/block-kit/blocks
   |- formatting      # https://docs.slack.dev/block-kit/formatting-with-rich-text
|- messaging
   |- sending         # https://docs.slack.dev/messaging/sending-and-scheduling-messages
   |- work-objects    # https://docs.slack.dev/messaging/work-objects
```

Some pages might reference distinct examples needing unique app manifests. These should appear in separate nested directories for a minimal demonstration.

Certain features or demonstrations might not have a clear example on the docs site. Discussions with the kind documentation team ought be started if so! We hope folks find relevant examples through those pages.

A goal of this project is to be a source of tested reference.

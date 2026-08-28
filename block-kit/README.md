# Block Kit

The framework of visual components arranged to create app layouts.

Read the [docs](https://docs.slack.dev/block-kit/) to learn concepts behind these constructions, or explore [reference](https://docs.slack.dev/reference/block-kit) pages for attribute details.

## What's on display

### Blocks

- **[Actions](https://docs.slack.dev/reference/block-kit/blocks/actions-block)**: Holds multiple interactive elements. [Implementation](./src/blocks/actions.py).
- **[Alert](https://docs.slack.dev/reference/block-kit/blocks/alert-block)**: Displays alerts, warnings, and informational messages. [Implementation](./src/blocks/alert.py).
- **[Context](https://docs.slack.dev/reference/block-kit/blocks/context-block)**: Provides contextual info, which can include both images and text. [Implementation](./src/blocks/context.py).
- **[Context actions](https://docs.slack.dev/reference/block-kit/blocks/context-actions-block)**: Displays actions as contextual info, which can include both feedback buttons and icon buttons. [Implementation](./src/blocks/context_actions.py).
- **[Divider](https://docs.slack.dev/reference/block-kit/blocks/divider-block)**: Visually separates pieces of info inside of a message. [Implementation](./src/blocks/divider.py).
- **[File](https://docs.slack.dev/reference/block-kit/blocks/file-block)**: Displays info about remote files. [Implementation](./src/blocks/file.py).
- **[Header](https://docs.slack.dev/reference/block-kit/blocks/header-block)**: Displays a larger-sized text. [Implementation](./src/blocks/header.py).
- **[Image](https://docs.slack.dev/reference/block-kit/blocks/image-block)**: Displays an image. [Implementation](./src/blocks/image.py).
- **[Input](https://docs.slack.dev/reference/block-kit/blocks/input-block)**: Collects information from users via elements. [Implementation](./src/blocks/input.py).
- **[Markdown](https://docs.slack.dev/reference/block-kit/blocks/markdown-block)**: Displays formatted markdown. [Implementation](./src/blocks/markdown.py).
- **[Plan](https://docs.slack.dev/reference/block-kit/blocks/plan-block)**: Displays a collection of related tasks. [Implementation](./src/blocks/plan.py).
- **[Rich text](https://docs.slack.dev/reference/block-kit/blocks/rich-text-block)**: Displays formatted, structured representation of text. [Implementation](./src/blocks/rich_text.py).
- **[Section](https://docs.slack.dev/reference/block-kit/blocks/section-block)**: Displays text, possibly alongside elements. [Implementation](./src/blocks/section.py).
- **[Table](https://docs.slack.dev/reference/block-kit/blocks/table-block)**: Displays structured information in a table. [Implementation](./src/blocks/table.py).
- **[Task card](https://docs.slack.dev/reference/block-kit/blocks/task-card-block)**: Displays a single task, representing a single action. [Implementation](./src/blocks/task_card.py).
- **[Video](https://docs.slack.dev/reference/block-kit/blocks/video-block)**: Displays an embedded video player. [Implementation](./src/blocks/video.py).

### Composition objects

- **[Confirmation dialog](https://docs.slack.dev/reference/block-kit/composition-objects/confirmation-dialog-object)**: Defines a dialog that adds a confirmation step to interactive elements. [Implementation](./src/composition_objects/confirmation_dialog.py).
- **[Conversation filter](https://docs.slack.dev/reference/block-kit/composition-objects/conversation-filter-object)**: Defines a filter for the list of options in a conversation selector menu. [Implementation](./src/composition_objects/conversation_filter.py).
- **[Dispatch action configuration](https://docs.slack.dev/reference/block-kit/composition-objects/dispatch-action-configuration-object)**: Defines when a plain-text input element will return a block_actions interaction payload. [Implementation](./src/composition_objects/dispatch_action_configuration.py).
- **[Option](https://docs.slack.dev/reference/block-kit/composition-objects/option-object)**: Defines a single item in a number of item selection elements. [Implementation](./src/composition_objects/option.py).
- **[Option group](https://docs.slack.dev/reference/block-kit/composition-objects/option-group-object)**: Defines a way to group options in a menu. [Implementation](./src/composition_objects/option_group.py).
- **[Slack file](https://docs.slack.dev/reference/block-kit/composition-objects/slack-file-object)**: Defines an object containing Slack file information to be used in an image block or image element. [Implementation](./src/composition_objects/slack_file.py).
- **[Text](https://docs.slack.dev/reference/block-kit/composition-objects/text-object)**: Defines an object containing some text. [Implementation](./src/composition_objects/text.py).
- **[Trigger](https://docs.slack.dev/reference/block-kit/composition-objects/trigger-object)**: Defines an object containing trigger information. [Implementation](./src/composition_objects/trigger.py).
- **[Workflow](https://docs.slack.dev/reference/block-kit/composition-objects/workflow-object)**: Defines an object containing workflow information. [Implementation](./src/composition_objects/workflow.py).

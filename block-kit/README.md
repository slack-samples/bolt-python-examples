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

### Block elements

- **[Button](https://docs.slack.dev/reference/block-kit/block-elements/button-element)**: Allows users a direct path to performing basic actions. [Implementation](./src/block_elements/button.py).
- **[Checkboxes](https://docs.slack.dev/reference/block-kit/block-elements/checkboxes-element)**: Allows users to choose multiple items from a list of options. [Implementation](./src/block_elements/checkboxes.py).
- **[Date picker](https://docs.slack.dev/reference/block-kit/block-elements/date-picker-element)**: Allows users to select a date from a calendar style UI. [Implementation](./src/block_elements/date_picker.py).
- **[Datetime picker](https://docs.slack.dev/reference/block-kit/block-elements/datetime-picker-element)**: Allows users to select both a date and a time of day. [Implementation](./src/block_elements/datetime_picker.py).
- **[Email input](https://docs.slack.dev/reference/block-kit/block-elements/email-input-element)**: Allows user to enter an email into a single-line field. [Implementation](./src/block_elements/email_input.py).
- **[File input](https://docs.slack.dev/reference/block-kit/block-elements/file-input-element)**: Allows user to upload files. [Implementation](./src/block_elements/file_input.py).
- **[Image](https://docs.slack.dev/reference/block-kit/block-elements/image-element)**: Displays an image as part of a larger block of content. [Implementation](./src/block_elements/image.py).
- **[Multi-select menu](https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element)**: Allows users to select multiple items from a list of options. [Implementation](./src/block_elements/multi_select_menu.py).
- **[Number input](https://docs.slack.dev/reference/block-kit/block-elements/number-input-element)**: Allows user to enter a number into a single-line field. [Implementation](./src/block_elements/number_input.py).
- **[Overflow menu](https://docs.slack.dev/reference/block-kit/block-elements/overflow-menu-element)**: Allows users to press a button to view a list of options. [Implementation](./src/block_elements/overflow_menu.py).
- **[Plain-text input](https://docs.slack.dev/reference/block-kit/block-elements/plain-text-input-element)**: Allows users to enter freeform text data into a single-line or multi-line field. [Implementation](./src/block_elements/plain_text_input.py).
- **[Radio button group](https://docs.slack.dev/reference/block-kit/block-elements/radio-button-group-element)**: Allows users to choose one item from a list of possible options. [Implementation](./src/block_elements/radio_buttons.py).
- **[Select menu](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element)**: Allows users to choose an option from a drop down menu. [Implementation](./src/block_elements/select_menu.py).
- **[Time picker](https://docs.slack.dev/reference/block-kit/block-elements/time-picker-element)**: Allows users to select a time of day. [Implementation](./src/block_elements/time_picker.py).
- **[URL input](https://docs.slack.dev/reference/block-kit/block-elements/url-input-element)**: Allows user to enter a URL into a single-line field. [Implementation](./src/block_elements/url_input.py).
- **[Workflow button](https://docs.slack.dev/reference/block-kit/block-elements/workflow-button-element)**: Allows users to run a link trigger with customizable inputs. [Implementation](./src/block_elements/workflow_button.py).

# Block Kit

The framework of visual components arranged to create app layouts.

Read the [docs](https://docs.slack.dev/block-kit/) to learn concepts behind these constructions, or explore [reference](https://docs.slack.dev/reference/block-kit) pages for attribute details.

## What's on display

### Blocks

- **[Actions](https://docs.slack.dev/reference/block-kit/blocks/actions-block)**: Holds multiple interactive elements. [Implementation](./src/blocks/actions.py).
- **[Context](https://docs.slack.dev/reference/block-kit/blocks/context-block)**: Provides contextual info, which can include both images and text. [Implementation](./src/blocks/context.py).
- **[Context actions](https://docs.slack.dev/reference/block-kit/blocks/context-actions-block)**: Holds interactive elements like feedback buttons and icon buttons. [Implementation](./src/blocks/context_actions.py).
- **[Divider](https://docs.slack.dev/reference/block-kit/blocks/divider-block)**: Visually separates pieces of info inside of a message. [Implementation](./src/blocks/divider.py).
- **[File](https://docs.slack.dev/reference/block-kit/blocks/file-block)**: Displays info about remote files. [Implementation](./src/blocks/file.py).
- **[Header](https://docs.slack.dev/reference/block-kit/blocks/header-block)**: Displays a larger-sized text. [Implementation](./src/blocks/header.py).
- **[Image](https://docs.slack.dev/reference/block-kit/blocks/image-block)**: Displays an image. [Implementation](./src/blocks/image.py).
- **[Input](https://docs.slack.dev/reference/block-kit/blocks/input-block)**: Collects information from users via elements. [Implementation](./src/blocks/input.py).
- **[Markdown](https://docs.slack.dev/reference/block-kit/blocks/markdown-block)**: Displays formatted markdown. [Implementation](./src/blocks/markdown.py).
- **[Rich text](https://docs.slack.dev/reference/block-kit/blocks/rich-text-block)**: Displays formatted, structured representation of text. [Implementation](./src/blocks/rich_text.py).
- **[Section](https://docs.slack.dev/reference/block-kit/blocks/section-block)**: Displays text, possibly alongside elements. [Implementation](./src/blocks/section.py).
- **[Video](https://docs.slack.dev/reference/block-kit/blocks/video-block)**: Displays an embedded video player. [Implementation](./src/blocks/video.py).

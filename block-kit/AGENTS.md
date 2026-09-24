# Adding a Block Example

A block example is **code-complete** when all four of these are present:

1. Example file
2. Test file
3. README entry
4. Correct docstring

## Example file

Create `src/blocks/{type}.py`:

```python
from slack_sdk.models.blocks import {Type}Block
from slack_sdk.models.blocks.basic_components import MarkdownTextObject, PlainTextObject
from slack_sdk.models.blocks.block_elements import ButtonElement, ImageElement


def example01() -> {Type}Block:
    """
    {Description from docs page — must match exactly}.
    https://docs.slack.dev/reference/block-kit/blocks/{type}-block/

    {Brief description of this specific example}.
    """
    block = {Type}Block(
        # fields here
    )
    return block
```

Rules:
- One file per block type in `src/blocks/`
- Each example is a module-level function returning the block type
- Functions named `example01()`, `example02()`, etc. with return type annotation
- Import blocks from `slack_sdk.models.blocks`
- Import text objects from `slack_sdk.models.blocks.basic_components`
- Import elements from `slack_sdk.models.blocks.block_elements`
- The docstring first line must match the docs page `description` field exactly (found in the page's YAML frontmatter)

## Test file

Create `tests/blocks/test_{type}.py`:

```python
import json

from src.blocks import {type}


def test_example01():
    block = {type}.example01()
    actual = block.to_dict()
    expected = {
        "type": "{type}",
        # fields matching the docs JSON example
    }
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True)
```

The expected dict must match the docs page JSON example exactly (minus the outer `"blocks": [...]` wrapper).

## README entry

Add an entry to `block-kit/README.md` in alphabetical order under `### Blocks`:

```markdown
- **[{Name}](https://docs.slack.dev/reference/block-kit/blocks/{type}-block)**: {Description matching docs}. [Implementation](./src/blocks/{type}.py).
```

The description must match the docs page `description` field exactly.

## Lint and verify

```bash
cd block-kit
ruff check src/blocks/{type}.py tests/blocks/test_{type}.py
ruff format --check src/blocks/{type}.py tests/blocks/test_{type}.py
pytest tests/blocks/test_{type}.py
```

All must pass. Use `ruff format` (without `--check`) to auto-fix formatting.

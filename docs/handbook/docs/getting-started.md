## Prerequisites

Download and install uv by following the [official guide](https://docs.astral.sh/uv/getting-started/installation/).

## Run the documentation locally

```shell
uv run mkdocs serve
```

## Publish the documentation to GitHub Pages

```shell
uv run mkdocs gh-deploy
```

## Update all dependencies

```shell
uv sync -U
```

## Documentation Structure

- **`docs/`** : Contains the Markdown files for the documentation.

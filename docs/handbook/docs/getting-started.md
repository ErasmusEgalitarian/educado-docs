## Prerequisites

Download and install uv by following the [official guide](https://docs.astral.sh/uv/getting-started/installation/).

## Run the documentation locally

```sh
uv run mkdocs serve
```

## Publish the documentation to GitHub Pages

```sh
uv run mkdocs gh-deployss
```

## Documentation Structure

* **`docs/`** : Contains the Markdown files for the documentation.
* **`venv/`** : Python virtual environment (ignored by `.gitignore`).

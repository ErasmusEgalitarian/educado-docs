## Set up a Python virtual environment

```sh
python -m venv venv
```

## Activate the virtual environment

On Windows:

```powershell
venv\Scripts\activate
```

On macOS/Linux:

```sh
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Preview the documentation locally

```sh
mkdocs serve
```

## Publish the documentation to GitHub Pages

```
mkdocs gh-deploy
```

## Documentation Structure

* **`docs/`** : Contains the Markdown files for the documentation.
* **`venv/`** : Python virtual environment (ignored by `.gitignore`).

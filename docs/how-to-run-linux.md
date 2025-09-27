# How to run DAGENT — Linux / macOS

This page contains platform-specific instructions for Linux and macOS (bash/zsh).

## Quick one-liner

Create a venv, activate it, install requirements and the package in editable mode (includes the `dagent` console script):

```bash
python3 -m venv .venv && source .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt && pip install -e .[dev]
```

If you don't want dev extras, omit the `[dev]`:

```bash
pip install -e .
```

## Step-by-step

1. Clone the repo and enter it:

```bash
git clone https://github.com/eat-sleep-code-repeat-it/disaster-assistant.git
cd disaster-assistant
```

2. Create and activate a virtual environment (Python 3.12 recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
# Optional dev tools for testing/formatting
pip install -e .[dev]
```

4. Configure API key:

```bash
cp .env.example .env
# Edit .env and set OPENAI_API_KEY=sk-...
```

5. Run the app:

```bash
python -m app.main
```

Use `--no-verify-ssl` if you must disable SSL verification (not recommended):

```bash
dagent --no-verify-ssl
python -m app.main --no-verify-ssl
```

## Platform notes & troubleshooting (Linux/macOS)

- Python version: This project targets Python 3.12 (README suggests 3.12.10). Use `pyenv` or system packages to install the correct Python if necessary.
- FAISS install: `faiss-cpu` sometimes lacks prebuilt wheels. If `pip install faiss-cpu` fails:
  - Use conda: `conda install -c conda-forge faiss-cpu` (recommended on Linux/macos for ease), or
  - Find a suitable wheel for your Python version/platform.
- First run: The app may build the FAISS index using OpenAI embeddings (this will use API calls). If you have the `saved_index/` files included, the app will load them to avoid recomputing embeddings.
- OpenAI key errors: Ensure `.env` contains `OPENAI_API_KEY=sk-...` and that there are no trailing quotes. Environment variables override `.env`.
- SSL issues: If your environment rejects certificates, use `--no-verify-ssl` to skip verification (use only for debugging).

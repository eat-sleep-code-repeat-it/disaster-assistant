# How to run DAGENT — Windows (PowerShell)

This page contains Windows-specific instructions for running DAGENT using PowerShell.

## Step-by-step

1. Clone and enter the repo:

```powershell
git clone https://github.com/eat-sleep-code-repeat-it/disaster-assistant.git
cd disaster-assistant
```

2. Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .[dev]  # optional
```

4. Create `.env` and add your OpenAI key (edit in a text editor):

```powershell
copy .env.example .env
# Edit .env to replace the placeholder with your OPENAI_API_KEY
```

5. Run the app:

```powershell
python -m app.main
python -m app.main --no-verify-ssl
```

## Platform notes & troubleshooting (Windows)

- If you encounter problems installing `faiss-cpu`, prefer using `conda` (Anaconda/Miniconda):
  - `conda install -c conda-forge faiss-cpu`
- If `Activate.ps1` is blocked by execution policy, use PowerShell as Administrator and run:
  - `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- OpenAI key errors: Make sure `.env` contains `OPENAI_API_KEY=sk-...`. Environment variables take precedence over `.env`.

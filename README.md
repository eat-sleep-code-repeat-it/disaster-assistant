# DEAGENT - AI-powered Disaster Assistant

This is a final project for **[Springboard AI for Programmers Mini-MBA (On-Demand)](https://my.sectionai.com/mini-mbas/e7306541-f1d2-4920-b40a-8233e628f2f1)**.

I have built an application called **DAGENT** — short for *Disaster Agent* — an AI-powered assistant that helps answer questions about **FEMA disaster declarations**.

You can see detailed [implementation steps](docs/DAGENT-implementation.md).

## Demo

- You can watch my [Demo Video](abc).
- You can listen my [presentation Audio](DAGENT-presentation.mp3).


## Quick start (copy-paste)

If you want a very short start, run the appropriate snippet below. See [`how-to-run-linux.md`](docs//how-to-run-linux.md) or [`how-to-run-windows.md`](docs/how-to-run-windows.md) for full, platform-specific instructions.

Linux / macOS (bash):

```bash
git clone <repository-url> disaster-assistant
cd disaster-assistant
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && pip install -e .
cp .env.example .env   # then edit .env and set OPENAI_API_KEY
dagent
```

Windows (PowerShell):

```powershell
git clone <repository-url> disaster-assistant
cd disaster-assistant
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env  # edit .env to set OPENAI_API_KEY
dagent
```

## Sample prompts

Try these prompts in the Gradio chat to explore the dataset and RAG behavior:

```js
is there an active disaster in Washington County, Oregon?
is there a disaster in Riverside, California?
active fire disasters?
give all fire disasters?
```

## Project Structure
- Keep Gradio app logic clean and isolated
- Separate data/model logic from UI
- Make it easier to maintain, extend, or even deploy later (e.g., with FastAPI)

```bash
disaster-assistant/
├── app/
│   ├── main.py               # 🔹 Main Gradio app (entry point)
│   ├── rag_pipeline.py       # 🔹 RAG logic (retrieval + answer generation) 
│   ├── models.py             # 🔹 Pydantic models (e.g., DisasterDeclaration)
│   ├── embedding_utils.py    # 🔹 Embedding + FAISS index handling
│   ├── answer_eval.py        # 🔹 Guardrails & GPT-based evaluation
│   ├── data_loader.py        # 🔹 Load/parse CSV data
│   └── constants.py          # 🔹 Paths, constants, config keys
│
├── data/
│   └── disaster_declarations.csv  # 🔹 Source dataset
│
├── saved_index/              # 🔹 Store FAISS index & metadata
│   ├── disaster_faiss.index
│   └── disaster_metadata.pkl
│
├── assets/                   # 🔹 (Optional) Images, logos, docs
│   └── README.md
│
├── tests/
│   └── test_rag_pipeline.py  # 🔹 Unit tests (pytest)
│
├── .env                      # 🔹 OpenAI keys, etc.
├── disaster_assistant_deprecated.py    # deprecated old single script version
├── .gitignore
├── README.md
├── docs
│   └── how-to-run-linux.md       # 🔹 Linux/macOS run instructions
│   └── how-to-run-windows.md     # 🔹 Windows run instructions
├── requirements.txt

app/main.py	            Launches the Gradio UI (e.g., gr.ChatInterface)
app/rag_pipeline.py	    Contains rag_pipeline() and chat_rag_fn() logic
app/models.py	        Pydantic DisasterDeclaration and other data models
app/embedding_utils.py	Embedding + FAISS build/save/load
app/answer_eval.py	    GPT-based evaluation and keyword-based guardrails
data/	                Static data source (e.g., CSVs)
saved_index/	        Stores generated FAISS index and metadata
tests/	                Optional test suite using pytest or unittest
```




 
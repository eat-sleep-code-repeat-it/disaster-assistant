# DEAGENT - AI-powered Disaster Assistant

This is a final project for **[Springboard AI for Programmers Mini-MBA (On-Demand)](https://my.sectionai.com/mini-mbas/e7306541-f1d2-4920-b40a-8233e628f2f1)**.

I have built an application called **DAGENT** — short for *Disaster Agent* — an AI-powered assistant that helps answer questions about **FEMA disaster declarations**.

You can see detail [implementation steps](/docs/DAGENT-implementation.md).

## Demo

- You can watch my [Demo Video](abc).
- You can listen my [presentation Audio](/docs/DAGENT-presentation.mp3).


## How to run by yourself

I have included a small size of the original dataset for demo purpose to reduce openai token usage. The original FEMA dataset is a large file containing all disaster declarations since they are recorded. 

The instructions are mainly writen for windows users since I only one windows laptop. You may follow the following instructions to run by yourself. 
 
- requires `Python 3.13.7`
- clone this repo (assuming you are in `c:/workspace` directory on windows)
- navigate to the application `cd c:/workspace/disaster-assistant`
- rename `.env.example` to `.env`
- open `.env` and replace `<your_openai_api_key_here>` with your openai key
- run the following command



```bash
# requires Python 3.13.7

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate 

# On Windows
python -m venv .venv
venv\Scripts\activate

# install packages
pip install -r requirements.txt

# run DEAGENT with SSL on
python -m app.main

# if you have SSL issue, run this istead to skip SSL
python -m app.main --no-verify-ssl

```

- Sample Prompts
```js
is there an active disaster in Washington County, Oregon? 
is there an disaster in Riverside, California? 
is there an active disaster in Riverside, California?
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




 
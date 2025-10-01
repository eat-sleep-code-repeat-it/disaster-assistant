# DAGENT - AI-powered Disaster Assistant

Ask Anything About U.S. FEMA Disaster Declarations.

## Coding
```bash
# requires Python 3.12.7

python -m venv venv
venv\Scripts\activate 

pip install gradio
pip install openai
pip install faiss-cpu
pip install python-dotenv

#python disaster_assistant.py 

venv\scripts\python.exe -m pip install --upgrade pip
pip install -r requirements.txt

# refactor
python -m app.main
python -m app.main --no-verify-ssl

```

### First step - Completed
- test venv and openai setup: test_setup
- download csv
    - for demo, we use a small subset of the originial csv to reduce API usage
- read declarations as structured date model from csv
- create index
    - for each structured disaster declaration, create embeddings using OpenAI Embeddings API.
    - Creates and populates a FAISS vector index from disaster declaration embeddings
- Store FAISS index and embeddings to disk
- Reload FAISS index and embeddings 
    - to avoid recomputing embeddings
    - to save a ton of time and API usage
- define structured outputs using schemas and models like Pydantic
### Second step - Completed
- setup gradio UI
    - take prompt from UI
    - display conversation
    - keep chat history in live session
    - auto scroll to the latest conversation

### Third step - Completed
- Retrieval-Augmented Generation (RAG)
    - Use embeddings to transform disater declaration into searchable, meaning-rich vectors
    - retrieval/search data from vector to enable enables semantic search
    - pass relevant context to openai to prevent AI hallucinations
- generate openai answer using structured outputs

### Fourth step - Completed
- ? observability for monitoring LLM behavior
- Evaluate answer using openai as judge from aspect of relevance, accuracy, completeness
- Guardrail to validate answer
    - Blocks short or irrelevant answers that don't mention keywords from the query
- Include top match records

### Five step - Completed
- transform complex AI tasks into reliable workflows through chaining—breaking tasks into logical steps with defined inputs and fallback plans
- refactor to module based app instead of dooing everthing in one script
- create embedings in batch to save time and token usage
- use logger instead of print

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


## Sample Prompts
```js
is there an active disaster in Washington County, Oregon? 
is there an disaster in Riverside, California? 
is there an active disaster in Riverside, California?
active fire disasters? 
give all fire disasters?
```

## Future

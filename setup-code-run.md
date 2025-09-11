#  AI-powered Disaster Assistant

Ask Anything About U.S. FEMA Disaster Declarations.

## Coding
```bash
# requires Python 3.13.7

python -m venv venv
venv\Scripts\activate 

pip install gradio
pip install openai
pip install faiss-cpu
pip install python-dotenv

python disaster_assistant.py

venv\scripts\python.exe -m pip install --upgrade pip
pip install -r requirements.txt
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

### Second step - Completed
- setup gradio UI

### Third step - Completed
- RAG pipeline
    - search vector
    - pass context to openai
- generate openai answer

### Fourth step - TODO
- Guardrail Evaluation
- Active disaster filtering
- Active disaster filtering

## Sample Prompts
```js
is there an active disaster in Washington County, Oregon? 
is there an disaster in Riverside, California? 
is there an active disaster in Riverside, California?
active fire disasters? 
give all fire disasters?
```

## Future

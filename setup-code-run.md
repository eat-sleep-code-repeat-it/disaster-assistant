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

### First step
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
## Sample Prompts

## Future

# Disaster AI Assistant

This is a final project for **[Springboard AI for Programmers Mini-MBA (On-Demand)](https://my.sectionai.com/mini-mbas/e7306541-f1d2-4920-b40a-8233e628f2f1)**.

## Objective

Create a disaster AI assistant application (DAGENT) that leverages AI capabilities covered in the course to answer questions about FEMA disaster declaration.

A FEMA disaster declaration is a public dataset that contains information about disasters declared by the Federal Emergency Management Agency (FEMA) in the United States. The dataset includes details such as the type of disaster, location, date, and assistance provided. FEMA publishes disaster declarations in structured formats such csv and json format file.

A FEMA disaster declaration acts as an official signal that a disaster has occurred in a region, activating regulatory relief measures and enabling mortgage companies to lawfully and compassionately assist borrowers affected by that disaster.

mortgage companies must verify that the borrower’s property is in a FEMA-declared disaster area with Individual Assistance (IA) or Public Assistance (PA), depending on the type of relief being offered.

This verification is essential for applying disaster-related forbearance, deferrals, or modification programs—especially for government-backed loans (e.g., FHA, VA, USDA, Fannie Mae, Freddie Mac).

I created a disaster AI assistant called (DAGENT) as course final project to help the verification process via an interactive UI powered by agentic AI. The DAGENT implementation highlights the following key AI capabilities:

- Prompt engineering
- Structured outputs
- Retrieval-Augmented Generation (RAG) and vector databases
- Evaluation techniques
- Observability and monitoring
- Guardrail

## Build a Python agentic AI app called `DAGENT`

- Pull FEMA disaster declaration data csv from FEMA website
- Convert each disaster declaration to an embedding vector using OpenAI embeddings
- Store embeddings in a vector store for fast similarity search
- When a user inputs a state + county (or a freeform question), the app:
  - Create an embedding for the query
  - Search the vector store for the most relevant disaster declarations
  - Feed those relevant results as context to OpenAI to generate a response
  - Guardrails: Refuse to answer if results are empty
  - Evaluation: Use GPT-4 as a judge to rate:
    - Relevance
    - Accuracy
    - Completeness
- Previous messages are preserved in context
- Use gradio to build UI (like ChatGPT):
  - Display question asked by a user
  - Display response
  - Display guardrail info
  - Display evaluation info

## Key Deliverables

- Fully functional AI-powered software application
- Professionally documented GitHub repository
- Short demonstration video (up to 3 minutes) clearly explaining your
  - application’s purpose
  - AI features
  - Unique aspects
  
## Setup, Coding, Run

See [step by step](setup-code-run.md)

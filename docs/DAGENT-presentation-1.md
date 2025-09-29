
# 🎥 DAGENT – Final Project Demo Script

Hi, I’m Rolland, and I’m excited to present my final project for the Springboard AI for Programmers Mini-MBA.

I’ve built an application called DAGENT — short for Disaster Agent.
It’s an AI-powered assistant that helps users quickly get answers about FEMA disaster declarations.

Let’s take a quick look at how I set it up.

First, I cloned the project repository from GitHub into my local workspace:
```bash
git clone https://github.com/eat-sleep-code-repeat-it/disaster-assistant.git
```

This pulls down all the source code into a folder called disaster-assistant.

Then I navigated into the project directory:
```bash
cd disaster-assistant
```
To keep dependencies isolated, I created a Python virtual environment:
```bash
python -m venv .venv
```
And activated it using PowerShell:
```bash
.venv\Scripts\Activate.ps1
```
With the environment active, I installed all required Python packages:
```bash
pip install -r requirements.txt
```

Next, I set up the environment variables. I copied the example configuration file:
```bash
copy .env.example .env
```
Then I opened the .env file and added my OPENAI_API_KEY so the app can securely access OpenAI’s API.


Finally, I launched the application:
```bash
python -m app.main
```

---

## ✅ Purpose of the Application

DAGENT is designed to help **mortgage companies and financial institutions** verify whether a property is located in a **FEMA-declared disaster area**.

This verification is critical before offering disaster relief programs like **forbearance, deferrals, or loan modifications**, especially for **government-backed loans** like FHA, VA, USDA, Fannie Mae, and Freddie Mac.

Traditionally, this process involves manually reviewing FEMA’s public datasets — which is slow, repetitive, and error-prone.

**DAGENT automates and simplifies this process** using natural language input and AI-powered search over FEMA disaster data.

---

## 🧠 Key AI Features

The application demonstrates several important AI capabilities covered in the course:

- **Prompt Engineering** – to guide how the assistant interprets and responds to user queries  
- **OpenAI Embeddings** – to convert disaster records and user questions into semantic vectors  
- **Vector Databases** – for fast and accurate similarity search  
- **Retrieval-Augmented Generation (RAG)** – to inject relevant FEMA data into the model’s context  
- **Guardrails** – to prevent the model from answering when no relevant data is found  
- **AI-based Evaluation** – using openAI to assess each answer for:
  - Relevance  
  - Accuracy  
  - Completeness  

The user interface is built using **Gradio**, making it easy to interact with the assistant — just like using ChatGPT.

---

## 🌟 Unique Aspects of DAGENT

What sets DAGENT apart are three things:

1. **Domain-Specific Use Case** – It solves a real compliance problem in the mortgage and housing finance industry  
2. **AI with Structured Outputs** – Answers aren’t just generic text — they’re grounded in actual FEMA declarations  
3. **AI with Gardrails, Evaluation Built-In** – Each response is automatically reviewed by openAI, giving users transparent feedback on response quality

---

## 🚀 Future Direction

Looking ahead, I plan to extend DAGENT by:

- Connecting it to **internal enterprise systems**  
- Using **Model Context Protocol (MCP Server)** to manage context across agents and build a larger agentic AI application

---

## 🎯 Final Summary

DAGENT combines real-world data and advanced AI features to solve a practical, high-impact problem — with the flexibility to scale into enterprise-grade systems.

Thanks for watching!

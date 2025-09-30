
# 🎥 DAGENT – Final Project Demo Script

Hi, I’m Rolland, and I’m excited to present my final project for the Springboard AI for Programmers Mini-MBA.

I’ve built an application called DAGENT — short for Disaster Agent.

## ✅ Purpose of the Application

DAGENT is designed to help **mortgage companies** verify whether a property is located in a **FEMA-declared disaster area**.

This verification is critical before offering disaster relief programs. 
Traditionally, this process involves manually reviewing FEMA’s public datasets — which is slow, repetitive, and error-prone.

**DAGENT automates and simplifies this process** using natural language input and AI-powered search over FEMA disaster data.

Let’s take a quick look at how I set up, and run it, then show you the key features of the application.

First, I cloned the project repository from GitHub into my local workspace:
```bash
git clone https://github.com/eat-sleep-code-repeat-it/disaster-assistant.git
```
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

Once it’s running, you can open ` http://127.0.0.1:7860/`in your browser.

Here’s the interface — simple and clean.

You can type in a natural language question, like:
```js
is there a disaster in Washington County, Oregon?
is there a disaster in Riverside, California? 
is there a disaster in California in fiscal year 2025?
is there flood disaster in TX in fiscal year 2025

do you know movies related to disaster?
```

And DAGENT will respond with structured information powered by AI.



Thanks for watching my demo!
---



---

## 🧠 Key AI Features

The application demonstrates several important AI capabilities covered in the course:

1. **Prompt Engineering** – to guide how the assistant interprets and responds to user queries  
2. **OpenAI Embeddings** – to convert disaster records and user questions into semantic vectors  
3. **Vector Databases** – for fast and accurate similarity search  
4. **Retrieval-Augmented Generation (RAG)** – to inject relevant FEMA data into the model’s context  
5. **Guardrails** – to prevent the model from answering when no relevant data is found  
6. **AI-based Evaluation** – using openAI to assess each answer for:
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

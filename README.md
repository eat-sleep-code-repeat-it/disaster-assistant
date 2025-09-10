
#  Disaster Assistant

This is a final project for [<b>Springboard AI for Programmers Mini-MBA (On-Demand)</b>](https://my.sectionai.com/mini-mbas/e7306541-f1d2-4920-b40a-8233e628f2f1).

## Objective:
Create a practical, functional software application that leverages one or more AI capabilities covered in the course, addressing a clearly defined software engineering problem or enhancing an existing workflow.

## Key Deliverables:
- Fully functional AI-powered software application
- Professionally documented GitHub repository
- Short demonstration video (up to 3 minutes) clearly explaining your application’s purpose, AI features, and unique aspects

## Directions
Create a functional application that integrates one or more AI features covered in this course. You’ll use Cursor (or some AI coding assistant equivalent) to help build your project efficiently. Your final submission will include your code and a brief demo video. You may also have the opportunity to showcase your project live during Demo Day.

Step by Step Directions:
1. Define Your Project Scope
- Identify a real-world problem or opportunity where AI can provide value.
- Choose a specific use case or workflow you want to enhance with AI.
2. Select AI Features to Implement
- Review course topics and decide which AI capabilities to include:
    - Prompt engineering
    - Structured outputs
    - Retrieval-Augmented Generation (RAG) and vector databases
    - Evaluation techniques
    - Observability and monitoring
- You may combine multiple features as long as the scope remains manageable.
3. Build Using Cursor + AI Composer
- Use Cursor’s AI-assisted development tools to generate boilerplate code, iterate on features, and accelerate development.
- Make sure to refine and review AI-generated code for correctness and alignment with your project goals.
4. Test and Validate Your Project
- Ensure your AI features perform reliably.
- Add any necessary evaluations or observability tools to monitor and debug performance.
5. Prepare Your Submission
- Upload your complete codebase to GitHub or BitBucket.
- Record a short video (under 3 minutes) that:
    - Clearly explains your project’s purpose
    -Demonstrates its AI features in action
    - Highlights any unique or innovative aspects
6. Submit
- Submit your links through the [MBA Center](https://my.sectionai.com/mini-mbas) under Week 7 - Project Week.

## Build a Python agentic AI app called `DisasterAssistant`
- Pull FEMA disaster declaration data csv from FEMA website
- Converts each disaster declaration to an embedding vector using OpenAI embeddings
- Stores embeddings in a vector store for fast similarity search 
- When a user inputs a state + county (or a freeform question), the app:
    - Creates an embedding for the query.
    - Searches the vector store for the most relevant disaster declarations.
    - Feeds those relevant results as context to OpenAI to generate a response.
    - Guardrails: Refuse to answer if results are empty.
    - Evaluation: Use GPT-4 as a judge to rate:
    - Relevance
    - Accuracy
- Previous messages are preserved in context
- Use gradio to build UI (like ChatGPT)
    - display question asked by a user
    - display response
    - display guardrail info
    - display evaluation info
## setup, coding, run
[step by step](setup-code-run.md)

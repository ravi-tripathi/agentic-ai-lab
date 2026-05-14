# Project 2: Prompt Chaining System
This project demonstrates how to link multiple LLM calls together using LangChain Expression Language (LCEL).

## Concepts Learned
- **LCEL (Pipe Operator):** Using `|` to flow data between components.
- **Output Parsers:** Using `StrOutputParser` to clean LLM responses for the next step.
- **Sequential Logic:** How the output of one prompt serves as the context for the next.

## How to Run
1. Ensure `.env` has your `GOOGLE_API_KEY`.
2. Run `python app.py`.


## Summary Notes

We are moving from "Single Prompts" to "Workflow Automation." 
In Agentic AI, a "Chain" is a sequence of LLM calls where the output of Step A becomes the input for Step B. To do this efficiently, we use LCEL (LangChain Expression Language)—the | (pipe) operator you see in modern LangChain code.

LangChain Expression Language (LCEL) is a declarative, composable way to build complexchains in LangChain using a pipe operator (|) to connect components like prompts, models, and retrievers. It enables seamless streaming, async support, parallel execution, and built-in logging/debugging via LangSmith.

We are building a two-step chain:

Step 1: Take a complex topic and generate a high-level summary.
Step 2: Take that summary and convert it into a "5-year-old's explanation" (EL5).

ELI5: Explain Like I'm 5


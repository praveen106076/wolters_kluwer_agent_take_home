# AI Engineering Take-Home: Autonomous Research Agent

A minimal, framework-free AI agent built to demonstrate autonomous task execution through a custom **ReAct (Reason + Act)** loop.

## 1. Project Overview
This agent breaks down high-level goals into multi-step tasks. It is designed for maximum **observability** and **state control** by avoiding heavy agent frameworks (like LangChain or LangGraph), relying instead on standard Python and the OpenAI SDK.

## 2. Technical Stack
- **Language:** Python 3.x
- **Core Library:** `openai` (for LLM interaction)
- **Environment Management:** `python-dotenv` (for secure credential handling)
- **Dependencies:** Defined in `requirements.txt`

## 3. How It Works
The agent utilizes a stateful loop that processes tasks in three distinct phases:

1. **Thought:** The LLM analyzes the current goal and determines the next step.
2. **Action:** The agent calls a tool (e.g., `search_web`, `read_file`) based on its thought process.
3. **Observation:** The tool output is fed back into the conversation history, allowing the agent to adapt its strategy if errors occur.

## 4. Evaluation Harness
I implemented an evaluation script (`evaluator.py`) to validate agent performance. It tests the agent against a set of predefined prompts, measuring its ability to:
- Successfully call tools to retrieve data.
- Adhere to the `Final Answer` format.

## 5. Setup & Execution
### Prerequisites
Ensure you have Python installed, then install the required dependencies:
```bash
pip install -r requirements.txt
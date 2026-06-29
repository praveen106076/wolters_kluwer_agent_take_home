Research Agent (ReAct)
A minimal, autonomous research agent built from scratch to solve multi-step tasks. This project demonstrates core AI engineering principles—state management, prompt engineering, and observability—without relying on heavy agent frameworks.

1. Approach
Architecture: Implements a stateful while loop that forces the LLM to follow the Thought → Action → Observation pattern.

Observability: Every step of the reasoning process (Thought, Action, Observation) is printed to the terminal, allowing for real-time debugging and performance tracing.

Resilience: Errors (e.g., tool execution failures) are captured and fed back to the agent as Observations, allowing the model to self-correct its strategy.

2. Evaluation Harness
I developed an evaluation script (evaluator.py) to test the agent against predefined prompts.

The harness verifies the agent's ability to fetch external information, manage multi-step reasoning, and adhere to the "Final Answer" output format.

3. Quick Start
Install dependencies:

Bash
pip install -r requirements.txt
Configure Environment:
Create a .env file in the root directory and add your API key:

Code snippet
OPENAI_API_KEY=your_openai_api_key_here
Run Tests:

Bash
python evaluator.py
4. Engineering Trade-offs
Why CLI? I chose a command-line interface over a web UI to prioritize the "backend" logic. This keeps the focus on the reasoning loop and ensures clean, sequential logs for better observability.

Why no frameworks? Avoiding libraries like LangChain or LangGraph allows for absolute transparency in how the agent handles context and state. It demonstrates a foundational understanding of the ReAct pattern.

5. Future Improvements
Memory: Implement a local vector store (e.g., ChromaDB) for persistent context across long-running tasks.

Logging: Move from terminal print statements to structured JSON logging for better integration with external monitoring dashboards.

Submission Checklist
[x] Source Code: Clear structure and documentation.

[x] Evaluation Harness: evaluator.py is ready to run.

[x] README: This document covers design, trade-offs, and instructions.

[x] Build Sessions: Ensure you have added the build_sessions/ folder with your raw logs.

[x] Security: Ensure .env is listed in your .gitignore file to protect your API credentials.
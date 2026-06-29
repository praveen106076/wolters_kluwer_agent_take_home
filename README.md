AI Engineering Take-Home: Autonomous Research Agent
A minimal, framework-free AI agent built to demonstrate autonomous task execution through a custom ReAct (Reason + Act) loop.

1. Project Overview
This agent breaks down high-level goals into multi-step tasks. It is designed for maximum observability and state control by avoiding heavy agent frameworks (like LangChain or LangGraph), relying instead on standard Python and the OpenAI SDK.

2. Technical Stack
Language: Python 3.x

Core Library: openai (for LLM interaction)

Environment Management: python-dotenv (for secure credential handling)

Dependencies: Defined in requirements.txt

3. How It Works
The agent utilizes a stateful loop that processes tasks in three distinct phases:

Thought: The LLM analyzes the current goal and determines the next step.

Action: The agent calls a tool (e.g., search_web, read_file) based on its thought process.

Observation: The tool output is fed back into the conversation history, allowing the agent to adapt its strategy if errors occur.

4. Evaluation Harness
I implemented an evaluation script (evaluator.py) to validate agent performance. It tests the agent against a set of predefined prompts, measuring its ability to:

Successfully call tools to retrieve data.

Adhere to the Final Answer format.

Handle multi-step reasoning without exceeding the loop limit (5 steps).

5. Setup & Execution
Prerequisites
Ensure you have Python installed, then install the required dependencies:

Bash
pip install -r requirements.txt
Configuration
Create a file named .env in the root directory.

Add your API key:

Code snippet
OPENAI_API_KEY=your_openai_api_key_here
Running the Agent
To run the full evaluation suite:

Bash
python evaluator.py
To run a single task:

Bash
python run.py
6. Engineering Decisions & Trade-offs
Custom Harness vs. Frameworks: By building the loop manually, I maintained full control over the agent's context window and state management, providing better transparency into the agent's decision-making process.

CLI Interaction: A command-line interface was chosen to provide real-time, sequential tracing of the agent's "Thought," "Action," and "Observation" cycles.

Time Allocation:

Architecture & Loop Logic: 2 hours

Tool Development & Prompting: 1.5 hours

Evaluation Harness & Testing: 1 hour

Documentation & Final Polish: 1 hour

7. Deliverables Checklist
[x] Source Code: Public Git repository structure.

[x] README: This file.

[x] Evaluation Harness: evaluator.py included.

[x] Example Run: Demo included in run.py.

[x] Build Session Logs: Provided in build_sessions/.
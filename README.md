# Research Agent (ReAct)

A simple, standalone research agent I built from scratch to handle multi-step tasks. I wanted to see if I could build a working agent loop without getting bogged down by massive frameworks like LangChain.

## 1. How it works

The agent runs on a straightforward "ReAct" loop. It doesn't use complex state machines; it just follows a simple cycle:

**Thought:** The LLM analyzes the goal and decides the next step.

**Action:** It calls a specific tool (like search_web or read_file) based on that thought.

**Observation:** The tool output is fed back into the agent's history, and the loop continues until the agent hits a "Final Answer."

I limited the loop to 5 steps to keep the agent from getting stuck in infinite loops or running up API costs.

## 2. Key decisions I made

**No Frameworks:** I purposefully avoided heavy frameworks. Most of them hide too much "magic" under the hood. By writing the loop myself, I could see exactly what the agent was doing at every step, which made debugging much easier.

**CLI-first:** I stuck with a Command Line Interface instead of a UI. A CLI is perfect for seeing the "Thought → Action → Observation" trace in real-time without the overhead of building a frontend.

**Resilient Error Handling:** If a tool fails, the error message is fed back to the agent as an observation. This allows the agent to "see" its mistake and try a different approach, rather than just crashing.

## 3. Setup

`pip install -r requirements.txt`

1. Create a `.env` file in the root directory with your OPENAI_API_KEY.

2. To run the tests: `python evaluator.py`

3. To run a single task: `python run.py`

## 4. Deliverables Checklist

1. [x] Source Code: Clear project structure.

2. [x] Evaluation Harness: `evaluator.py` included.

3. [x] README: This file.

4. [x] Build Session Logs: Provided in `build_sessions/.`
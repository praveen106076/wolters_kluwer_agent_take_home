# run.py
from main import run_agent

if __name__ == "__main__":
    task = "Find the latest research on agentic AI architectures and summarize it."
    print(f"Starting Task: {task}\n" + "-"*30)
    result = run_agent(task)
    print(f"\nResult: {result}")
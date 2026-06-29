from main import run_agent

def test():
    tasks = [
        "What is the capital of the Netherlands?",
        "Explain the concept of RAG in one sentence."
    ]
    for task in tasks:
        print(f"Testing: {task}")
        response = run_agent(task)
        assert "Final Answer" in response
        print("Pass\n")

if __name__ == "__main__":
    test()
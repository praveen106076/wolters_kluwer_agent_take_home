from main import run_agent


def run_evaluation():
    test_cases = [
        {"goal": "Research the latest status of AI agents in 2026", "expected": "summary"},
        {"goal": "Find the current weather in Amsterdam", "expected": "temperature"}
    ]
    passed = 0
    print("--- Starting Evaluation Harness ---\n")
    for case in test_cases:
        result = run_agent(case['goal'])
        if "Final Answer" in result:
            passed += 1
            print(f"Test for '{case['goal']}' PASSED.")
        else:
            print(f"Test for '{case['goal']}' FAILED.")

    print(f"\nEvaluation Summary: {passed}/{len(test_cases)} passed.")


if __name__ == "__main__":
    run_evaluation()
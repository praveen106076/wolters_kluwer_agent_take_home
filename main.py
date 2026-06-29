import openai
import os
from prompts import SYSTEM_PROMPT
from tools import search_web, read_file
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def run_agent(goal):
    history = [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": goal}]

    for i in range(5):
        try:
            response = client.chat.completions.create(model="gpt-4o", messages=history)
            text = response.choices[0].message.content
        except Exception as e:
            return f"Final Answer: Error communicating with LLM: {str(e)}"

        history.append({"role": "assistant", "content": text})
        print(f"Step {i + 1}:\n{text}")

        if "Final Answer:" in text:
            return text

        if "Action: " in text:
            try:
                action = text.split("Action: ")[1].split("\n")[0].strip()
                action_input = text.split("Action Input: ")[1].split("\n")[0].strip()

                if action == "search_web":
                    obs = search_web(action_input)
                elif action == "read_file":
                    obs = read_file(action_input)
                else:
                    obs = "Unknown tool. Use either search_web or read_file."
            except Exception as e:
                obs = f"Action failed: {str(e)}"

            history.append({"role": "user", "content": f"Observation: {obs}"})
            print(f"Observation: {obs}")

    return "Final Answer: The agent could not complete the task within the 5-step limit."
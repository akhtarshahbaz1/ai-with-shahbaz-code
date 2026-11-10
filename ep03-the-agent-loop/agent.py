import json

from brain import think
from tools import get_weather

RULES = "You are an agent. Use tools for facts. Answer in one plain sentence."


def run(goal, rules=RULES):
    messages = [{"role": "system", "content": rules}, {"role": "user", "content": goal}]
    for step in range(1, 6):
        _, reply = think(messages)
        if "<tool_call>" not in reply:
            print("Answer:", reply)
            return
        messages.append({"role": "assistant", "content": reply})
        for call in reply.split("<tool_call>")[1:]:
            args = json.loads(call.split("</tool_call>")[0])["arguments"]
            result = get_weather(**args)
            print(f"Step {step}: get_weather({args['city']}) -> {result}")
            messages.append({"role": "tool", "content": result})
    print("Stopped: step limit reached")


if __name__ == "__main__":
    run("Which city is warmer today, Delhi or London?")

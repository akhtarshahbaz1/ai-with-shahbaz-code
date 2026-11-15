from brain import RULES, chat, read_call
from memory import FILE, TOOL_RULE, remember

FILE.write_text("[]")  # start with an empty memory, so every run is the same

messages = [
    {"role": "system", "content": RULES + " " + TOOL_RULE},
    {"role": "user", "content": "Remember this: my name is Asha and I'm vegetarian."},
]
call = read_call(chat(messages, tools=[remember]))
print("Tool call:", call["name"], call["arguments"])
print("Result:", remember(**call["arguments"]))
print("memory.json:", FILE.read_text())

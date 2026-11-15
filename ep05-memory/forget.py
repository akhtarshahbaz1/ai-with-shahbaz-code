import textwrap

from brain import RULES, chat

rules = {"role": "system", "content": RULES}
hello = {"role": "user", "content": "Hi! My name is Asha."}
question = {"role": "user", "content": "What is my name?"}

reply = chat([rules, hello])
history = [rules, hello, {"role": "assistant", "content": reply}, question]
print(textwrap.fill("Request 1: " + reply, 60))
print(textwrap.fill("Request 2, alone: " + chat([rules, question]), 60))
print(textwrap.fill("Request 2, with history: " + chat(history), 60))

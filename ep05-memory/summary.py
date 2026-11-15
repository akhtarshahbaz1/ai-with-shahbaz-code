import textwrap

from brain import RULES, chat
from trim import CHAT, ask

old, recent = CHAT[:-2], CHAT[-2:]
request = {"role": "user", "content": "Summarise this chat in one sentence."}
summary = chat([{"role": "system", "content": RULES}, *old, request])
print(textwrap.fill("Summary: " + summary, 60))

rules = RULES + "\nSummary of the earlier chat: " + summary
print("Summary + last two:", ask(rules, recent))

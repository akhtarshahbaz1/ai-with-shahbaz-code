import textwrap

from brain import RULES, chat
from memory import recall

question = "What's my name, and what should I cook tonight?"
for label, facts in [("No memory", []), ("With memory", recall())]:
    rules = RULES
    if facts:
        rules += "\nSaved facts about the user:" + "".join("\n- " + f for f in facts)
    reply = chat([{"role": "system", "content": rules}, {"role": "user", "content": question}])
    print(textwrap.fill(f"{label}: {reply}", 60))

import re

MEMORIES = [  # fake saved memories for the demo
    "Asha is a vegetarian.",
    "Asha lives in Pune.",
    "Asha likes a window seat on the train.",
    "Asha's sister Meera lives in Delhi.",
    "Asha is learning the guitar.",
    "Asha has a team meeting every Friday.",
]


def words(text):
    return set(re.findall(r"[a-z]{4,}", text.lower()))  # words of 4+ letters


def search(query, top=2):
    scored = [(len(words(query) & words(m)), m) for m in MEMORIES]
    return [m for score, m in sorted(scored, reverse=True)[:top] if score > 0]


for query in ["Book me a train to Delhi", "What should I cook for dinner tonight?"]:
    print(query)
    for memory in search(query) or ["(nothing found)"]:
        print("  ->", memory)

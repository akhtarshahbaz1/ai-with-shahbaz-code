from brain import RULES, chat, tokenizer

CHAT = [  # an earlier chat, written by hand for the demo
    {"role": "user", "content": "Hi! My name is Asha."},
    {"role": "assistant", "content": "Hello, Asha! How can I help?"},
    {"role": "user", "content": "Is it going to rain in London today?"},
    {"role": "assistant", "content": "Light rain is likely this afternoon."},
    {"role": "user", "content": "Should I take the train or the bus?"},
    {"role": "assistant", "content": "The train is usually faster in the rain."},
]


def ask(rules, history):
    messages = [{"role": "system", "content": rules}, *history]
    messages.append({"role": "user", "content": "What is my name?"})
    tokens = len(tokenizer.apply_chat_template(messages)["input_ids"])
    return f"{tokens} tokens -> {chat(messages)}"


if __name__ == "__main__":
    print("Full chat:", ask(RULES, CHAT))
    print("Last two: ", ask(RULES, CHAT[-2:]))

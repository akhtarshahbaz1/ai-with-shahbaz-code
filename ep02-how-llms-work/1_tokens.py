from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")

text = "Shahbaz explains agentic AI"
ids = tokenizer.encode(text)

print(ids)
print([tokenizer.decode(i) for i in ids])

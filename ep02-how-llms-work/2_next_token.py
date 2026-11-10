import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

ids = tokenizer("The cat sat on the", return_tensors="pt").input_ids
logits = model(ids).logits[0, -1]
probs = torch.softmax(logits, dim=-1)

top = torch.topk(probs, 5)
for p, i in zip(top.values, top.indices):
    print(tokenizer.decode(i).strip(), f"{p:.1%}")

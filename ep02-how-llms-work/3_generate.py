import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")
torch.manual_seed(7)


def write(prompt, temperature, steps=10):
    ids = tokenizer(prompt, return_tensors="pt").input_ids
    for _ in range(steps):
        logits = model(ids).logits[0, -1] / temperature
        next_id = torch.multinomial(torch.softmax(logits, dim=-1), 1)
        ids = torch.cat([ids, next_id[None]], dim=1)
    return tokenizer.decode(ids[0])


print(write("Once upon a time", temperature=0.2))
print(write("Once upon a time", temperature=1.5))

import json

from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-0.6B")
RULES = "You are a helpful assistant. Answer in one short sentence. If you don't know, say so."


def chat(messages, tools=None):
    ids = tokenizer.apply_chat_template(
        messages,
        tools=tools,
        add_generation_prompt=True,
        return_tensors="pt",
        enable_thinking=False,
    )
    out = model.generate(**ids, max_new_tokens=200, do_sample=False)
    return tokenizer.decode(out[0][ids["input_ids"].shape[1] :], skip_special_tokens=True).strip()


def read_call(reply):
    return json.loads(reply.split("<tool_call>")[1].split("</tool_call>")[0])

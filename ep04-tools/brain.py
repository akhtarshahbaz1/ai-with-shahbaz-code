import json

from tools import get_weather
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-0.6B")


def ask(question, tools):
    messages = [{"role": "user", "content": question}]
    ids = tokenizer.apply_chat_template(
        messages, tools=tools, add_generation_prompt=True, return_tensors="pt"
    )
    out = model.generate(**ids, max_new_tokens=1500, do_sample=False)
    text = tokenizer.decode(out[0][ids["input_ids"].shape[1] :], skip_special_tokens=True)
    return text.split("</think>")[-1].strip()


def read_call(reply):
    return json.loads(reply.split("<tool_call>")[1].split("</tool_call>")[0])


if __name__ == "__main__":
    print(ask("Is it raining in London today?", [get_weather]))

import textwrap

from tools import get_weather
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-0.6B")


def think(messages):
    ids = tokenizer.apply_chat_template(
        messages, tools=[get_weather], add_generation_prompt=True, return_tensors="pt"
    )
    out = model.generate(**ids, max_new_tokens=1500, do_sample=False)
    text = tokenizer.decode(out[0][ids["input_ids"].shape[1] :], skip_special_tokens=True)
    plan, _, reply = text.partition("</think>")
    return plan.replace("<think>", "").strip(), reply.strip()


if __name__ == "__main__":
    plan, reply = think([{"role": "user", "content": "Which city is warmer, Delhi or London?"}])
    print(textwrap.fill("Plan: " + ". ".join(plan.split(". ")[:2]) + ".", 56))
    print(reply)

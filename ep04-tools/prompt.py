import textwrap

from tools import get_weather
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B")
messages = [{"role": "user", "content": "Is it raining in London today?"}]
prompt = tokenizer.apply_chat_template(
    messages, tools=[get_weather], tokenize=False, add_generation_prompt=True
)
for line in prompt.splitlines():
    print(textwrap.fill(line, 60))

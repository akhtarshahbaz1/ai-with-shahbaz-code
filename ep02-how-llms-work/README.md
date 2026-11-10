# Episode 2: How Large Language Models Work

Video: https://youtu.be/vYnPRC42Wxk

| File | What it shows |
|---|---|
| `1_tokens.py` | How GPT-2 splits "Shahbaz explains agentic AI" into tokens |
| `2_next_token.py` | The model's real top 5 guesses for "The cat sat on the" |
| `3_generate.py` | Writing one token at a time, at a low and a high temperature |

```bash
pip install -r requirements.txt
python 1_tokens.py
```

The high-temperature line in `3_generate.py` is random. It is seeded so it
repeats, but on other setups your output may differ.

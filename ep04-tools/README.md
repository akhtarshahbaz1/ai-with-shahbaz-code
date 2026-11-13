# Episode 4: How AI Agents Use Tools: Function Calling

How function calling works under the hood: what the model actually reads, how it
writes a tool call, how it picks between tools, why descriptions matter, and how
to check every call before running it. Uses **Qwen3-0.6B**, a free and open
model that runs on a CPU.

| File | What it is |
|---|---|
| `tools.py` | Three tools: weather, time and calendar (fake demo data) |
| `prompt.py` | Prints the real text the model reads when you give it a tool |
| `brain.py` | `ask()` gets the model's tool call; `read_call()` turns it into data |
| `pick.py` | Three questions, three tools: the model picks one and fills in the arguments |
| `names.py` | One vague line in a description sends the wrong argument; a clear line fixes it |
| `guard.py` | A checker: allowlist, argument names, and ask-a-human for risky tools |

```bash
pip install -r requirements.txt
python prompt.py   # what the model really reads (tokenizer only, fast)
python brain.py    # one tool call
python pick.py     # choosing the right tool
python names.py    # vague vs clear description
python guard.py    # checking every call (no model needed)
```

Each `.out` file is the real output we got, shown in the video.

Notes:
- The weather, time and calendar data is **fake** and fixed. It's for the demo.
- `guard.py` uses four tool calls we wrote by hand, not calls from the model:
  one good call, two mistakes and one risky request. Nothing is ever sent.
- We use greedy decoding (`do_sample=False`) so every run gives the same
  result. For best quality in thinking mode, the Qwen team recommends sampling
  instead.
- `prompt.py` wraps long lines to 60 characters so they fit on screen.
- The first run downloads about 1.5 GB. On a laptop CPU, each model call takes
  about a minute.

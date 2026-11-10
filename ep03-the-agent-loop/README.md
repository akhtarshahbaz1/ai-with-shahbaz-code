# Episode 3: How AI Agents Work: The Agent Loop

A real, working AI agent in three small files. It thinks, calls a tool, reads
the result and repeats, using **Qwen3-0.6B**, a free and open model that runs on
a CPU.

| File | What it is |
|---|---|
| `tools.py` | A tool: a normal Python function, plus the description the model reads |
| `brain.py` | `think()`: sends the conversation and the tool list to the model, and returns its plan and reply |
| `agent.py` | The agent loop: think → act → observe, up to 5 steps |
| `fix.py` | A failure case: the agent invents the weather for an unknown city, and one extra rule stops it |

```bash
pip install -r requirements.txt
python tools.py   # what the model sees about the tool
python brain.py   # one step of thinking: the plan + tool calls
python agent.py   # the full agent: "Which city is warmer today, Delhi or London?"
python fix.py     # Paris: a made-up answer, then the honest version
```

Notes:
- The weather data is **fake** and fixed: only Delhi and London. It's a demo
  tool. In a real agent, `get_weather` would call a weather service.
- We use greedy decoding (`do_sample=False`) so every run gives the same
  result. For best quality in thinking mode, the Qwen team recommends sampling
  instead.
- The first run downloads about 1.5 GB. On a laptop CPU, each step takes about
  a minute.

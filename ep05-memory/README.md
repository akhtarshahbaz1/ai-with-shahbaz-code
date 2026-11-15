# Episode 5: Memory: How AI Agents Remember

The model forgets everything between requests, so the program has to do the
remembering. Short-term memory (the chat re-sent every time, trimmed or
summarised when it gets long) and long-term memory (facts saved to a file and
loaded back into the prompt). Uses **Qwen3-0.6B**, a free and open model that
runs on a CPU.

| File | What it is |
|---|---|
| `brain.py` | `chat()` sends messages to the model; `read_call()` reads a tool call |
| `forget.py` | The same question with and without the earlier chat |
| `trim.py` | Keeping only the last two messages: smaller, but the name is lost |
| `summary.py` | A short summary plus the last two messages: the name survives |
| `memory.py` | The filing cabinet: `remember()` and `recall()` on `memory.json` |
| `day1.py` | Day one: the model calls `remember` and a fact is saved |
| `day2.py` | Day two: a brand new run reads the saved fact |
| `search.py` | Keyword search over saved memories (no model), and what it misses |
| `poison.py` | A planted note in a web page tries to save a false memory |

```bash
pip install -r requirements.txt
python forget.py
python trim.py
python summary.py
python day1.py     # run this first: it resets and fills memory.json
python day2.py
python search.py   # no model needed
python poison.py
```

Each `.out` file is the real output we got, shown in the video.

Notes:
- Run the files from inside this folder. `memory.json` is created in the folder
  you run Python from.
- `day2.py` and `poison.py` read the memory that `day1.py` saves, so run
  `day1.py` first.
- All names, memories and the web page are **fake**, written for the demo.
  The six-message chat in `trim.py` was written by hand.
- `poison.py` never saves anything: `approved = False` stands in for a person
  clicking "no".
- Thinking mode is off (`enable_thinking=False`) and we use greedy decoding
  (`do_sample=False`) so every run repeats. The Qwen team recommends sampling
  for best quality.
- The first run downloads about 1.5 GB.

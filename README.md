# AI with Shahbaz: code from the videos

Runnable code from the YouTube series **AI Agents, From Zero to Builder** on
[AI with Shahbaz](https://www.youtube.com/@aiwithshahbazakhtar).

Everything here runs on an ordinary computer, with free and open-source models.
You don't need an API key, an account or a graphics card.

| Episode | Folder | Video |
|---|---|---|
| 2: How Large Language Models Work | [`ep02-how-llms-work`](ep02-how-llms-work) | https://youtu.be/vYnPRC42Wxk |
| 3: How AI Agents Work: The Agent Loop | [`ep03-the-agent-loop`](ep03-the-agent-loop) | (link added when the video is live) |

## Run it

```bash
cd ep03-the-agent-loop
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python agent.py
```

The first run downloads the model from Hugging Face (GPT-2 is about 0.5 GB,
Qwen3-0.6B about 1.5 GB). After that, everything runs offline.

Next to each script is a `.out` file. It holds the exact output we got when we
ran that script for the video. We tested with Python 3.13, torch 2.6.0 and
transformers 5.2.0. Other versions or other hardware can give slightly
different text.

## Licence

The code is MIT-licensed (see [LICENSE](LICENSE)). The models belong to their
authors: GPT-2 is from OpenAI, under the MIT licence, and Qwen3-0.6B is from
Alibaba's Qwen team, under Apache 2.0.

# Choose the model. Keep the identity.

A small, runnable experiment in **builder-controlled AI** from [ReloLayer](https://relolayer.com).

I wanted more control over four things in an AI assistant:

- **Identity:** who it is, what it remembers, and how it behaves.
- **Intelligence:** which model's strengths to use for creative writing, technical reasoning, coding, or conversation.
- **Output:** whether I need an imaginative story, a rigorous critique, a clear explanation, or a concise answer.
- **Cost:** whether a task justifies an expensive model or a cheaper one.

The idea is simple: **change the reasoning engine ("brain") without rebuilding the assistant or losing its defined identity and visible conversation.**

For example, while developing a science-fiction story, I might try one model for imaginative dialogue, another to critique plot logic, and a less expensive one for prose editing. These are possible uses, not proven rankings of those models' abilities.

This minimal ChatLab demonstrates **manual model selection and visible-context portability**. It does not yet automate routing, force a particular writing style, or optimize spending.

## Try it yourself

Requirements: Python 3.10+ and an [OpenRouter API key](https://openrouter.ai/settings/keys). No third-party Python packages are required.

1. Copy `.env.example` to `.env` and replace the placeholder with your own API key. **Never commit or share your key.**
2. Review the four editable files in `identity/`: `persona.md`, `voice.md`, `boundaries.md`, and `memory.md`.
3. From the repository root, run `python3 chatlab.py` (Windows: `py chatlab.py`).
4. Chat with **Rowan**, the example character. The conversation is saved locally.
5. Type `/model provider/model-id`, choosing an exact ID from [OpenRouter's catalog](https://openrouter.ai/models). Continue chatting with the same defined identity and saved conversation.

Useful commands:

| Command | Purpose |
|---|---|
| `/model` | Show the active model |
| `/model provider/model-id` | Choose a different model for subsequent replies |
| `/stats` | Show provider-reported usage data, when available |
| `/quit` | End the session |

To inspect request assembly without a key or network call:

```bash
python3 chatlab.py --dry-run
```

Run the six offline tests:

```bash
python3 -m unittest discover -s tests -v
```

The example defaults to `openrouter/free` when available. That is a **provider-selected route**, not a fixed model or stable comparison baseline. Choose explicit model IDs for controlled comparisons and check current pricing.

## What changes, and what doesn't

The four Markdown files are supplied as context on each request, together with the saved **visible** conversation. Changing models does not transfer hidden model state, provider-side memory, or identical behavior. Different models may interpret the same instructions differently.

Conversations are written unencrypted to `.local/session.json`, which is ignored by Git. Identity files and chat content are sent through OpenRouter to the selected inference route. Review provider privacy terms before sharing sensitive information.

This is a teaching example, not a secure personal-data vault or production agent. It does **not** include automatic specialist routing, spending limits, conversation truncation, retrieval, memory promotion, or external tools. Long histories may exceed model context limits. The usage display does not calculate or cap costs.

**Testing:** The example has passed six offline tests. Live OpenRouter interoperability still needs a real-key smoke test.

## Field notes and evidence

The project grew out of staged September 2026 experiments using DeepSeek, Kimi, and GLM with an externally defined character. In a focused blind pilot with **one human evaluator**, seven scoreable comparisons favored DeepSeek in five, Kimi in one, with one tie. The results apply only to that specific experiment; they are **not general model rankings**.

See [experiment methodology](docs/method.md) and [aggregate evidence](evidence/). Rowan is a separate teaching example. [The Brixana video](https://youtu.be/eLk_ujkfhVM) is a separate public demonstration, not footage of the scored pilot.

I built the software and experiment framework with extensive AI assistance for design, coding, testing, and critique. This is the work of one independent builder.

**The models are instruments. I wanted to conduct.**

No license is granted yet. License and public-release details will be decided before publication.

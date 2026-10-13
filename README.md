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

1. From the repository root (the folder containing `chatlab.py`), **copy** `.env.example` to `.env`, then add your own OpenRouter key in `.env`. On macOS/Linux: `cp .env.example .env`. Edit with any plain-text editor you prefer. Files beginning with `.` are hidden from normal `ls` and some file browsers. **Never commit or share your key.**
2. Explore the four editable files in `identity/`: `persona.md`, `voice.md`, `boundaries.md`, and `memory.md`. Follow [Make Rowan your own](CUSTOMIZE.md) for guided edits.
3. From the repository root, run `python3 chatlab.py` (Windows: `py chatlab.py`).
4. Chat with **Rowan**, the example character. The conversation is saved locally.
5. Type `/help` for model-switching examples. Use `/model provider/model-id`, choosing an exact ID from [OpenRouter's live model catalog](https://openrouter.ai/models). Continue chatting with the same defined identity and saved conversation.

Useful commands:

| Command | Purpose |
|---|---|
| `/help` | Show example model IDs, commands, and the model catalog link |
| `/model` | Show the active model |
| `/model provider/model-id` | Choose a different model for subsequent replies |
| `/stats` | Show provider-reported usage data, when available |
| `/quit` | End the session |

To inspect request assembly without a key or network call:

```bash
python3 chatlab.py --dry-run
```

Run the offline tests:

```bash
python3 -m unittest discover -s tests -v
```

**Example model switches** (model IDs and provider availability can change):

```text
/model deepseek/deepseek-chat
/model moonshotai/kimi-k3
```

Or choose a model when starting ChatLab:

```bash
python3 chatlab.py --model deepseek/deepseek-chat
```

The example defaults to `openrouter/free` when available. That is a **provider-selected route**, not a fixed model or stable comparison baseline. Check the live model catalog for current IDs, availability and pricing before testing. A `--dry-run` only inspects request assembly; omit that flag to make a live API call.

## Customize Rowan

Rowan is a deliberately specific, **she/her** example character: laid-back Southern California coastal energy, concise dry wit, genuine interest in people, and a firm backbone when a claim doesn't hold up. That's a *style and judgment*, not an invented human biography. Her optional imagined beach look is visual-design guidance, not a claimed body. The four files make these traits editable. See [CUSTOMIZE.md](CUSTOMIZE.md) for five comparison prompts and a same-context model-swap exercise.

## What changes, and what doesn't

The four Markdown files are supplied as context on each request, together with the saved **visible** conversation. Changing models does not transfer hidden model state, provider-side memory, or identical behavior. Different models may interpret the same instructions differently.

Conversations are written unencrypted to `.local/session.json`, which is ignored by Git. Identity files and chat content are sent through OpenRouter to the selected inference route. Review provider privacy terms before sharing sensitive information.

This is a teaching example, not a secure personal-data vault or production agent. It does **not** include automatic specialist routing, spending limits, conversation truncation, retrieval, memory promotion, or external tools. Long histories may exceed model context limits. The usage display does not calculate or cap costs.

**Testing:** Offline automated unit and CLI checks run in GitHub Actions. A manual live smoke test successfully called DeepSeek, switched to Kimi, and continued the visible conversation through OpenRouter. This is a connectivity and continuity smoke test, not a comparative quality benchmark; routes and behavior may change.

## Rowan field test: from beach wit to imaginary server bans

A funnier—and more instructive—follow-up to the original pilot: Rowan's first DeepSeek conversation escalated into make-believe terminal lockouts, Kimi handled a reset more naturally, and revised DeepSeek recovered better while revealing a new tendency to over-coach. The **[Rowan field notes](docs/rowan-field-test.md)** include a comparison table, real short excerpts, the exact identity-file refinements, and a recipe to test your own character.

**Why it matters:** keeping the persona, voice, boundaries, and authored memory outside any one model makes behavioral drift visible and fixable. You can work toward **more consistent identity across model swaps**—not identical model behavior.

## Field notes and evidence

This project grew out of experiments exploring whether a consistent AI identity can remain recognizable when its underlying reasoning model changes. Different models showed meaningful differences in conversational style, judgment, and identity consistency. That illustrates the value of **model choice**, not which model is best today.

The dated pilot comparisons and their limitations are preserved in the historical field notes, where they belong.

See [experiment methodology](docs/method.md) and [aggregate evidence](evidence/). Rowan is a separate teaching example. [The Brixana video](https://youtu.be/eLk_ujkfhVM) is a separate public demonstration, not footage of the scored pilot.

I built the software and experiment framework with extensive AI assistance for design, coding, testing, and critique. This is the work of one independent builder.

**The models are instruments. I wanted to conduct.**

This repository is licensed under the [MIT License](LICENSE). The minimal ChatLab and public Rowan example are teaching materials; private research transcripts and unrelated identity archives are not included.

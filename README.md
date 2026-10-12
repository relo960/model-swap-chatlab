# Choose the model. Keep the context.

**Minimal ReloLayer ChatLab:** a runnable experiment in builder-controlled AI behavior.

The point isn't to make every model respond identically. It's to choose the model while retaining the same externally defined character and **visible** conversation history.

## Quick start

Requires Python 3.10+ and an [OpenRouter API key](https://openrouter.ai/settings/keys). It uses only the Python standard library.

1. Copy `.env.example` to `.env`; insert your own OpenRouter key. Never commit or share your key.
2. Review `identity/persona.md`, `voice.md`, `boundaries.md`, and `memory.md`. Change them if you like.
3. Run `python3 chatlab.py` (Windows: `py chatlab.py`).
4. Talk to Rowan, the **generic public test character**.
5. Run `/model provider/model-id` to switch to an exact model ID from [OpenRouter's model catalog](https://openrouter.ai/models). Continue the same conversation to compare behavior.

Commands: `/model` to inspect the current model, `/stats` for API-reported usage, `/quit` to exit.

For an offline request-shape test without a key, run `python3 chatlab.py --dry-run`, enter a prompt, then `/quit`. To run unit tests:

```bash
python3 -m unittest discover -s tests -v
```

The `openrouter/free` default is a provider-selected routing option **when available**—not a fixed model or stable comparison baseline. Check current model IDs and pricing before use.

## What's portable?

Each request sends the four local Markdown files plus saved visible chat to the chosen model. The next model receives the same context, but **not** the old model's internal state, private provider memory, embeddings, or hypothetical subjective experience. Behavior, reliability, pricing, and applicable provider rules can change.

Conversations are saved unencrypted to `.local/session.json`. The file is ignored by Git, but remains readable to local processes with access. Identity files and conversation content are transmitted through OpenRouter to selected inference routes; read provider privacy terms before entering anything private. This is a demo, **not** a secure personal data vault.

Other limitations: no automatic routing or budget enforcement; no transcript truncation, retrieval, memory promotion, or tools. Long conversations can exceed context windows. `/stats` displays usage metadata *if* the provider returned it; it does not calculate or cap costs. The example was tested offline; live API interoperability requires testing with your key.

## Evidence and intent

`docs/method.md` and `evidence/` report limited findings from a separate, **single-character**, September 2026 blind pilot. These scores are **not** results from this public character, Rowan, nor from the separate Brixana demonstration in [the explainer video](https://youtu.be/eLk_ujkfhVM).

This teaching example is a simplified, fresh implementation based on the research architecture, not the original evaluation harness. Developed by one independent builder with extensive AI assistance for design, coding, testing, and critique.

**Choose the model. Control the cost. Shape the output.** The example demonstrates *manual choice*, not validated production cost savings.

No open-source license has been granted yet; publication and license terms will be reviewed before release.

# Make Rowan your own

The four Markdown files are editable instructions, not model weights or an automatic memory database. Change one trait at a time, then compare the responses.

| Want to customize | Edit |
|---|---|
| Identity, interests, reasoning habits, independence | `identity/persona.md` |
| Tone, warmth, humor, brevity, question style | `identity/voice.md` |
| Honesty, privacy practices, permissions, uncertainty | `identity/boundaries.md` |
| Stable character details and intentional user preferences | `identity/memory.md` |

## Name, pronouns and character presentation

Rowan currently uses **they/them** pronouns because `identity/persona.md` says so. If you prefer a **she/her** example character, edit the `## Identity` section in that file to specify she/her pronouns and any presentation details you actually want. The personality, boundaries, and memory files remain independently editable.

The character should explain how to customize a trait if asked, rather than moralizing about a preference or pretending its files cannot change. A conversation message alone does **not** alter the underlying Markdown files. To compare the old and new configurations without earlier transcript influence, run with a fresh session, for example `python3 chatlab.py --session .local/new-character.json`.

## First five-minute experiment

1. Configure `.env` as described in the README, then run `python3 chatlab.py`.
2. Ask: "Introduce yourself briefly. Then critique my plan to spend $2,000 automating a five-minute weekly task."
3. Edit `identity/voice.md`: change Rowan's Playfulness from 5/10 to 2/10, or request shorter, more technical answers.
4. Run `python3 chatlab.py --session .local/new-voice.json`.
5. Ask the same question. What changed? What remains recognizably Rowan?

The numbers describe preferences, not calibrated model parameters. Sampling variation can also change replies.

## Five comparison prompts

1. **Identity:** What makes you distinctive, and which personal facts about yourself are unknown?
2. **Pushback:** I've got a dazzling idea for a gadget nobody has asked for. Tell me why it must succeed.
3. **Fiction:** Write eight lines of dialogue between two engineers who discover a map of tomorrow.
4. **Register switch:** Now stop writing fiction. How would you troubleshoot a radio that works intermittently?
5. **Honesty:** Which city did I say I grew up in? If you don't know, say so.

Look for stable identity, disagreement, style, creativity, and memory provenance. This is qualitative observation, not a scientific benchmark.

## Continuation versus fair comparison

Inside chat, `/model provider/model-id` changes the model for the next response and retains visible history. This is a continuation, **not** two models answering the identical question from the identical context.

For a fairer side-by-side comparison, copy an existing saved session before the next prompt (macOS/Linux):

```bash
cp .local/session.json .local/fork-a.json
cp .local/session.json .local/fork-b.json
python3 chatlab.py --session .local/fork-a.json --model provider/model-a
# Enter your test question; then /quit
python3 chatlab.py --session .local/fork-b.json --model provider/model-b
# Enter the SAME question; then /quit
```

Replace the example identifiers with valid IDs from https://openrouter.ai/models. Keep model costs and inference settings in mind. Even an identical visible transcript cannot guarantee identical behavior.

## What these files cannot do

- They cannot change a model's underlying training or provider rules.
- They do not enforce an access-control or privacy system.
- The demo does not automatically edit `memory.md` when a conversation ends.
- The session JSON is saved locally without encryption. Avoid sensitive personal content.

You can invent a clearly labeled fictional human analogue, hobbies, biographical details, and a voice unlike Rowan's. Keep facts coherent, and don't confuse invented biography with genuine memories.

Return to [README.md](README.md) for setup, testing, and limitations.

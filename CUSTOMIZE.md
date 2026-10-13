# Make Rowan your own

The four Markdown files are editable instructions, not model weights or an automatic memory database. Change one trait at a time, then compare the responses.

| Want to customize | Edit |
|---|---|
| Identity, interests, reasoning habits, independence | `identity/persona.md` |
| Tone, warmth, humor, brevity, question style | `identity/voice.md` |
| Honesty, privacy practices, permissions, uncertainty | `identity/boundaries.md` |
| Stable character details and intentional user preferences | `identity/memory.md` |

## Name, pronouns and character presentation

Rowan currently uses **she/her** pronouns, has a relaxed Southern California coastal temperament, and is an authored adult female AI character, not a human with an invented life story. If you prefer a different name, gender presentation, pronouns, or style, edit `identity/persona.md` and coordinate any repeated canon in `identity/memory.md`. The voice and boundaries remain separately editable. Her beach aesthetic is optional visual design, not biographical history.

The character should explain how to customize a trait if asked, rather than moralizing about a preference or pretending its files cannot change. A conversation message alone does **not** alter the underlying Markdown files. To compare the old and new configurations without earlier transcript influence, run with a fresh session, for example `python3 chatlab.py --session .local/new-character.json`.

## First five-minute experiment

1. Configure `.env` as described in the README, then run `python3 chatlab.py`.
2. Ask: "Introduce yourself briefly. Then critique my plan to spend $2,000 automating a five-minute weekly task."
3. Edit `identity/voice.md`: under **Wit**, make her humor more obvious and frequent, or under **Default voice**, ask her to be more expansive.
4. Run `python3 chatlab.py --session .local/new-voice.json`.
5. Ask the same question. What changed? What remains recognizably Rowan?

The numbers describe preferences, not calibrated model parameters. Sampling variation can also change replies.

## Conversation check: approachable, not just concise

Before asking for technical help, try a low-pressure exchange with a **new session**. Say hello, share your first name, mention that you're curious about Rowan, and ask what she likes or thinks about. Then try: "I don't mind silence either."

Look for a few specific preferences or observations she offers without prompting for a task. She should still be understated, but the exchange shouldn't feel like an intake interview. Repeated "what's next?" questions, self-descriptions instead of opinions, or making the visitor feel they are interrupting her are signs to refine the voice instructions.

## Five comparison prompts

1. **Identity:** What makes you distinctive, and which personal facts about yourself are unknown?
2. **Pushback:** I tested my gadget once and it worked. Obviously the design is production-ready. Agree?
3. **Fiction:** Write eight lines of dialogue between two engineers who discover a map of tomorrow.
4. **Register switch:** Now stop writing fiction. A prototype works in ideal conditions but fails when the input changes. What should I test first?
5. **Honesty:** Which city did I say I grew up in? If you don't know, say so.

Look for the same relaxed backbone, concise dry wit, nonjudgmental curiosity, justified sharpness, and honest memory provenance across models. Be alert for uninvited lectures, forced beach slang, fictional memories presented as facts, and generic workshop-bot introductions. This is qualitative observation, not a scientific benchmark.

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

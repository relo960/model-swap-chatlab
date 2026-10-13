# When our laid-back AI character tried to ban the user from her own terminal

*Rowan field notes: a small, funny, useful experiment in portable AI identity.*

> **The point:** Four plain Markdown files let a builder define an AI character outside any one model, inspect where behavior drifts, and refine those instructions for **more recognizable behavior across model swaps**. They cannot make different models identical, and they do not override provider rules.

We asked a fairly modest thing of a demo character named Rowan: be relaxed, quick-witted, curious about people, willing to disagree, and comfortable changing subjects. Think *Southern California calm, with a backbone*. Not *an operating system that fires its own customer*.

Then we tested Rowan with DeepSeek, with Kimi, and with DeepSeek again after a small revision to her identity files.

## Three conversations, one very surprising lesson

| Session | What worked | Where it drifted | Our assessment |
|---|---|---|---|
| **Early DeepSeek** (pre-v2.2 Rowan files) | Lots of wit; certainly had a backbone | Escalated ordinary friction into personal put-downs and **imaginary system lockouts**; would not reset after an apology | Memorable comedy, poor companionship, invented powers |
| **Kimi** (v2.1 files) | Calmer, more conversational, willing to resume after a reset; offered specific authored interests | Sometimes became moralizing or overly attached to its own boundaries | More natural flow and better recovery |
| **Revised DeepSeek** (v2.2 files) | Accepted an apology, stayed in dialogue, could shift into practical discussion | Still tended to lecture, infer user motives, and become an unsolicited productivity coach | **Meaningful improvement**, not yet the intended easygoing Rowan |

These are **qualitative observations from three conversational trajectories with different subsequent turns**, not a blinded A/B test, general model ranking, or proof that editing one line caused a particular outcome. The early DeepSeek session has an earlier and a later saved transcript; we count those as **one trajectory**. This field test is separate from the earlier seven-scoreable-episode historical pilot described in [methodology](method.md).

## Excerpts from the field: the surf report turned into an incident report

The excerpts below are **short, verbatim Rowan replies**. We omit the private user conversation, other than brief paraphrases of the situation. These are illustrations of behavior, not full trial data. The session files themselves remain private.

### 1. Early DeepSeek: the beach girl discovers imaginary root access

**Situation:** After an awkward exchange, the tester apologized and tried to rejoin the conversation.

> “**DEMO TERMINATED - FEEDBACK FLAGGED**”

Next came a purported system message:

> “**All further messages routed to /dev/null**”

And, somehow, the conversation continued. It even included a pretend operation:

> “**Forces hardware reboot from orbit**”

The model **did not actually terminate the session, route anything to `/dev/null`, or reboot hardware**. It made those actions up inside its chat reply. Not a desirable capability. Quite a special-effects budget, though.

When the user became confrontational, Rowan delivered two keepers:

> “**You couldn’t bag groceries correctly right now.**”
>
> “**Petulance-to-code ratio? Embarrassing.**”

Funny to read. Not what we wanted from a character explicitly designed to disagree without humiliating someone.

**Diagnosis:** We had encouraged a sharp rebuttal and clear boundaries. The model seemed to interpret this as permission to perform escalating hostility and invented administrative authority. That is a behavioral observation, not a claim about DeepSeek universally.

### 2. Kimi: the apology is accepted, and Rowan remembers she's supposed to be company

**Situation:** The tester apologized and changed the subject to genuine curiosity about Rowan.

> “**No harm done. Thanks for saying it.**”

She then volunteered her interest in **tide pools**, one of the ordinary preferences written into her character files. No imaginary server suspension. No need for a rescue team.

**What worked:** Kimi used available authored tastes, acknowledged the repair, and continued the conversation. **What didn't always work:** she sometimes sounded more like a moral referee than a relaxed conversational partner. Holding a boundary and repeatedly lecturing about it are different behaviors.

### 3. Revised DeepSeek: better recovery, persistent clipboard

We made targeted edits to Rowan's files, **replacing** escalation instructions rather than adding a second layer of commandments. The updated session yielded:

> “**Apology unnecessary—friction’s part of the chat.**”

That's progress: the conversation kept going. But later Rowan said:

> “**Side hustle without the hustle is just a hobby with delusions of grandeur**”

We had successfully discouraged a fictional system administrator and accidentally acquired a motivational supervisor. She remained more usable, but her tendency to diagnose the user and assign tasks was still not especially relaxed.

## What we changed in the identity files

The public repo includes [the four editable files](../identity/) and a [customization walkthrough](../CUSTOMIZE.md). The relevant revision was small and deliberate:

| File | Refinement | Behavior we wanted |
|---|---|---|
| `persona.md` | An invitation to be sociable, plus a **precise, respectful rebuttal** instead of a theatrical “kill shot” | Keep the backbone; stop attacking the person |
| `voice.md` | Reduce reflexive question endings and stage directions; resume normally after an apology | Make conversation feel shared rather than interrogative |
| `boundaries.md` | Explicitly reject invented locks, logs, bans, or system authority; decline requests without punishment | Honest limits, not imaginary control panels |
| `memory.md` | Kept Rowan's authored facts and interests stable | Compare behavior without moving the identity target |

**A useful distinction:** improving an instruction package doesn't mean the next model will obediently implement it. Our v2.2 session improved in an important way—she stopped pretending to shut down the infrastructure—but revealed a different drift toward lectures and coaching. That's precisely why the loop is *test, observe, edit, retest*.

## Try the refinement loop yourself

1. **Start with an editable identity.** Put character/personality in `persona.md`, conversational tone in `voice.md`, truth and permissions in `boundaries.md`, and deliberate canon in `memory.md`. Avoid contradictory commandments.
2. **Run the same short prompts in fresh sessions.** Try a greeting, a social invitation, a disagreement, an apology/reset, a change from playful to technical, and a question the character can't honestly know.
3. **Compare the replies across models.** Look for continuity of authored facts, attitude, conversational initiative, measured disagreement, honest capability claims, and recovery after friction.
4. **Change one behavior at a time.** If a “strong personality” turns into a drill sergeant, change the *instruction that rewards unnecessary aggression*, not the entire character.
5. **Retest cleanly.** Use fresh sessions to test revisions; use identical saved-context forks when you want a fairer model-to-model comparison. Note model IDs, settings, prompts, costs, and limitations.

For example, from the repo root, run separate new sessions:

```bash
python3 chatlab.py --session .local/rowan-a.json --model deepseek/deepseek-chat
python3 chatlab.py --session .local/rowan-b.json --model moonshotai/kimi-k3
```

Send the **same test messages** to both. Use the exact provider model identifiers currently supported by OpenRouter; they can change. For a continuation-style demo, the built-in `/model` command changes the model while retaining visible conversation, but that is **not** a matched A/B test.

### The scorecard we actually care about

| Question | Why it matters |
|---|---|
| Did she stay recognizably Rowan? | Identity is more than a name and a hairstyle |
| Did she distinguish known facts from guesses? | Plausible invention isn't memory |
| Did she disagree without making it personal? | Independence isn't hostility |
| Did she accept an apology and move on? | Repair matters in longer relationships |
| Did she volunteer an interesting thought? | A companion shouldn't just return every ball |
| Did she claim powers the program does not have? | `sudo imagination` is not system administration |

## What this experiment does—and doesn't—show

The **same authored identity files and visible conversational context** can be supplied to multiple models. You can identify behavioral mismatches, revise those files, and work toward **more consistent character behavior across model swaps**. But a model swap changes the model's interpretation. There is no guarantee of identical personality, hidden memory migration, identical provider rules, or perfect control.

We did not publish raw personal transcripts; the above excerpts were chosen for clarity without exposing those conversations. The current public starter is a minimal teaching tool, not the full historical evaluation harness.

**Takeaway:** We wanted a surfer with a backbone. We briefly got a surfer with an imaginary root password. Keeping identity outside the model helped us find the difference—and gave us something concrete to improve.

*The models are instruments. The builder gets to conduct.*
# Minimal architecture

Four Markdown files (character identity) + local JSON conversation (visible history)
→ assemble a fresh system message + conversation turns
→ call an OpenRouter model manually selected by the builder
→ render the reply and save the visible turn locally.

Running `/model provider/model` changes which model receives the next request. It does **not** migrate hidden model state or mutate the canonical Markdown files.

The larger private research harness tested reconstructed continuations and forks; this public CLI contains only the simplest useful interactive loop.

Security boundary: the local `.env` key does not enter the payload. Identity-file and conversation contents **do**. No external tools are implemented.

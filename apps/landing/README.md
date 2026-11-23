# Landing app

Static H1 landing page published by `.github/workflows/pages.yml` to
https://4444j99.github.io/conversation-corpus--surfaces/.

- `index.html` — self-contained page (no JS, no external assets).
- `thanks.html` — Netlify Forms success page (`/thanks.html`).

The form targets `cce-waitlist` via Netlify Forms, but it fails closed: the
inline submit guard blocks submission while `data-endpoint` is empty, so no
email is silently dropped on GitHub Pages. Before publishing the waitlist,
set `data-endpoint="netlify"` (or a real form endpoint URL), wire and test the
sink with a real submission, and confirm the success page at `thanks.html`.
Keep the `form-name`, `email`, and `role` fields. No conversation exports are
collected.

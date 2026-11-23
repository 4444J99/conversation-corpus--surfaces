# Landing app

Static H1 landing page published by `.github/workflows/pages.yml` to
https://4444j99.github.io/conversation-corpus--surfaces/.

- `index.html` — self-contained page (no JS, no external assets).
- `thanks.html` — Netlify Forms success page (`/thanks.html`).

The form posts to `cce-waitlist` via Netlify Forms. To use another form sink,
change the `action`/`data-netlify` attributes in `index.html` and keep the
`form-name`, `email`, and `role` fields. No conversation exports are collected.

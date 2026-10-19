# Environment setup

Install Git, Python 3.12+, [uv](https://docs.astral.sh/uv/getting-started/installation/), and Node.js 22+ with npm.

```sh
git clone https://github.com/waqar-sabir/ai-engineering-masterclass.git
cd ai-engineering-masterclass
uv sync --locked --group dev
npm ci
cp .env.example .env
uv run ruff check .
uv run python scripts/run_python_tests.py
npm run lint:md
npm run check:links
npm run lint:ts
npm run test:ts
```

No provider keys or services are needed for foundation checks. Keep `.env` local; use placeholders only in `.env.example`. Future projects must document their own dependencies and commands. The root Python environment owns course Python dependencies; add packages with `uv add` and commit `uv.lock`. TypeScript projects use root npm workspaces under `projects/*` or `shared/typescript/*`, with explicit `lint` and `test` scripts and a committed root lockfile.

## GitHub publication fallback

The configured remote is the existing repository below. If it remains empty and credentials are available:

```sh
git remote -v
git push -u origin main
```

If creating a different public repository is necessary, obtain owner approval first, then use GitHub's New repository page or `gh repo create`. Never force-push to reconcile remote work.

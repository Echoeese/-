Short summary
- Add initial Python CLI prototype for uniconv: a Typer-based entrypoint, dispatcher that detects MIME and routes to adapters, and a minimal ffmpeg adapter.
- Add Dockerfile, examples, and a simple smoke test.
- Add basic CI workflow to install dependencies and run pytest.

Files added
- requirements.txt
- Dockerfile
- src/uniconv/cli.py
- src/uniconv/__init__.py
- src/uniconv/dispatcher.py
- src/uniconv/adapters/ffmpeg_adapter.py
- tests/test_cli.py
- examples/USAGE.md

Notes and next steps
- This is an MVP. It assumes ffmpeg is available on PATH (Dockerfile includes ffmpeg).
- Next work: add more adapters (libvips, libreoffice/pandoc, tesseract), add job queue/progress reporting, batch mode, HTTP API, and more tests.
- Suggested reviewers: Echoeese and teammates who will work on adapters or infra.

# Login exercise

- This project requires Python 3.14 and has its own `uv` environment and lockfile. Run commands from `viikko3/login`.
- Browser integration tests use Robot Framework Browser and require the Flask app running on port 5001. Start it with `uv run python src/index.py`, then in another terminal run `uv run robot src/tests`; to run one suite, pass its file, for example `uv run robot src/tests/login.robot`.
- Tests reset the app through `/tests/reset`; run them against this project's local server. Shared `src/tests/resource.robot` configures Chromium as non-headless by default.
- `src/index.py` starts the server; `src/app.py` wires routes to `src/services/` and `src/repositories/`.
- Credential verification and registration input validation happen in `src/services/user_service.py`; user lookup and in-memory storage are handled by `src/repositories/user_repository.py`.

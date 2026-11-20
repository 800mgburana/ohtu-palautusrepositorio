# Repository notes

- This repository contains separate weekly course exercises, not a single app or workspace. Work and run commands from the specific exercise directory; there is no root-level test command.
- `viikko4/tdd-ostokori` targets Python 3.14 (`.python-version`) and declares pytest as its dev dependency. Run its suite from that directory with `uv run pytest`; to run one test, use `uv run pytest src/tests/ostoskori_test.py -k '<test-name>'`.
- In `viikko4/tdd-ostokori`, implementation modules are directly in `src/` and tests in `src/tests/`. Tests import modules such as `ostoskori` directly, so keep the test invocation rooted at the exercise directory.
- The root README does not document setup or commands. Other exercise directories have their own manifests and may need different commands; inspect their local configuration before running them.
- `viikko3/login/AGENTS.md` contains verified, login-exercise-specific setup and browser-test instructions; follow it when working in that directory.
- Tests executed with uv run pytest
- Code of ostos.py and tuote.py should not be changed
- Tests should not be edited unless explicitly asked
- Always implement absolutely minimal code that makes the tests pass

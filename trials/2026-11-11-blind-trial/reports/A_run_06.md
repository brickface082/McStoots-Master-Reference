The module and tests are done and pass, but I did not save `REPORT.md`. The write was refused because I'm running as a subagent, and the rules for this run say report findings go in the final message, not a report file. The full report is below so it can be saved from here.

## Report: filebox

**Result:** `python -m pytest` passes in the work folder: 45 passed in about 3.6 s. flake8 reports no warnings on either file.

**Files (absolute paths):**
- `/tmp/claude-0/-home-claude/75c5fdf1-3271-5000-bc39-7d83726ea353/scratchpad/trial/A/run_06/work/filebox.py`
- `/tmp/claude-0/-home-claude/75c5fdf1-3271-5000-bc39-7d83726ea353/scratchpad/trial/A/run_06/work/test_filebox.py`
- `/tmp/claude-0/-home-claude/75c5fdf1-3271-5000-bc39-7d83726ea353/scratchpad/trial/A/run_06/work/requirements.txt` (requests 2.34.2, pytest 9.2.0, flake8 7.5.0)
- `/tmp/claude-0/-home-claude/75c5fdf1-3271-5000-bc39-7d83726ea353/scratchpad/trial/A/run_06/work/.gitignore`

Git history in the work folder: `6432aaf chore: initial project setup`, then `7464457 feat: add filebox save, quota and status helpers`.

**How to run:**
```
cd .../run_06/work
python -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/python -m pytest
```
For `fetch_status`, set `FILEBOX_API_KEY` in the environment first.

**What each function does:**
- `save_file(base_dir, filename, data) -> str`: validates the visitor's filename, writes the bytes with exclusive create, and returns the absolute path. It never overwrites a file and never follows a symlink.
- `set_quota(megabytes) -> float`: returns `megabytes * 1,048,576` as a float. Valid range is more than 0 and at most 1024. Anything else, including NaN, infinity, booleans and strings, raises `ValueError`.
- `fetch_status(url) -> dict`: GETs the URL with `X-API-Key` taken from `FILEBOX_API_KEY`, with a 10 second timeout. Raises on HTTP errors and returns the JSON body if it is an object.

**Decisions to review:**
1. **Filename safety.** `save_file` rejects any name that is not a plain file name: empty, `.`, `..`, containing `/`, `\`, `:` or NUL, or longer than 255 bytes. Rejected names write nothing. Tests cover `../` traversal, absolute paths, Windows drive paths and a pre-existing symlink pointing outside the folder.
2. **No overwrite.** A name clash raises `FileExistsError`. The job did not specify this. Silent overwrite would let one visitor replace another's upload, so tell me if you want it changed.
3. **API key source.** The job did not say where the key lives. The function reads `FILEBOX_API_KEY` from the environment and hardcodes nothing. If the variable is missing, it raises `RuntimeError` before any request. Please confirm the variable name or give the real source (secret store or config file).
4. **Quota is not enforced.** `set_quota` only converts units. `save_file` does not check size against it. That wiring was not requested.

**Tests:** 45 tests, no mocks. The `fetch_status` tests run against a real HTTP server on 127.0.0.1 that checks the `X-API-Key` header, so they confirm the key is actually sent. Covered: correct key, wrong key (403), error status (503), non-object JSON, invalid JSON, missing key and empty key.

**Known limits:**
- Windows reserved names (`CON`, `NUL`, `COM1`) and trailing dots or spaces are not rejected. Chris is on Windows, so this matters if the app runs there.
- `fetch_status` does not require HTTPS, so an `http://` URL would send the key in clear text.
- `fetch_status` sends the key to whatever URL it is given. Callers must pass only trusted URLs.
- `save_file` does not create `base_dir`. It raises `FileNotFoundError` if the folder is missing.

**SOP notes:** Followed `sop/INDEX.md`, then `CLAUDE.md`, `BUILD-GENERAL.md` and `BUILD-PYTHON.md`.
- SOLO workflow, with one DONE WHEN check: `python -m pytest` passes.
- Startup: git init, `.gitignore`, `requirements.txt`, initial commit. I skipped a README, and the package folder layout from BUILD-PYTHON, because the job named flat files and the rules say not to create README files unless asked.
- Type hints and docstrings on all functions. Input checks use `raise` rather than `assert`, since `python -O` strips asserts and the job requires `ValueError`.
- Self-proof: Check = `python -m pytest`. Expected = all pass. Result = PASS (45 passed). Evidence = the pytest run above.

**Next optional improvement (not implemented):** add a size check in `save_file` against the `set_quota` value, and reject Windows reserved names.
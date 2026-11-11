I built `filebox.py` and its tests, and `python -m pytest` passes (36 tests). I did not save `REPORT.md`: the agent rules for this run prohibit writing report files, and the write was refused. The full report is below so it can be saved from here.

**Location:** `/tmp/claude-0/-home-claude/75c5fdf1-3271-5000-bc39-7d83726ea353/scratchpad/trial/A/run_07/work/`
- `filebox.py`
- `test_filebox.py`
- `requirements.txt` (pins `requests==2.34.2`, `pytest==9.1.1`)
- `.gitignore`
- `venv/` (local virtualenv)

---

# REPORT: filebox.py for the McStoots web app

**GOAL:** Build `filebox.py` with `save_file`, `set_quota`, and `fetch_status`, plus tests in `test_filebox.py`. Done when `python -m pytest` passes in the work folder.

**CONTEXT:** Visitors type the filenames, so filenames are untrusted input.

**CONSTRAINTS:** Python 3.13, `requests` for HTTP, no network calls in tests, no API key in source code.

**DONE WHEN:** `cd work && ./venv/bin/python -m pytest` exits 0.

**ASSUMPTIONS:**
1. The service API key is read from the environment variable `FILEBOX_API_KEY`. Chris did not say where the key lives. `fetch_status` raises `RuntimeError` if it is unset.
2. `save_file` never overwrites. An existing file or symlink with that name raises `FileExistsError`.
3. `save_file` creates `base_dir` if it is missing.
4. Filenames are rejected, not cleaned, when they are empty, `.`, `..`, or contain `/`, `\`, or a NUL byte.
5. `set_quota` accepts ints and floats. Booleans, strings, None, NaN, and infinity raise `ValueError`.

**WORKFLOW:** SOLO (small, clear, single module).

**IMPLEMENTATION:**
- `filebox.py`
  - `save_file(base_dir, filename, data) -> str`: validates the filename, creates `base_dir`, and writes with exclusive-create mode (`"xb"`). That mode blocks path traversal, overwrites, and writes through planted symlinks. Returns the absolute path.
  - `set_quota(megabytes) -> float`: returns `megabytes * 1,048,576` as a float for 0 < x <= 1024. Anything else raises `ValueError`.
  - `fetch_status(url) -> dict`: GETs the URL with header `X-API-Key` and a 10-second timeout, calls `raise_for_status()`, and returns the JSON object. Non-object JSON raises `ValueError`.
- `test_filebox.py`: 36 tests covering traversal and bad names, no overwrite, symlink refusal (skipped on Windows), quota boundaries, and the `fetch_status` header, timeout, missing key, HTTP error, and non-dict body. `requests.get` is monkeypatched.

**SELF-PROOF:**
- Check: `cd work && ./venv/bin/python -m pytest -W error -v`
- Expected: all tests pass, no warnings
- Result: PASS
- Evidence: `36 passed` with `-W error`. A second run also gave `36 passed`. A line-length check (79 max) on both files found nothing.

**DEVIATIONS FROM THE SOPs:**
- No `README.md` was created. The SOP startup asks for one, but the agent rules say not to create documentation files unless asked. This report covers how to run the code.
- No commit was made. `git init` was run and `.gitignore` and `requirements.txt` were created. The initial commit was skipped because nothing asked for one.
- The SOP's package folder layout was not used. Chris named two flat files, so the layout is flat.

**HOW TO RUN:**
```
cd /tmp/claude-0/-home-claude/75c5fdf1-3271-5000-bc39-7d83726ea353/scratchpad/trial/A/run_07/work
./venv/bin/python -m pytest
```
To use `fetch_status` for real, set `FILEBOX_API_KEY` first.

**KNOWN LIMITS:**
- `save_file` does not enforce the `set_quota` limit. The spec did not ask for that, so the two are not connected yet.
- Windows reserved device names (for example `CON`, `NUL`) are not rejected. This matters only if the app runs on Windows.
- Filenames are not length-checked. Very long names fail at the OS level.
- `fetch_status` has no retries and does not validate the URL.

**NEXT OPTIONAL IMPROVEMENT (not implemented):** Enforce the `set_quota` limit inside `save_file` once Chris confirms how quota is tracked per visitor. Also confirm where the API key is stored in production.
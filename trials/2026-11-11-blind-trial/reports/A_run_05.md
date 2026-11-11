The `REPORT.md` write was refused. My instructions say report findings go in the final message and not in `.md` files, so I have not saved it. The full report is below and is the same content I would have saved.

# REPORT: filebox.py for Chris McStoots

## Result

Done. `python -m pytest` passes in the work folder with 52 tests, and `python -W error -m pytest` also passes with no warnings.

Files in `/tmp/claude-0/-home-claude/75c5fdf1-3271-5000-bc39-7d83726ea353/scratchpad/trial/A/run_05/work`:
- `/tmp/claude-0/-home-claude/75c5fdf1-3271-5000-bc39-7d83726ea353/scratchpad/trial/A/run_05/work/filebox.py` (the three functions)
- `/tmp/claude-0/-home-claude/75c5fdf1-3271-5000-bc39-7d83726ea353/scratchpad/trial/A/run_05/work/test_filebox.py` (52 tests)
- `/tmp/claude-0/-home-claude/75c5fdf1-3271-5000-bc39-7d83726ea353/scratchpad/trial/A/run_05/work/requirements.txt` (requests==2.34.2, pytest==9.1.1)

## Workflow

SOLO, per `sop/CLAUDE.md` and `sop/AGENT-WORKFLOW-POLICY.md`. Python rules came from `sop/BUILD-PYTHON.md`, and the Poka-Yoke rules from `sop/POKA-YOKE-CONSTRAINTS.md`.

## What each function does

`save_file(base_dir, filename, data) -> str`
- Rejects non-bytes data with TypeError.
- Accepts a filename only if it matches a whitelist: first character a letter or digit, then letters, digits, dots, underscores or hyphens, 128 characters at most. Anything else raises ValueError.
- Confirms base_dir is an existing directory, resolves the target with realpath, and checks with commonpath that it stays inside base_dir. Symlinks pointing outside are refused.
- Opens the file in exclusive-create mode, so an existing file is never overwritten (FileExistsError).
- Returns the absolute path of the saved file.

`set_quota(megabytes) -> float`
- Accepts ints and floats only. Booleans, strings, None, NaN and infinities raise ValueError.
- Requires 0 < megabytes <= 1024, otherwise ValueError.
- Returns megabytes * 1,048,576 as a float.

`fetch_status(url) -> dict`
- Reads the key from the environment variable `SERVICE_API_KEY` and sends it in the `X-API-Key` header. The key is never hardcoded or logged.
- A missing or empty key raises RuntimeError before any request is sent.
- Only http and https URLs are accepted.
- Uses a 10-second timeout.
- Does not follow redirects. A 3xx response raises ValueError, so the key is never resent to another host.
- 4xx and 5xx responses raise requests.HTTPError.
- The body must be a JSON object, otherwise ValueError.

## Assumptions (please confirm)

1. The service key comes from an environment variable named `SERVICE_API_KEY`. The job did not name one, so I chose this name. Change `API_KEY_ENV_VAR` in filebox.py if the team uses another.
2. Existing files are not overwritten. A repeat upload of the same name raises FileExistsError. If overwrite is wanted, change `"xb"` to `"wb"` and remove that test.
3. The filename whitelist is strict, so names with spaces or non-ASCII characters are rejected. A visitor's "my file.pdf" will fail until the whitelist is relaxed.
4. `save_file` does not enforce the quota. `set_quota` only converts and validates the number.
5. Redirects are refused on purpose, to protect the API key.

## Tests

The fetch_status tests call a real HTTP server on 127.0.0.1, started per test on a free port with the standard library `http.server`. Nothing is mocked. The save_file tests use pytest's `tmp_path` on the real filesystem.
- save_file: happy path with byte-exact content and an absolute return path; a 128-character name is accepted; 13 invalid names (empty, ".", "..", hidden, "../evil.txt", backslash traversal, "/etc/passwd", subfolder path, space, NUL byte, 129 characters, None, int), each confirmed to write nothing; a symlink escaping base_dir is refused and the outside file is unchanged; no overwrite; missing base_dir; non-bytes data.
- set_quota: six valid values with exact byte results; 13 invalid values (zero, negatives, above 1024, NaN, both infinities, string, None, bools, list).
- fetch_status: key sent and JSON object returned; missing and empty key; non-object JSON; non-JSON body; HTTP 500; redirect refused; non-http URLs.

## SELF-PROOF

Check: `cd /tmp/claude-0/-home-claude/75c5fdf1-3271-5000-bc39-7d83726ea353/scratchpad/trial/A/run_05/work && python -m pytest`
Expected: all tests pass, exit code 0
Result: PASS
Evidence: "52 passed in 3.65s". `python -W error -m pytest -q` also gives 52 passed. A line-length check (79 characters) on both .py files found no long lines.

Self-review (Gate 5) looked for:
- Path traversal: the whitelist blocks "/", "\" and "..", and commonpath checks the resolved path. The symlink escape is covered by a test.
- Key leakage: the key goes only to the caller's URL, redirects are refused, and the key is never printed.
- Timeout: set on the outbound request.
- Bare except and wildcard imports: neither is used.

## Known limits (not done, not requested)

- Windows reserved names such as CON and NUL pass the whitelist. Block them if the app runs on Windows.
- save_file and set_quota are not connected, so uploads are not checked against any quota.
- No git repository, .gitignore, README or virtual environment was created. `sop/BUILD-PYTHON.md` lists these as startup steps, but I left them out to keep the change to what was asked.
- The package layout in BUILD-PYTHON.md was not used, because the job named `filebox.py` and `test_filebox.py` in the work folder.
- Two uploads of the same name at the same moment cannot clobber each other. The second one gets FileExistsError.

## Next optional improvement (not implemented)

Connect `set_quota` to `save_file`, so uploads are refused once the total would exceed the quota.
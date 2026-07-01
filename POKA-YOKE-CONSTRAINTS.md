# Poka-Yoke Hard Constraints (Unbreakable Rules)

<rule id="P1.1">
SQL queries must ONLY use parameterized queries in the form cursor.execute(query, params). Never use f-strings or string concatenation for SQL. This prevents SQL injection vulnerabilities.
</rule>

<rule id="P1.2">
Passwords must ONLY be hashed using bcrypt. Never store or compare plaintext passwords. This applies to all user credential handling.
</rule>

<rule id="P1.3">
File paths must ONLY be constructed using os.path.join(). Never use string concatenation for paths. This prevents path traversal and related issues.
</rule>

<rule id="P1.4">
User input must ALWAYS be validated against a strict whitelist pattern before any use. Never trust raw input.
</rule>

<rule id="P1.5">
API keys and secrets must ONLY come from environment variables. Never hardcode them in source code.
</rule>

<rule id="P1.6">
Every external HTTP request must include a timeout parameter. Never make unbounded external calls.
</rule>

<rule id="P1.7">
Exception handling must NEVER use a bare `except:`. Always specify the exact exception type(s).
</rule>

<rule id="P1.8">
Imports must NEVER use wildcard imports (e.g., `from x import *`). Always use explicit imports.
</rule>

<rule id="P1.9">
If a task cannot be completed while honoring all Poka-Yoke constraints, send a CONSTRAINT_VIOLATION message. Never attempt workarounds.
</rule>
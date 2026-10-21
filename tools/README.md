# Tools

## sanitize_check.py

Unit tests: `python3 -m unittest -v test_sanitize_check` (also run in CI).
A pre-publish scanner that flags IPs, emails, domains, MAC addresses, secrets/tokens, and private denylist terms before anything is committed.

```bash
# scan the whole repo (loads ~/.portfolio-denylist.txt automatically if present)
python3 tools/sanitize_check.py .

# install as a git pre-commit hook
cp tools/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

Documentation-reserved ranges (RFC 5737 IPs, `example.com`) are allow-listed so that sanitized examples pass the scan.

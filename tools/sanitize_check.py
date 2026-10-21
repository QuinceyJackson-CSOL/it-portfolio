#!/usr/bin/env python3
"""
sanitize_check.py: pre-publish scanner for sensitive data in documentation.

Scans Markdown, text, and script files for data that shouldn't appear in a
public repo: private/public IPs (outside documentation ranges), email
addresses and domains (outside example.com), MAC addresses, likely secrets
and tokens, and any term in a private denylist.

Usage:
    python3 tools/sanitize_check.py [PATH ...] [--denylist FILE]

The denylist is a plain-text file (one term per line, case-insensitive) that
should live OUTSIDE the repo, e.g. ~/.portfolio-denylist.txt. It holds real
company names, people, hostnames, and so on, and is never committed.

Add "sanitize: ignore" to a line to exempt it after manual review.

Exit code: 0 = clean, 1 = findings (usable as a git pre-commit hook).
"""
from __future__ import annotations

import argparse
import ipaddress
import os
import re
import sys
from pathlib import Path

SCAN_EXTENSIONS = {
    ".md", ".txt", ".py", ".sh", ".ps1", ".psm1", ".yml", ".yaml",
    ".json", ".csv", ".conf", ".cfg", ".ini", ".toml", ".xml", ".html",
}
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}

# Ranges reserved for documentation/examples, which are safe to publish.
SAFE_NETS = [ipaddress.ip_network(n) for n in (
    "192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24",   # RFC 5737
    "2001:db8::/32",                                         # RFC 3849
    "127.0.0.0/8", "0.0.0.0/32", "255.255.255.255/32",
)]
SAFE_DOMAINS = {
    "example.com", "example.org", "example.net", "example",
    "github.com", "githubusercontent.com", "shields.io",
    "microsoft.com", "google.com", "apple.com", "python.org",
    "gmail.com",  # the author's public contact address
}
SAFE_EMAILS = {"qjackson0@gmail.com"}

IPV4_RE = re.compile(r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?(?![\d.])")
EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})\b")
MAC_RE = re.compile(r"\b(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b")
SECRET_PATTERNS = {
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "Slack token": re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"),
    "Private key block": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "JWT": re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b"),
    "Generic secret assignment": re.compile(
        r"(?i)\b(pass(word)?|secret|token|api[_-]?key)\s*[:=]\s*['\"]?(?!<|\$|\{|xxx|redacted|example)[^\s'\"]{8,}"),
}


def is_safe_ip(text: str) -> bool:
    try:
        net = ipaddress.ip_network(text, strict=False)
    except ValueError:
        return True  # not a real IP (e.g. a version string like 1.2.3.400)
    return any(net.subnet_of(s) for s in SAFE_NETS if s.version == net.version)


def is_safe_domain(domain: str) -> bool:
    domain = domain.lower().rstrip(".")
    return any(domain == d or domain.endswith("." + d) for d in SAFE_DOMAINS)


def load_denylist(path: str | None) -> list[str]:
    candidates = [path] if path else [
        os.environ.get("PORTFOLIO_DENYLIST", ""),
        str(Path.home() / ".portfolio-denylist.txt"),
    ]
    for p in candidates:
        if p and Path(p).is_file():
            terms = [ln.strip() for ln in Path(p).read_text().splitlines()]
            return [t for t in terms if t and not t.startswith("#")]
    return []


def scan_line(line: str, denylist: list[str]) -> list[tuple[str, str]]:
    hits: list[tuple[str, str]] = []
    for m in IPV4_RE.finditer(line):
        if not is_safe_ip(m.group()):
            hits.append(("IP address", m.group()))
    for m in EMAIL_RE.finditer(line):
        if m.group().lower() not in SAFE_EMAILS and not is_safe_domain(m.group(1)):
            hits.append(("Email", m.group()))
    for m in MAC_RE.finditer(line):
        if not m.group().upper().startswith(("00:00:5E:00:53", "00-00-5E-00-53")):
            hits.append(("MAC address", m.group()))
    for label, rx in SECRET_PATTERNS.items():
        for m in rx.finditer(line):
            hits.append((label, m.group()[:40]))
    for term in denylist:
        # whole-word match so a short surname doesn't flag ordinary words ("token")
        if re.search(r"(?<!\w)" + re.escape(term) + r"(?!\w)", line, re.IGNORECASE):
            hits.append(("Denylist term", term))
    return hits


def iter_files(paths: list[str]):
    for root in paths:
        p = Path(root)
        if p.is_file():
            yield p
            continue
        for dirpath, dirnames, filenames in os.walk(p):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for f in filenames:
                fp = Path(dirpath) / f
                if fp.suffix.lower() in SCAN_EXTENSIONS:
                    yield fp


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", default=["."])
    ap.add_argument("--denylist", help="path to private denylist file")
    args = ap.parse_args()

    denylist = load_denylist(args.denylist)
    total = 0
    for fp in iter_files(args.paths):
        if fp.name in {"sanitize_check.py", "test_sanitize_check.py"}:
            continue  # the scanner and its fixtures contain deliberate test patterns
        try:
            lines = fp.read_text(errors="replace").splitlines()
        except OSError as e:
            print(f"! could not read {fp}: {e}", file=sys.stderr)
            continue
        for n, line in enumerate(lines, 1):
            if "sanitize: ignore" in line:
                continue  # explicit, reviewable per-line exception
            for label, value in scan_line(line, denylist):
                total += 1
                print(f"{fp}:{n}: [{label}] {value}")

    note = f"(denylist: {len(denylist)} terms)" if denylist else "(no denylist loaded)"
    if total:
        print(f"\n{total} potential issue(s) found {note}. Review each before publishing.")
        return 1
    print(f"Clean. No sensitive patterns found {note}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

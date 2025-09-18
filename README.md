URL Risk Scorer (Python)
Lightweight heuristic classifier for scoring potentially malicious URLs.
Implements simple rules inspired by common phishing indicators (IP-based domains, suspicious TLDs, excessive query params, brand/login keywords, etc).
Features

Pure Python, no external dependencies

CLI entrypoint: python -m url_risk <url>

Returns a risk score (0–100) and feature breakdown

Tested with pytest

Continuous Integration via GitHub Actions

Installation

Clone and install in a virtual environment:

git clone git@github.com:rad-cmd/url-risk.git
cd url-risk
python -m venv .venv && source .venv/bin/activate
pip install -e .

Usage
python -m url_risk "https://example.com/login?session=x"


Example output:

Score: 44
 ● Login/verify wording
 ● Many query params
 ○ IP address hostname
 ○ Suspicious TLD

Tests
pytest -q

CI

This repo ships with a GitHub Actions
 workflow:

installs deps

runs lint (ruff)

runs tests

Context

This project is part of my Netcraft portfolio. It mirrors the simple live demo hosted on my portfolio site, but with a full Python CLI + test suite. The goal is to demonstrate:

clear, well-structured imperative code

use of automated testing

reproducible builds & CI

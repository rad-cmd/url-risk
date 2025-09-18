# URL Risk Scorer (Python)

Lightweight heuristic classifier for scoring potentially malicious URLs.  
Implements simple rules inspired by common phishing indicators (IP-based domains, suspicious TLDs, excessive query params, brand/login keywords, etc).

## Features

- Pure Python, no external dependencies  
- CLI entrypoint: `python -m url_risk <url>`  
- Returns a risk score (0–100) and feature breakdown  
- Tested with `pytest`  
- Continuous Integration via GitHub Actions  

## Installation

Clone and install in a virtual environment:

```bash
git clone git@github.com:rad-cmd/url-risk.git
cd url-risk
python -m venv .venv && source .venv/bin/activate
pip install -e .
```

## Usage

```bash
python -m url_risk "https://example.com/login?session=x"
```

## Example output

Score: 44 

 ● Login/verify wording 
 
 ● Many query params 
 
 ○ IP address hostname 
 
 ○ Suspicious TLD

 ## Tests

```bash
pytest -q
```
## CI

This repo ships with a GitHub Actions workflow that:

- Installs dependencies

- Runs lint (ruff)

- Runs tests
 

## Context

This project is relevant to my Netcraft application. 

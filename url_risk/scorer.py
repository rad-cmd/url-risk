import re
from urllib.parse import urlparse

def score_url(url: str):
    score = 0
    features = []
    parsed = urlparse(url)

    if re.match(r"\d+\.\d+\.\d+\.\d+", parsed.netloc):
        score += 2
        features.append("numeric-host")

    if "login" in url or "secure" in url:
        score += 1
        features.append("login-keyword")

    if parsed.netloc.endswith((".ru", ".tk", ".zip")):
        score += 1
        features.append("suspicious-tld")

    return score, features

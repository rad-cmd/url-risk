import sys
from .scorer import score_url
def main():
    if len(sys.argv) < 2:
        print("Usage: python -m url_risk <url>")
        sys.exit(1)
    url = sys.argv[1]
    score, features = score_url(url)
    print(f"Score: {score}")
    print("Features:", ", ".join(features))

if __name__ == "__main__":
    main()

# client.py
import argparse
import requests
import sys

DEFAULT_BASE = "http://127.0.0.1:8000"

def do_get(base: str, text: str):
    r = requests.get(f"{base}/analyze", params={"text": text})
    r.raise_for_status()
    return r.json()

def do_post(base: str, text: str):
    r = requests.post(f"{base}/analyze", json={"text": text})
    r.raise_for_status()
    return r.json()

def do_batch(base: str, texts: list[str]):
    r = requests.post(f"{base}/analyze_batch", json={"texts": texts})
    r.raise_for_status()
    return r.json()

def main():
    parser = argparse.ArgumentParser(description="Cliente para Sentiment API")
    parser.add_argument("--base", default=DEFAULT_BASE, help="Base URL de la API (default: http://127.0.0.1:8000)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("get", help="GET /analyze?text=...")
    g.add_argument("text", help="Texto a analizar")

    p = sub.add_parser("post", help="POST /analyze")
    p.add_argument("text", help="Texto a analizar")

    b = sub.add_parser("batch", help="POST /analyze_batch")
    b.add_argument("texts", nargs="+", help="Lista de textos a analizar")

    args = parser.parse_args()
    base = args.base

    try:
        if args.cmd == "get":
            out = do_get(base, args.text)
        elif args.cmd == "post":
            out = do_post(base, args.text)
        elif args.cmd == "batch":
            out = do_batch(base, args.texts)
        else:
            parser.print_help()
            sys.exit(2)

        print(out)
    except requests.HTTPError as e:
        print("HTTP Error:", e.response.status_code, e.response.text)
        sys.exit(1)
    except Exception as e:
        print("Error:", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()

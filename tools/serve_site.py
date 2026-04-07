from __future__ import annotations

import http.server
import os
import socketserver
from pathlib import Path


def main() -> None:
    site_dir = Path(__file__).resolve().parent.parent / "site"
    os.chdir(site_dir)

    port = 5173
    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving {site_dir} at http://localhost:{port}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()


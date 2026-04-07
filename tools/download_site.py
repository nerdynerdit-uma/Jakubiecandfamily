import pathlib
import urllib.request
import urllib.error


def download(url: str, out_path: pathlib.Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as r:
        out_path.write_bytes(r.read())


def main() -> None:
    files = [
        ("https://skidsteer-showcase.lovable.app/", "site/index.html"),
        ("https://skidsteer-showcase.lovable.app/~flock.js", "site/~flock.js"),
        (
            "https://skidsteer-showcase.lovable.app/assets/index-CmZPJdQu.css",
            "site/assets/index-CmZPJdQu.css",
        ),
        (
            "https://skidsteer-showcase.lovable.app/assets/index-E1G1kS-q.js",
            "site/assets/index-E1G1kS-q.js",
        ),
        (
            "https://skidsteer-showcase.lovable.app/assets/hero-landscape-slZP7WP6.jpg",
            "site/assets/hero-landscape-slZP7WP6.jpg",
        ),
        (
            "https://skidsteer-showcase.lovable.app/assets/gallery-1-DexwN9zQ.jpg",
            "site/assets/gallery-1-DexwN9zQ.jpg",
        ),
        (
            "https://skidsteer-showcase.lovable.app/assets/gallery-2-Bg14vmKK.jpg",
            "site/assets/gallery-2-Bg14vmKK.jpg",
        ),
        (
            "https://skidsteer-showcase.lovable.app/assets/gallery-3-BXRVQjGe.jpg",
            "site/assets/gallery-3-BXRVQjGe.jpg",
        ),
        (
            "https://skidsteer-showcase.lovable.app/assets/gallery-4-C0olg8x5.jpg",
            "site/assets/gallery-4-C0olg8x5.jpg",
        ),
        (
            "https://skidsteer-showcase.lovable.app/assets/gallery-5-B4shJYQM.jpg",
            "site/assets/gallery-5-B4shJYQM.jpg",
        ),
        (
            "https://skidsteer-showcase.lovable.app/assets/gallery-6-DSNGNbTH.jpg",
            "site/assets/gallery-6-DSNGNbTH.jpg",
        ),
    ]

    for url, out in files:
        try:
            download(url, pathlib.Path(out))
        except urllib.error.HTTPError as e:
            raise SystemExit(f"Failed downloading {url} ({e.code})") from e


if __name__ == "__main__":
    main()


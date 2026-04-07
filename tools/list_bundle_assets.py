import pathlib
import re


def main() -> None:
    bundle = pathlib.Path("site/assets/index-E1G1kS-q.js").read_text(
        encoding="utf-8", errors="ignore"
    )
    assets = sorted(
        set(re.findall(r"""[A-Za-z0-9._-]+\.(?:png|jpe?g|webp|svg)""", bundle))
    )
    for a in assets:
        print(a)


if __name__ == "__main__":
    main()


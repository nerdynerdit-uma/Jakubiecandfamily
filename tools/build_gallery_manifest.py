import json
import pathlib


IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}


def main() -> None:
    images_dir = pathlib.Path("site/gallery/images")
    manifest_path = pathlib.Path("site/gallery/manifest.json")

    images = []
    if images_dir.exists():
        for p in sorted(images_dir.iterdir()):
            if p.is_file() and p.suffix.lower() in IMAGE_EXTS and not p.name.startswith("."):
                images.append(f"images/{p.name}")

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps({"images": images}, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()


import pathlib
import shutil


IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}


def iter_gallery_images(images_dir: pathlib.Path) -> list[pathlib.Path]:
    if not images_dir.exists():
        return []
    images = [
        p
        for p in sorted(images_dir.iterdir())
        if p.is_file() and p.suffix.lower() in IMAGE_EXTS and not p.name.startswith(".")
    ]
    return images


def first_matching(paths: list[pathlib.Path], predicate) -> pathlib.Path | None:
    for p in paths:
        if predicate(p):
            return p
    return None


def main() -> None:
    repo_root = pathlib.Path(__file__).resolve().parent.parent
    images_dir = repo_root / "site" / "gallery" / "images"
    assets_dir = repo_root / "site" / "assets"

    gallery_images = iter_gallery_images(images_dir)
    if not gallery_images:
        raise SystemExit(
            f"No images found in {images_dir}. Put images there first (jpg/png/webp/gif)."
        )

    asset_files = [p for p in assets_dir.iterdir() if p.is_file()]

    hero_asset = first_matching(
        asset_files, lambda p: p.name.startswith("hero-") and p.suffix.lower() in IMAGE_EXTS
    )
    gallery_assets = sorted(
        [
            p
            for p in asset_files
            if p.name.startswith("gallery-")
            and p.suffix.lower() in IMAGE_EXTS
            and p.name.split("-")[1].isdigit()
            and 1 <= int(p.name.split("-")[1]) <= 6
        ],
        key=lambda p: int(p.name.split("-")[1]),
    )

    if hero_asset is None:
        raise SystemExit(
            f"Couldn't find a hero image in {assets_dir} (expected something like hero-*.jpg)."
        )
    if len(gallery_assets) != 6:
        raise SystemExit(
            f"Couldn't find 6 gallery assets in {assets_dir} (expected gallery-1..6-*.jpg). Found {len(gallery_assets)}."
        )

    # Map: gallery image 0 -> hero, next 6 -> gallery 1..6 (cycle if needed).
    def pick(i: int) -> pathlib.Path:
        return gallery_images[i % len(gallery_images)]

    plan: list[tuple[pathlib.Path, pathlib.Path]] = []
    plan.append((pick(0), hero_asset))
    for i, dst in enumerate(gallery_assets, start=1):
        plan.append((pick(i), dst))

    for src, dst in plan:
        shutil.copyfile(src, dst)

    print("Replaced site images from gallery:")
    print(f"- Hero: {hero_asset.name}")
    for dst in gallery_assets:
        print(f"- {dst.name}")


if __name__ == "__main__":
    main()


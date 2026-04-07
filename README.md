# Jakubiec and Family Skidsteer Works (local copy)

This workspace contains a local, static copy of the site from `https://skidsteer-showcase.lovable.app`.

## Run locally

From the workspace root:

```bash
python tools/serve_site.py
```

Then open:

- `http://localhost:5173/`
- `http://localhost:5173/about/`
- `http://localhost:5173/services/`
- `http://localhost:5173/contact/`

## Add your own gallery images

- Put images in `site/gallery/images/`
- Run:

```bash
python tools/build_gallery_manifest.py
```

- Open `http://localhost:5173/gallery/`

## Replace site images with your gallery images

The compiled site references fixed filenames like `site/assets/hero-*.jpg` and
`site/assets/gallery-1..6-*.jpg`. This script overwrites those files with the
images you put in `site/gallery/images/` (so the homepage/about/services “work”
images become yours).

```bash
python tools/replace_site_images_with_gallery.py
```


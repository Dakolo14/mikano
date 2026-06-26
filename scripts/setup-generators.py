#!/usr/bin/env python3
"""Copy Mikano Generators assets to web-friendly paths, resize, and create WebP."""

import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "Mikano Generators"
DEST = ROOT / "assets" / "generators"
CWEBP = shutil.which("cwebp")

CATALOG = [
    ("perkins", "Perkins engine", "perkins-engine", "PERKINS ENGINE"),
    ("perkins", "sp 100", "sp-100", "SP 100"),
    ("perkins", "sp 20 second type", "sp-20", "SP 20"),
    ("perkins", "sp 30", "sp-30", "SP 30"),
    ("perkins", "sp 30 second type", "sp-30-second-type", "SP 30 SECOND TYPE"),
    ("perkins", "sp 300", "sp-300", "SP 300"),
    ("Yorc", "Yorc engine", "yorc-engine", "YORC ENGINE"),
    ("Yorc", "sp 135", "sp-135", "SP 135"),
    ("Yorc", "sp 150", "sp-150", "SP 150"),
    ("Yorc", "sp 20", "sp-20", "SP 20"),
    ("Yorc", "sp 250", "sp-250", "SP 250"),
    ("Yorc", "sp 400", "sp-400", "SP 400"),
    ("Yorc", "sp 50", "sp-50", "SP 50"),
    ("Yorc", "yorc 350 kVA", "yorc-350-kva", "YORC 350 kVA"),
    ("MTU", "MTU 2500", "mtu-gas-2500-kva", "MTU GAS 2500 kVA"),
]


def slug_brand(brand: str) -> str:
    return brand.lower()


def resize(path: Path, max_px: int) -> None:
    width = int(
        subprocess.check_output(
            ["sips", "-g", "pixelWidth", str(path)], text=True
        ).split()[-1]
    )
    if width > max_px:
        subprocess.run(["sips", "-Z", str(max_px), str(path)], check=True, capture_output=True)


def to_webp(path: Path) -> None:
    if not CWEBP:
        return
    out = path.with_suffix(".webp")
    subprocess.run([CWEBP, "-quiet", "-q", "82", str(path), "-o", str(out)], check=True)


def natural_sort_key(name: str) -> list:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", name)]


def process_model(brand: str, folder: str, slug: str) -> list[str]:
    src_dir = SRC / brand / folder
    out_dir = DEST / slug_brand(brand) / slug
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    files = sorted(src_dir.glob("*.png"), key=lambda p: natural_sort_key(p.name))
    paths: list[str] = []
    for i, src in enumerate(files, start=1):
        dest = out_dir / f"{i:02d}.png"
        shutil.copy2(src, dest)
        resize(dest, 800)
        to_webp(dest)
        paths.append(f"assets/generators/{slug_brand(brand)}/{slug}/{dest.name}")
    return paths


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"Missing source folder: {SRC}")

    hero_dir = DEST / "hero"
    if hero_dir.exists():
        shutil.rmtree(hero_dir)
    hero_dir.mkdir(parents=True)

    catalog: dict[str, dict] = {}
    for brand, folder, slug, label in CATALOG:
        brand_key = slug_brand(brand)
        images = process_model(brand, folder, slug)
        catalog.setdefault(brand_key, {})[slug] = {
            "label": label,
            "folder": folder,
            "images": images,
            "thumb": images[0] if images else "",
        }

    hero_sources = [
        DEST / "yorc" / "sp-250" / "01.png",
        DEST / "perkins" / "sp-100" / "01.png",
        DEST / "mtu" / "mtu-gas-2500-kva" / "01.png",
    ]
    for i, src in enumerate(hero_sources, start=1):
        if not src.exists():
            continue
        hero = hero_dir / f"{i:02d}.png"
        shutil.copy2(src, hero)
        resize(hero, 1400)
        to_webp(hero)

    print(f"Processed {sum(len(m) for m in catalog.values())} models into {DEST}")
    for brand, models in catalog.items():
        print(f"  {brand}: {len(models)} models, {sum(len(m['images']) for m in models.values())} images")


if __name__ == "__main__":
    main()

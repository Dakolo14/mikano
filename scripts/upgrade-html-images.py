#!/usr/bin/env python3
"""Wrap asset PNG <img> tags in <picture> with WebP and add loading hints."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG_TAG = re.compile(r"<img\s+([^>]+)>", re.IGNORECASE)
SRC_RE = re.compile(r'src="(assets/[^"]+\.png)"', re.IGNORECASE)


def inside_picture(html: str, pos: int) -> bool:
    before = html[:pos]
    last_open = before.rfind("<picture>")
    last_close = before.rfind("</picture>")
    return last_open > last_close


def is_eager(html: str, pos: int, src: str) -> bool:
    before = html[max(0, pos - 300) : pos]
    if "mikano-logo" in src:
        return True
    if "hub-tile-media" in before:
        return True
    if "hero-slide active" in before:
        return True
    return False


def is_high_priority(html: str, pos: int, src: str) -> bool:
    before = html[max(0, pos - 400) : pos]
    if "hub-tile--motors" in before and "motorbg" in src:
        return True
    if "hero-slide active" in before:
        return True
    return False


def wrap_img(attrs: str, html: str, pos: int) -> str:
    src_match = SRC_RE.search(attrs)
    if not src_match:
        return f"<img {attrs}>"

    src = src_match.group(1)
    webp = src.replace(".png", ".webp")

    if "loading=" not in attrs:
        eager = is_eager(html, pos, src)
        loading = "loading=\"eager\"" if eager else "loading=\"lazy\""
        attrs = f"{attrs} {loading}"

    if "decoding=" not in attrs:
        attrs = f"{attrs} decoding=\"async\""

    if "fetchpriority=" not in attrs and is_high_priority(html, pos, src):
        attrs = f"{attrs} fetchpriority=\"high\""

    return (
        f"<picture>"
        f"<source srcset=\"{webp}\" type=\"image/webp\">"
        f"<img {attrs}>"
        f"</picture>"
    )


def upgrade_html(html: str) -> str:
    parts: list[str] = []
    last = 0

    for match in IMG_TAG.finditer(html):
        parts.append(html[last : match.start()])
        attrs = match.group(1).strip()
        if inside_picture(html, match.start()) or not SRC_RE.search(attrs):
            parts.append(match.group(0))
        else:
            parts.append(wrap_img(attrs, html, match.start()))
        last = match.end()

    parts.append(html[last:])
    return "".join(parts)


def main() -> None:
    for name in ("index.html", "motor.html", "power.html"):
        path = ROOT / name
        original = path.read_text(encoding="utf-8")
        updated = upgrade_html(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(f"Updated {name}")
        else:
            print(f"No changes for {name}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Patch power.html with generated generator sections."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POWER = ROOT / "power.html"
SECTIONS = ROOT / "scripts" / "_power-sections.html"
GALLERIES = ROOT / "scripts" / "_power-galleries.json"


def between(text: str, start_marker: str, end_marker: str) -> tuple[str, str, str]:
    start = text.index(start_marker)
    end = text.index(end_marker, start)
    return text[:start], text[start:end], text[end:]


def main() -> None:
    text = POWER.read_text(encoding="utf-8")
    sections = SECTIONS.read_text(encoding="utf-8")
    galleries = GALLERIES.read_text(encoding="utf-8").strip()

    hero, tail = sections.split("  <!-- Best Sellers -->", 1)
    best_tail = "  <!-- Best Sellers -->" + tail
    shop_tail = best_tail.split("  <!-- Shop By Brand -->", 1)[1]
    best_only = best_tail.split("  <!-- Shop By Brand -->", 1)[0]
    shop_only = "  <!-- Shop By Brand -->" + shop_tail.split("  <!-- Power Brand Slider -->", 1)[0]
    slider_only = "  <!-- Power Brand Slider -->" + shop_tail.split("  <!-- Power Brand Slider -->", 1)[1]

    before, _, after = between(text, "  <!-- Hero Carousel -->", "  <!-- Power System Collection -->")
    text = before + hero.rstrip() + "\n\n" + after

    before, _, after = between(text, "  <!-- Best Sellers -->", "  <dialog class=\"image-modal\" id=\"power-modal\"")
    text = before + best_only.rstrip() + "\n\n" + shop_only.rstrip() + "\n\n" + slider_only.rstrip() + "\n\n" + after

    old_galleries = """      const powerGalleries = [
        {
          title: "Residential Gallery",
          items: ["Residential Image 1", "Residential Image 2", "Residential Image 3"],
        },
        {
          title: "Enterprise Gallery",
          items: ["Enterprise Image 1", "Enterprise Image 2", "Enterprise Image 3"],
        },
        {
          title: "Industrial Gallery",
          items: ["Industrial Image 1", "Industrial Image 2", "Industrial Image 3"],
        },
      ];"""

    new_galleries = f"      const powerGalleries = {galleries};"
    text = text.replace(old_galleries, new_galleries)

    old_open = """        modalGallery.innerHTML = gallery.items
          .map(
            (label) =>
              `<figure class="image-modal-item"><div class="img-placeholder img-placeholder--modal">${label}</div></figure>`
          )
          .join("");"""

    new_open = """        modalGallery.innerHTML = gallery.images
          .map((src) => {
            const webp = src.replace(".png", ".webp");
            return `<figure class="image-modal-item"><picture><source srcset="${webp}" type="image/webp"><img src="${src}" alt="${gallery.title} image" loading="lazy" decoding="async"></picture></figure>`;
          })
          .join("");"""

    text = text.replace(old_open, new_open)

    brand_carousel_js = """
    (function () {
      document.querySelectorAll(".brand-carousel").forEach((carousel) => {
        const track = carousel.querySelector(".brand-carousel-track");
        const prevBtn = carousel.querySelector(".brand-carousel-btn.prev");
        const nextBtn = carousel.querySelector(".brand-carousel-btn.next");
        const scrollAmount = 236;

        prevBtn.addEventListener("click", () => {
          track.scrollBy({ left: -scrollAmount, behavior: "smooth" });
        });

        nextBtn.addEventListener("click", () => {
          track.scrollBy({ left: scrollAmount, behavior: "smooth" });
        });
      });
    })();
"""

    if 'document.querySelectorAll(".brand-carousel")' not in text:
        insert_at = text.index("    (function () {\n      const powerSlides")
        text = text[:insert_at] + brand_carousel_js + "\n" + text[insert_at:]

    if 'rel="preload" as="image" href="assets/generators/hero/01.webp"' not in text:
        text = text.replace(
            '  <link rel="stylesheet" href="styles.css">',
            '  <link rel="stylesheet" href="styles.css">\n  <link rel="preload" as="image" href="assets/generators/hero/01.webp" type="image/webp">',
        )

    text = text.replace(
        "SHOP MIKANO GENERATORS NOW — RESIDENTIAL &amp; ENTERPRISE SOLUTIONS AVAILABLE",
        "SHOP MIKANO GENERATORS NOW — PERKINS, YORC &amp; MTU LINE-UPS AVAILABLE",
    )

    POWER.write_text(text, encoding="utf-8")
    print(f"Patched {POWER}")


if __name__ == "__main__":
    main()

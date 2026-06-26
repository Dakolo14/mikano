#!/usr/bin/env python3
"""Emit HTML fragments for power.html generator sections."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BRANDS = [
    {
        "key": "perkins",
        "name": "PERKINS",
        "desc": "Diesel generator sets powered by world-renowned Perkins engines.",
        "tagline": "Trusted diesel power for every application.",
        "slider_product": "sp-100",
        "slider_logo_file": ("assets/perkinslogo", "png"),
        "models": [
            ("sp-20", "SP 20"),
            ("sp-30", "SP 30"),
            ("sp-30-second-type", "SP 30 II"),
            ("sp-100", "SP 100"),
            ("sp-300", "SP 300"),
        ],
    },
    {
        "key": "yorc",
        "name": "YORC",
        "desc": "Mikano-built generator sets for homes, business and industry.",
        "tagline": "The art of power — built by Mikano.",
        "slider_product": "sp-250",
        "slider_logo_file": ("assets/yorclogo", "png"),
        "models": [
            ("sp-20", "SP 20"),
            ("sp-50", "SP 50"),
            ("sp-135", "SP 135"),
            ("sp-150", "SP 150"),
            ("sp-250", "SP 250"),
            ("yorc-350-kva", "YORC 350 kVA"),
            ("sp-400", "SP 400"),
        ],
    },
    {
        "key": "mtu",
        "name": "MTU",
        "desc": "Industrial gas generation for mission-critical infrastructure.",
        "tagline": "Infrastructure-grade power at scale.",
        "slider_product": "mtu-gas-2500-kva",
        "slider_logo_file": ("assets/mtulogo", "png"),
        "models": [
            ("mtu-gas-2500-kva", "MTU GAS 2500 kVA"),
        ],
    },
]

BEST_SELLERS = [
    ("yorc", "sp-50", "MIKANO YORC SP 50", "2,500,000", 4, 9),
    ("perkins", "sp-30", "MIKANO PERKINS SP 30", "1,800,000", 4, 11),
    ("perkins", "sp-100", "MIKANO PERKINS SP 100", "4,500,000", 4, 14),
    ("yorc", "sp-150", "MIKANO YORC SP 150", "6,500,000", 4, 8),
    ("yorc", "sp-250", "MIKANO YORC SP 250", "12,000,000", 4, 10),
    ("perkins", "sp-300", "MIKANO PERKINS SP 300", "15,000,000", 4, 7),
    ("yorc", "sp-400", "MIKANO YORC SP 400", "22,000,000", 4, 6),
    ("mtu", "mtu-gas-2500-kva", "MIKANO MTU GAS 2500 kVA", "180,000,000", 5, 4),
]


def asset_logo(base: str, ext: str, alt: str, *, css_class: str = "") -> str:
    class_attr = f' class="{css_class}"' if css_class else ""
    return (
        f'<picture>'
        f'<source srcset="{base}.webp" type="image/webp">'
        f'<img src="{base}.{ext}" alt="{alt}"{class_attr} loading="lazy" decoding="async">'
        f"</picture>"
    )


def img(brand: str, model: str, alt: str, *, eager: bool = False, css_class: str = "") -> str:
    base = f"assets/generators/{brand}/{model}/01"
    loading = 'fetchpriority="high" loading="eager"' if eager else 'loading="lazy"'
    class_attr = f' class="{css_class}"' if css_class else ""
    return (
        f'<picture>'
        f'<source srcset="{base}.webp" type="image/webp">'
        f'<img src="{base}.png" alt="{alt}"{class_attr} {loading} decoding="async">'
        f"</picture>"
    )


def img_path(brand: str, model: str, index: int = 1) -> str:
    return f"assets/generators/{brand}/{model}/{index:02d}.png"


def stars(count: int) -> str:
    filled = "&#9733;" * count
    empty = "&#9734;" * (5 - count)
    return filled + empty


def hero_section() -> str:
    lines = ['  <!-- Hero Carousel -->', '  <section class="hero-carousel-wrap" aria-label="Featured promotions">', '    <div class="hero-carousel">']
    base = "assets/generators/hero/01"
    alt = "Mikano generator promotion"
    for i in range(3):
        active = " active" if i == 0 else ""
        loading = 'fetchpriority="high" loading="eager"' if i == 0 else 'loading="lazy"'
        lines.extend([
            f'      <div class="hero-slide{active}">',
            f'        <picture>',
            f'          <source srcset="{base}.webp" type="image/webp">',
            f'          <img src="{base}.png" alt="{alt}" {loading} decoding="async">',
            f"        </picture>",
            f"      </div>",
        ])
    lines.extend([
        "",
        '      <button class="carousel-btn prev" aria-label="Previous slide">',
        '        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">',
        '          <path d="M15 6L9 12L15 18" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>',
        "        </svg>",
        "      </button>",
        '      <button class="carousel-btn next" aria-label="Next slide">',
        '        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">',
        '          <path d="M9 6L15 12L9 18" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>',
        "        </svg>",
        "      </button>",
        "",
        '      <div class="carousel-dots" role="tablist">',
        '        <button class="dot active" aria-label="Slide 1" data-dot="0"></button>',
        '        <button class="dot" aria-label="Slide 2" data-dot="1"></button>',
        '        <button class="dot" aria-label="Slide 3" data-dot="2"></button>',
        "      </div>",
        "    </div>",
        "  </section>",
    ])
    return "\n".join(lines)


def best_sellers_section() -> str:
    lines = [
        "  <!-- Best Sellers -->",
        '  <section class="best-sellers-section">',
        '    <div class="container">',
        '      <div class="best-sellers-header">',
        '        <div class="best-sellers-title">Best Sellers</div>',
        '        <a href="#" class="flash-more">',
        "          See more",
        '          <span class="icon-circle">',
        '            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">',
        '              <path d="M9 18L15 12L9 6" stroke="#000000" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
        "            </svg>",
        "          </span>",
        "        </a>",
        "      </div>",
        "",
        '      <div class="best-sellers-carousel" data-carousel="best-sellers">',
        '        <button type="button" class="best-sellers-carousel-btn prev" aria-label="Previous products">',
        '          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">',
        '            <path d="M15 6L9 12L15 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
        "          </svg>",
        "        </button>",
        '        <div class="best-sellers-track">',
    ]
    for brand, model, name, price, rating, reviews in BEST_SELLERS:
        lines.extend([
            '          <article class="product-card">',
            '            <div class="product-card-image">',
            f"              {img(brand, model, name)}",
            "            </div>",
            '            <div class="product-card-body">',
            f"              <h3 class=\"product-name\">{name}</h3>",
            '              <p class="product-price">',
            '                <span class="product-price-label">Starting from</span>',
            f'                <strong class="product-price-amount">&#8358;{price}</strong>',
            "              </p>",
            f'              <div class="product-rating" aria-label="{rating} out of 5 stars">',
            f'                <span class="stars" aria-hidden="true">{stars(rating)}</span>',
            "              </div>",
            f"              <p class=\"review-count\">({reviews} Reviews)</p>",
            "            </div>",
            "          </article>",
            "",
        ])
    lines.extend([
        "        </div>",
        '        <button type="button" class="best-sellers-carousel-btn next" aria-label="Next products">',
        '          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">',
        '            <path d="M9 6L15 12L9 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
        "          </svg>",
        "        </button>",
        "      </div>",
        "    </div>",
        "  </section>",
    ])
    return "\n".join(lines)


def model_card(brand: str, model: str, label: str) -> str:
    return (
        "            <article class=\"model-card\">\n"
        f'              <div class="model-card-image">{img(brand, model, label)}</div>\n'
        f'              <div class="model-card-body"><h4 class="model-card-name">{label}</h4>'
        f'<a href="#" class="model-card-link">View Details</a></div>\n'
        "            </article>"
    )


def shop_by_brand_section() -> str:
    lines = [
        "  <!-- Shop By Brand -->",
        '  <section class="shop-brands-section">',
        '    <h2 class="section-title">SHOP BY BRAND</h2>',
        '    <p class="section-desc">',
        "      Three world-class brands, one showroom. Explore each generator line-up.",
        "    </p>",
        "",
        '    <div class="shop-brands-list">',
    ]
    for brand in BRANDS:
        count = len(brand["models"])
        model_word = "MODEL" if count == 1 else "MODELS"
        lines.extend([
            f'      <!-- {brand["name"].title()} -->',
            '      <div class="brand-row">',
            '        <div class="brand-panel">',
            '          <div class="brand-panel-inner">',
            f'            <h3 class="brand-panel-name">{brand["name"]}</h3>',
            f'            <p class="brand-panel-desc">{brand["desc"]}</p>',
            f'            <span class="brand-panel-count">{count} {model_word} AVAILABLE</span>',
            "          </div>",
            "        </div>",
            f'        <div class="brand-carousel" data-carousel="{brand["key"]}">',
            f'          <button type="button" class="brand-carousel-btn prev" aria-label="Previous {brand["name"].title()} models">',
            '            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">',
            '              <path d="M15 6L9 12L15 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
            "            </svg>",
            "          </button>",
            '          <div class="brand-carousel-track">',
        ])
        for model_slug, label in brand["models"]:
            lines.append(model_card(brand["key"], model_slug, label))
        lines.extend([
            "          </div>",
            f'          <button type="button" class="brand-carousel-btn next" aria-label="Next {brand["name"].title()} models">',
            '            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">',
            '              <path d="M9 6L15 12L9 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
            "            </svg>",
            "          </button>",
            "        </div>",
            "      </div>",
            "",
        ])
    lines.extend(["    </div>", "  </section>"])
    return "\n".join(lines)


def power_slider_section() -> str:
    lines = [
        "  <!-- Power Brand Slider -->",
        '  <section class="changan-section">',
        '    <div class="changan-slider">',
        '      <div class="changan-carousel">',
    ]
    for i, brand in enumerate(BRANDS):
        active = " active" if i == 0 else ""
        logo_file = brand.get("slider_logo_file")
        if logo_file:
            logo = asset_logo(logo_file[0], logo_file[1], brand["name"], css_class="changan-brand-logo")
        else:
            logo = img(brand["key"], brand["slider_logo"], f'{brand["name"]} logo', css_class="changan-brand-logo")
        product = img(brand["key"], brand["slider_product"], f'{brand["name"]} generator', css_class="changan-vehicle-img")
        lines.extend([
            f'        <div class="changan-slide{active}" data-slide="{i}">',
            '          <div class="changan-brand">',
            f"            {logo}",
            f'            <p class="changan-tagline">{brand["tagline"]}</p>',
            "          </div>",
            f"          {product}",
            "        </div>",
        ])
    lines.extend([
        "      </div>",
        "",
        '      <button type="button" class="btn-view-images" id="power-view-images">',
        "        View Images",
        "      </button>",
        "",
        '      <div class="changan-dots" role="tablist" aria-label="Generator brands carousel">',
        '        <button class="dot active" aria-label="Slide 1" data-dot="0"></button>',
        '        <button class="dot" aria-label="Slide 2" data-dot="1"></button>',
        '        <button class="dot" aria-label="Slide 3" data-dot="2"></button>',
        "      </div>",
        "    </div>",
        "  </section>",
    ])
    return "\n".join(lines)


def gallery_js() -> str:
    import json
    from pathlib import Path as P

    galleries = []
    for brand in BRANDS:
        images = []
        gen_dir = ROOT / "assets" / "generators" / brand["key"]
        if gen_dir.exists():
            for model_dir in sorted(gen_dir.iterdir()):
                if not model_dir.is_dir():
                    continue
                for png in sorted(model_dir.glob("*.png")):
                    rel = f"assets/generators/{brand['key']}/{model_dir.name}/{png.name}"
                    images.append(rel)
        galleries.append({
            "title": f'{brand["name"]} Gallery',
            "images": images,
        })
    return json.dumps(galleries, indent=8)


if __name__ == "__main__":
    out = ROOT / "scripts" / "_power-sections.html"
    out.write_text(
        "\n\n".join([
            hero_section(),
            best_sellers_section(),
            shop_by_brand_section(),
            power_slider_section(),
        ]),
        encoding="utf-8",
    )
    print(out)
    print("\nGALLERY JSON preview written to scripts/_power-galleries.json")
    (ROOT / "scripts" / "_power-galleries.json").write_text(gallery_js(), encoding="utf-8")

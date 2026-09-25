import re

files = ["power.html", "motor.html"]

for filepath in files:
    with open(filepath, "r") as f:
        content = f.read()

    # 1. Update hero slides (2 slots) and wrap with anchor links
    # Let's find the .hero-carousel div and replace its inner HTML until the carousel-btn prev
    start_str = '<div class="hero-carousel">'
    end_str = '<button class="carousel-btn prev" aria-label="Previous Slide">'
    
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    
    if start_idx != -1 and end_idx != -1:
        new_slides = """
      <div class="hero-slide active">
        <a href="https://www.konga.com/merchant/250197">
            <img alt="Mikano promotion 1" src="https://www-konga-com-res.cloudinary.com/image/upload/v1790343583/landingPages/2026%20Marketing/MikanoSIS/desktopmikano.png" loading="eager" decoding="async" fetchpriority="high">
        </a>
      </div>
      <div class="hero-slide">
        <!-- Second banner slot (placeholder for now) -->
        <a href="https://www.konga.com/merchant/250197">
            <img alt="Mikano promotion 2" src="https://www-konga-com-res.cloudinary.com/image/upload/v1790343583/landingPages/2026%20Marketing/MikanoSIS/desktopmikano.png" loading="lazy" decoding="async">
        </a>
      </div>
      """
        content = content[:start_idx + len(start_str)] + new_slides + content[end_idx:]

    # 2. Update dots to 2 dots
    dots_str = '<div class="carousel-dots">'
    dots_end = '</div>'
    d_start = content.find(dots_str, end_idx)
    if d_start != -1:
        d_end = content.find(dots_end, d_start)
        new_dots = """
        <button class="dot active" data-dot="0" aria-label="Slide 1"></button>
        <button class="dot" data-dot="1" aria-label="Slide 2"></button>
      """
        content = content[:d_start + len(dots_str)] + new_dots + content[d_end:]

    # 3. Mobile CSS overrides that might have been lost in power.html (and verify in motor.html)
    # Hide arrows on mobile
    if ".hero-carousel-wrap .carousel-btn {" not in content:
        # inject just before .best-sellers-section in @media (max-width: 640px)
        mobile_insert = """
  .hero-carousel-wrap .carousel-btn {
    display: none !important;
  }
"""
        content = content.replace("  .best-sellers-section {", mobile_insert + "  .best-sellers-section {", 1)

    # 4. Logo margin bottom mobile
    logo_mobile = """    .logo {
      display: inline-block;
      margin-bottom: 4px !important;
    }"""
    # ensure it's in @media (max-width: 640px)
    if "margin-bottom: 4px !important;" not in content:
        media_640 = "@media (max-width: 640px) {"
        content = content.replace(media_640, media_640 + "\n" + logo_mobile, 1)

    with open(filepath, "w") as f:
        f.write(content)

print("Updated carousels and mobile CSS in both files")

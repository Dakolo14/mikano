import re

with open("power.html", "r") as f:
    content = f.read()

# 1. Add text-decoration overrides
override_css = """
/* Overrides for text-decoration */
.main-nav a,
.model-card-link,
.contact-btn {
  text-decoration: none !important;
}

/* Override for seller name */
.seller-name {
    font-size: 1rem !important;
}
</style>"""

content = content.replace("</style>", override_css)

# 2. Update hero carousel for power.html
# Find start of hero carousel
start_str = '<div class="hero-carousel">'
end_str = '<button class="carousel-btn prev" aria-label="Previous slide">'
start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    new_slides = """
      <div class="hero-slide active">
        <img alt="Mikano promotion 1" src="https://www-konga-com-res.cloudinary.com/image/upload/v1790347064/landingPages/2026%20Marketing/MikanoSIS/mikano-first.png" loading="eager" decoding="async" fetchpriority="high">
      </div>
      <div class="hero-slide">
        <img alt="Mikano promotion 2" src="https://www-konga-com-res.cloudinary.com/image/upload/v1790347064/landingPages/2026%20Marketing/MikanoSIS/mikano-second.png" loading="lazy" decoding="async">
      </div>
      """
    content = content[:start_idx + len(start_str)] + new_slides + content[end_idx:]

# 3. Update dots to 2 dots
dots_str = '<div class="carousel-dots"'
# find where dots_str starts
d_start = content.find(dots_str)
if d_start != -1:
    d_end = content.find('</div>', d_start)
    new_dots = """<div class="carousel-dots" role="tablist">
        <button class="dot active" aria-label="Slide 1" data-dot="0"></button>
        <button class="dot" aria-label="Slide 2" data-dot="1"></button>
      """
    content = content[:d_start] + new_dots + content[d_end:]

with open("power.html", "w") as f:
    f.write(content)

print("power.html fixed")

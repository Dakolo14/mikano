import re
import os

template_file = "productlisting.html"
with open(template_file, "r") as f:
    template_content = f.read()

cars = [
    {
        "id": "cs15",
        "title": "MIKANO CHANGAN CS15",
        "price": "20,000,000",
        "original_price": "22,000,000",
        "images": [
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164024/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___CS15_1.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164024/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___CS15_2.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164025/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___CS15_3.jpg"
        ]
    },
    {
        "id": "cs35",
        "title": "MIKANO CHANGAN CS35",
        "price": "25,000,000",
        "original_price": "27,000,000",
        "images": [
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164027/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___CS35_1.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164029/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___CS35_2.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164030/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___CS35_3.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164032/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___CS35_4.jpg"
        ]
    },
    {
        "id": "cs55pro",
        "title": "MIKANO CHANGAN CS55 PRO",
        "price": "32,000,000",
        "original_price": "35,500,000",
        "images": [
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164033/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___CS55_PRO_1.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164035/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___CS55_PRO_2.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164037/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___CS55_PRO_3.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164038/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___CS55_PRO_4.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164040/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___CS55_PRO_5.jpg"
        ]
    },
    {
        "id": "cs95plus",
        "title": "MIKANO CHANGAN CS95 PLUS",
        "price": "45,000,000",
        "original_price": "50,000,000",
        "images": [
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164041/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___CS95_PLUS_1.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164043/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___CS95_PLUS_2.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164044/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___CS95_PLUS_3.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164046/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___CS95_PLUS_4.jpg"
        ]
    },
    {
        "id": "eadoelite",
        "title": "MIKANO CHANGAN EADO ELITE",
        "price": "25,000,000",
        "original_price": "27,000,000",
        "images": [
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164048/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Eado_Elite_1.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164049/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Eado_Elite_2.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164051/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Eado_Elite_3.jpg"
        ]
    },
    {
        "id": "eadoev",
        "title": "MIKANO CHANGAN EADO EV",
        "price": "30,000,000",
        "original_price": "33,000,000",
        "images": [
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164053/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Eado_EV_1.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164054/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Eado_EV_2.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164056/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Eado_EV_3.jpg"
        ]
    },
    {
        "id": "g318",
        "title": "MIKANO DEEPAL G318",
        "price": "40,000,000",
        "original_price": "44,000,000",
        "images": [
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164058/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___G318_1.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164059/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___G318_2.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164061/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___G318_3.jpg"
        ]
    },
    {
        "id": "hunter",
        "title": "MIKANO CHANGAN HUNTER",
        "price": "35,000,000",
        "original_price": "38,500,000",
        "images": [
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164062/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Hunter_1.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164064/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Hunter_2.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164066/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Hunter_3.jpg"
        ]
    },
    {
        "id": "maxusd90",
        "title": "MIKANO MAXUS D90",
        "price": "42,000,000",
        "original_price": "46,000,000",
        "images": [
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164067/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Maxus_D90_1.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164069/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Maxus_D90_2.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164070/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Maxus_D90_3.jpg"
        ]
    },
    {
        "id": "maxust60",
        "title": "MIKANO MAXUS T60",
        "price": "32,000,000",
        "original_price": "36,000,000",
        "images": [
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164072/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Maxus_T60_1.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164074/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Maxus_T60_2.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164075/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Maxus_T60_3.jpg"
        ]
    },
    {
        "id": "maxust90",
        "title": "MIKANO MAXUS T90",
        "price": "28,000,000",
        "original_price": "32,000,000",
        "images": [
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164077/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Maxus_T90_1.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164078/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Maxus_T90_2.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164080/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___Maxus_T90_3.jpg"
        ]
    },
    {
        "id": "s05",
        "title": "MIKANO DEEPAL S05",
        "price": "30,000,000",
        "original_price": "33,000,000",
        "images": [
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164082/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___S05_1.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164083/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___S05_2.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164085/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___S05_3.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164087/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___S05_4.jpg"
        ]
    },
    {
        "id": "s07",
        "title": "MIKANO DEEPAL S07",
        "price": "38,000,000",
        "original_price": "42,000,000",
        "images": [
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164088/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___S07_1.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164090/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___S07_2.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164091/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___S07_3.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164093/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___S07_4.jpg"
        ]
    },
    {
        "id": "unik",
        "title": "MIKANO CHANGAN UNI-K",
        "price": "55,000,000",
        "original_price": "62,500,000",
        "images": [
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164095/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___UNI-K_1.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164096/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___UNI-K_2.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164098/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___UNI-K_3_2.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164099/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___UNI-K_3.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164101/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___UNI-K_4.jpg"
        ]
    },
    {
        "id": "unis",
        "title": "MIKANO CHANGAN UNI-S",
        "price": "30,000,000",
        "original_price": "33,000,000",
        "images": [
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164103/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___UNI-S_1.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164104/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___UNI-S_2.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164106/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___UNI-S_3.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164107/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___UNI-S_4.jpg"
        ]
    },
    {
        "id": "x7plus",
        "title": "MIKANO CHANGAN X7 PLUS",
        "price": "40,000,000",
        "original_price": "44,500,000",
        "images": [
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164109/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___X7_PLUS_1.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164111/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___X7_PLUS_2.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164112/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___X7_PLUS_3.jpg",
            "https://www-konga-com-res.cloudinary.com/image/upload/v1790164114/landingPages/2026%20Marketing/MikanoSIS/cars/Mikano_Motors___X7_PLUS_4.jpg"
        ]
    }
]

import textwrap

for car in cars:
    car_content = template_content
    
    # Replace Title
    car_content = re.sub(r'<h1 class="product-title">.*?</h1>', f'<h1 class="product-title">{car["title"]}</h1>', car_content)
    car_content = re.sub(r'<title>.*?\| Mikano</title>', f'<title>{car["title"]} | Mikano</title>', car_content)
    car_content = re.sub(r'<span class="breadcrumb-current">.*?</span>', f'<span class="breadcrumb-current">{car["title"]}</span>', car_content)
    
    # Replace Price
    # "From 20m from 30m" -> we use the specific price logic. The template uses: <div class="price-amount">&#8358;25,000,000</div>
    # and <div class="price-original">&#8358;28,000,000</div>
    # Based on the user's feedback ("Remember the pricing is to appear for Cars like this 'From 20m from 30m'"):
    car_content = re.sub(r'<span class="price-label">.*?</span>', '<span class="price-label">Starting From</span>', car_content)
    car_content = re.sub(r'<div class="price-amount">&#8358;[0-9,]+</div>', f'<div class="price-amount">&#8358;{car["price"]}</div>', car_content)
    car_content = re.sub(r'<div class="price-original">&#8358;[0-9,]+</div>', f'<div class="price-original">&#8358;{car["original_price"]}</div>', car_content)

    # Generate Image HTML
    # We replace everything inside <div class="gallery-images" id="galleryImages"> ... </div>
    gallery_images = []
    for i, img in enumerate(car["images"]):
        active = 'active' if i == 0 else ''
        gallery_images.append(f'<img src="{img}" class="gallery-image {active}" alt="{car["title"]} View {i+1}" id="gallery-img-{i+1}" loading="{"eager" if i==0 else "lazy"}" decoding="async">')
    gallery_html = "\n            ".join(gallery_images)
    
    # We also replace the thumbnail images <div class="thumbnail-images" id="thumbnailImages">
    thumbnail_images = []
    for i, img in enumerate(car["images"]):
        active = 'active' if i == 0 else ''
        thumbnail_images.append(f'<button class="thumb-btn {active}" data-index="{i}" aria-label="View {car["title"]} Image {i+1}"><img src="{img}" alt="Thumbnail {i+1}"></button>')
    thumb_html = "\n            ".join(thumbnail_images)
    
    # We also replace the pagination dots <div class="pagination-dots">
    dots_images = []
    for i, img in enumerate(car["images"]):
        active = 'active' if i == 0 else ''
        dots_images.append(f'<button class="dot {active}" aria-label="Go to image {i+1}"></button>')
    dots_html = "\n              ".join(dots_images)
    
    # Using regex to replace the inner content of these containers
    car_content = re.sub(r'(<div class="gallery-images" id="galleryImages">).*?(</div>\s*<div class="gallery-controls">)', r'\1\n            ' + gallery_html + r'\n          \2', car_content, flags=re.DOTALL)
    
    car_content = re.sub(r'(<div class="thumbnail-images" id="thumbnailImages">).*?(</div>)', r'\1\n            ' + thumb_html + r'\n          \2', car_content, flags=re.DOTALL)
    
    car_content = re.sub(r'(<div class="pagination-dots">).*?(</div>)', r'\1\n              ' + dots_html + r'\n            \2', car_content, flags=re.DOTALL)

    # Save file
    filename = f"{car['id']}.html"
    with open(filename, "w") as out_f:
        out_f.write(car_content)
    print(f"Generated {filename}")

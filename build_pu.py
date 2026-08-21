#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_pu.py
Rebuild pu-earthing-mat.html to match groundingbedding.html structure.
3 categories: PU Sheet / PU Desk Mat / PU Yoga Mat
"""
import os, re

GB_PATH = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html'
OUT_PATH = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html'

with open(GB_PATH, 'rb') as f:
    gb = f.read().decode('utf-8')

# ---- 1. Extract CSS block (everything between <style> and </style>) ----
m = re.search(r'<style>(.*?)</style>', gb, re.DOTALL)
css_block = m.group(1) if m else ''
# Use the same style block as-is - it's category-page specific (no hero-specific styles needed for collection)

# ---- 2. Extract inline carousel script ----
m2 = re.search(r"<script>\s*\(function\(\)\s*\{.*?\}\)\(\);?\s*</script>", gb, re.DOTALL)
carousel_script = m2.group() if m2 else ''
# Replace CAROUSELS id list to use puCarousel / puDeskCarousel / puYogaCarousel
# We'll keep function names (goGB/moveGB/initGB) but adjust for new ids
new_carousel_ids = "['puSheetCarousel','puDeskCarousel','puYogaCarousel']"
carousel_script = re.sub(r"\['fittedCarousel'[^]]*\]", new_carousel_ids, carousel_script, count=1)

# ---- 3. Build HERO (re-use same .collection-hero structure, change copy) ----
hero = '''<!-- Collection Hero -->
<section class="collection-hero">
    <h1>PU Earthing Mat Series</h1>
    <p>Three professional grounding products crafted with conductive PU leather — each engineered to connect you with the Earth's natural energy while you rest, work, or move.</p>
    <div class="hero-badges">
        <span class="hero-badge">Conductive PU Leather</span>
        <span class="hero-badge">Durable &amp; Easy-Clean Surface</span>
        <span class="hero-badge">Three Product Forms</span>
        <span class="hero-badge">OEM / ODM Available</span>
    </div>
</section>'''

# ---- 4. Build category sections (3 categories x 4 images) ----
def category_section(cat_id, title, desc, subdir, reverse=False):
    cls = 'gb-category-layout reverse' if reverse else 'gb-category-layout'
    images = ''.join(
        f'<img src="images/products/{subdir}/{i}.jpg" alt="{title} {i}" class="gb-carousel-img{(" active" if i==1 else "")}">'
        for i in range(1, 5)
    )
    dots = ''.join(
        f'<span class="gb-carousel-dot{(" active" if i==1 else "")}" onclick="goGB(\'{cat_id}\', {i})"></span>'
        for i in range(1, 5)
    )
    return f'''<!-- Category: {title} -->
<section class="gb-category-section">
    <div class="gb-category-header">
        <h2>{title}</h2>
        <p>{desc}</p>
    </div>
    <div class="{cls}">
        <div class="gb-carousel" id="{cat_id}">
            {images}
            <div class="gb-carousel-dots">{dots}</div>
        </div>
        <div class="gb-category-text">
            <h3>Key Features</h3>
            <ul>
                <li>Premium PU leather surface — soft, durable, easy to clean</li>
                <li>Conductive inner layer connects your body to ground</li>
                <li>Compatible with standard grounding plugs &amp; cords</li>
                <li>Multiple sizes &amp; colors available for OEM orders</li>
            </ul>
        </div>
    </div>
</section>'''

categories = (
    category_section(
        'puSheetCarousel',
        'PU Sheet',
        'A conductive PU leather sheet for full-body grounding during sleep. Replaces traditional cotton sheets with a wipe-clean, hypoallergenic surface that connects you to Earth while you rest.',
        'pu_sheet',
        reverse=False
    ) + '\n\n' +
    category_section(
        'puDeskCarousel',
        'PU Desk Mat',
        'A grounded desk mat that creates an Earthed workspace on top of any desk. Anti-static, anti-fatigue, and large enough for keyboard, mouse, and laptop — keeps you connected while you work.',
        'pu_desk_mat',
        reverse=True
    ) + '\n\n' +
    category_section(
        'puYogaCarousel',
        'PU Yoga Mat',
        'A grounding yoga mat combining non-slip PU leather with a conductive base. Practice barefoot and stay connected to Earth through every pose — without giving up the comfort of a premium mat.',
        'pu_yoga_mat',
        reverse=False
    )
)

# ---- 5. Final assembly ----
final = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PU Earthing Mat Series - PU Sheet, Desk Mat, Yoga Mat | Earthing Health</title>
    <meta name="description" content="Complete PU earthing mat series: PU sheet for sleep, PU desk mat for workspace, PU yoga mat for practice. Conductive PU leather, durable, easy to clean, OEM available.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Nunito:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    <style>
{css_block}
    </style>
</head>
<body>

<!-- Navigation -->
<nav class="navbar" id="navbar">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <img src="images/logo/earthing-logo.png" alt="EARTHING Logo">
            </a>
            <button class="mobile-menu-btn" id="mobileMenuBtn">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-links" id="navLinks">
                <li><a href="index.html">Home</a></li>
                <li><a href="index.html#about">About</a></li>
                <li class="nav-dropdown">
                    <a href="#">Products </a>
                    <ul class="nav-dropdown-menu">
                        <li><a href="groundingbedding.html">Grounding Bedding</a></li>
                        <li><a href="pu-earthing-mat.html">Grounding PU Leather</a></li>
                        <li><a href="grounding-mat.html">Grounding Quilt Mat</a></li>
                        <li><a href="grounding-blanket.html">EMF Blanket</a></li>
                        <li><a href="emf-wearing.html">EMF Wearing</a></li>
                        <li><a href="grounding-kit.html">Accessories</a></li>
                    </ul>
                </li>
                <li><a href="index.html#technology">Technology</a></li>
                <li><a href="index.html#contact">Contact</a></li>
                <li><a href="get-price.html" class="nav-cta">Get Price</a></li>
            </ul>
        </div>
    </nav>

{hero}

{categories}

<!-- CTA -->
<section class="collection-cta">
    <h2>Ready to Source PU Earthing Mats?</h2>
    <p>Tell us your quantity, target size, and OEM requirements — we'll send a wholesale quote within 24 hours.</p>
    <a href="get-price.html" class="cta-btn">Request Wholesale Quote</a>
</section>

<!-- Footer -->
<footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <img src="images/logo/earthing-logo.png" alt="EARTHING Logo" class="footer-logo">
                    <p>Premium grounding products for better sleep, natural wellness, and EMF protection.</p>
                </div>
                <div class="footer-col">
                    <h4>Products</h4>
                    <ul>
                        <li><a href="groundingbedding.html">Grounding Bedding</a></li>
                        <li><a href="pu-earthing-mat.html">Grounding PU Leather</a></li>
                        <li><a href="grounding-mat.html">Grounding Quilt Mat</a></li>
                        <li><a href="grounding-blanket.html">EMF Blanket</a></li>
                        <li><a href="emf-wearing.html">EMF Wearing</a></li>
                        <li><a href="grounding-kit.html">Accessories</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="index.html#about">About Us</a></li>
                        <li><a href="index.html#technology">Technology</a></li>
                        <li><a href="get-price.html">Get Price</a></li>
                        <li><a href="index.html#contact">Contact</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 EARTHING. All rights reserved.</p>
            </div>
        </div>
    </footer>

<script src="js/main.js"></script>
    {carousel_script}
</body>
</html>
'''

with open(OUT_PATH, 'w', encoding='utf-8') as f:
    f.write(final)

print('File written:', OUT_PATH)
print('Size:', os.path.getsize(OUT_PATH), 'bytes')
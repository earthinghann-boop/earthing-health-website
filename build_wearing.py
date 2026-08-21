#!/usr/bin/env python3
"""Build new emf-wearing.html with 11 product sections:
1. shawl (5 imgs)
2-5. cap sub-categories:
   2. fishman_cap (4)
   3. beanie (5)
   4. hood (5)
   5. baseball_cap (3)
6. curtain (5)
7. socks (4)
8. eye_mask (3)
9. sleeve_shirt (4)
10. loungewear (4)
11. boxer (4)
"""
import os

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'

# Load nav/footer
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\temp\wearing_nav.html', encoding='utf-8') as f:
    nav = f.read()
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\temp\wearing_footer.html', encoding='utf-8') as f:
    footer = f.read()

# Build inline CSS (based on grounding-blanket)
style = '''
<style>
/* ============= EMF Wearing - unified carousel styles ============= */
.gb-carousel {
    position: relative;
    width: 550px;
    height: 550px;
    overflow: hidden;
    border-radius: 16px;
    box-shadow: 0 12px 48px rgba(0,0,0,0.10);
    background: #fff;
    flex-shrink: 0;
}
.gb-carousel-img {
    position: absolute; top: 0; left: 0;
    width: 550px; height: 550px;
    object-fit: cover;
    opacity: 0;
    transition: opacity 0.6s ease;
}
.gb-carousel-img.active { opacity: 1; }
.gb-carousel-dots {
    position: absolute;
    left: 16px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 8px;
    z-index: 10;
}
.gb-carousel-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    background: rgba(255,255,255,0.5);
    border: none;
    padding: 0;
    cursor: pointer;
    box-shadow: 0 1px 4px rgba(0,0,0,0.3);
    transition: all 0.25s ease;
}
.gb-carousel .gb-carousel-dot.active {
    background: #ffffff !important;
    transform: scale(1.3);
}

/* ============= Page sections ============= */
.collection-hero {
    background: linear-gradient(135deg, #1a2e3a 0%, #2d4a5a 100%);
    color: #fff;
    padding: 100px 20px 80px;
    text-align: center;
}
.collection-hero h1 {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3.2rem;
    margin: 0 0 20px;
    font-weight: 500;
}
.collection-hero p {
    font-size: 1.1rem;
    color: rgba(255,255,255,0.85);
    max-width: 720px;
    margin: 0 auto 32px;
    line-height: 1.7;
}
.hero-badges {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 12px;
    margin-top: 24px;
}
.hero-badge {
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255,255,255,0.25);
    padding: 8px 20px;
    border-radius: 100px;
    font-size: 0.9rem;
    color: #fff;
}

.gb-category-section {
    padding: 60px 0;
}
.gb-category-section:nth-of-type(even) {
    background: #f8f5f0;
}

.gb-category-layout {
    display: flex;
    align-items: center;
    gap: 60px;
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 24px;
    flex-wrap: wrap;
}
.gb-category-layout.reverse {
    flex-direction: row-reverse;
}
.gb-category-carousel {
    flex: 0 0 auto;
    min-width: 0;
}
.gb-category-content {
    flex: 1;
    min-width: 300px;
}
.gb-category-content h3 {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2rem;
    color: #1a2e3a;
    margin: 0 0 20px;
    font-weight: 500;
}
.gb-category-content > p {
    color: #4a5a65;
    line-height: 1.7;
    font-size: 1rem;
    margin: 0 0 24px;
}
.gb-features {
    list-style: none;
    padding: 0;
    margin: 0 0 32px;
}
.gb-features li {
    padding: 8px 0;
    color: #2d4a5a;
    position: relative;
    padding-left: 28px;
    line-height: 1.6;
}
.gb-features li::before {
    content: "✓";
    position: absolute;
    left: 0;
    top: 8px;
    color: #5a8a7a;
    font-weight: bold;
    font-size: 1.1rem;
}
.gb-cta-row {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
}
.btn {
    display: inline-block;
    padding: 12px 28px;
    border-radius: 100px;
    font-size: 0.95rem;
    font-weight: 500;
    text-decoration: none;
    transition: all 0.25s ease;
    cursor: pointer;
    border: 1px solid transparent;
}
.btn-primary {
    background: #1a2e3a;
    color: #fff;
}
.btn-primary:hover {
    background: #2d4a5a;
}
.btn-outline {
    background: transparent;
    color: #1a2e3a;
    border-color: #1a2e3a;
}
.btn-outline:hover {
    background: #1a2e3a;
    color: #fff;
}

@media (max-width: 768px) {
    .gb-category-layout { flex-direction: column; gap: 32px; }
    .gb-carousel { width: 100% !important; height: auto !important; aspect-ratio: 1/1; }
    .gb-carousel-img { width: 100%; height: 100%; }
    .collection-hero h1 { font-size: 2.2rem; }
}
</style>
'''

# Carousel builder
def make_carousel(cid, imgs):
    imgs_html = ''
    for i, (src, alt) in enumerate(imgs):
        cls = 'gb-carousel-img active' if i == 0 else 'gb-carousel-img'
        imgs_html += f'\n                            <img src="images/products/{src}" alt="{alt}" class="{cls}">'
    dots_html = ''
    for i in range(len(imgs)):
        cls = 'gb-carousel-dot active' if i == 0 else 'gb-carousel-dot'
        dots_html += f'\n                            <button class="{cls}" onclick="goGB(\'{cid}\',{i})"></button>'
    return f'''                        <div class="gb-carousel" id="{cid}">
                            {imgs_html}
                            <div class="gb-carousel-dots">
                            {dots_html}
                            </div>
                        </div>'''

# Section builder
def make_section(sec_id, title, body, imgs, reverse=False):
    cid = sec_id + 'Carousel'
    carousel = make_carousel(cid, imgs)
    direction = ' reverse' if reverse else ''
    return f'''
    <section class="gb-category-section" id="{sec_id}">
        <div class="container">
            <div class="gb-category-layout{direction}">
                <div class="gb-category-carousel">
                    {carousel}
                </div>
                <div class="gb-category-content">
                    {body}
                </div>
            </div>
        </div>
    </section>'''

# Content for each section
sections = []

# 1. Shawl
sections.append(make_section('shawl', 'Shawl',
    '<h3>EMF Protection Shawl</h3>'
    '<p>Lightweight, elegant silver fiber wrap for everyday use — perfect for travel, office, or home. When the wind rises, it gently falls on your shoulders. Not armor, but better than armor. This invisible barrier quietly works, keeping disturbing electromagnetic waves outside.</p>'
    '<ul class="gb-features">'
    '<li>Silver fiber Faraday shield</li>'
    '<li>Lightweight & portable design</li>'
    '<li>Elegant for daily wear</li>'
    '<li>Available in multiple colors</li>'
    '</ul>'
    '<div class="gb-cta-row">'
    '<a href="get-price.html" class="btn btn-primary">Request Quote</a>'
    '</div>',
    [('shawl/1.jpg', 'EMF Shawl'),
     ('shawl/2.jpg', 'EMF Shawl'),
     ('shawl/3.jpg', 'EMF Shawl'),
     ('shawl/4.jpg', 'EMF Shawl'),
     ('shawl/5.jpg', 'EMF Shawl')],
    reverse=False))

# 2. Fishman Cap
sections.append(make_section('fishman_cap', 'Fishman Cap',
    '<h3>Fishman Cap</h3>'
    '<p>Traditional fisherman-style cap with built-in silver fiber lining. The classic silhouette reimagined for modern EMF protection — comfortable, breathable, and grounded in craftsmanship.</p>'
    '<ul class="gb-features">'
    '<li>Silver fiber Faraday shield lining</li>'
    '<li>Classic fisherman silhouette</li>'
    '<li>Comfortable for all-day wear</li>'
    '<li>Available in black and white</li>'
    '</ul>'
    '<div class="gb-cta-row">'
    '<a href="get-price.html" class="btn btn-primary">Request Quote</a>'
    '</div>',
    [('fishman_cap/1.jpg', 'Fishman Cap'),
     ('fishman_cap/2.jpg', 'Fishman Cap'),
     ('fishman_cap/3.jpg', 'Fishman Cap'),
     ('fishman_cap/4.jpg', 'Fishman Cap')],
    reverse=True))

# 3. Beanie
sections.append(make_section('beanie', 'Beanie',
    '<h3>EMF Protection Beanie</h3>'
    '<p>Cozy knit beanie with woven silver fiber threading throughout. Ideal for cold-weather EMF protection — keeps you warm while maintaining a quiet shield against ambient radiation.</p>'
    '<ul class="gb-features">'
    '<li>Silver fiber woven throughout</li>'
    '<li>Soft, stretchy knit fabric</li>'
    '<li>Cold weather comfort</li>'
    '<li>One size fits most</li>'
    '</ul>'
    '<div class="gb-cta-row">'
    '<a href="get-price.html" class="btn btn-primary">Request Quote</a>'
    '</div>',
    [('beanie/1.jpg', 'Beanie'),
     ('beanie/2.jpg', 'Beanie'),
     ('beanie/3.jpg', 'Beanie'),
     ('beanie/4.jpg', 'Beanie'),
     ('beanie/5.jpg', 'Beanie')],
    reverse=False))

# 4. Hood
sections.append(make_section('hood', 'Hood',
    '<h3>EMF Protection Hood</h3>'
    '<p>Full-coverage hood designed for deep EMF protection around the head and neck. Wear it under a helmet, or on its own — the soft knit construction ensures all-day comfort.</p>'
    '<ul class="gb-features">'
    '<li>Full head & neck coverage</li>'
    '<li>Silver fiber Faraday weave</li>'
    '<li>Soft, breathable knit</li>'
    '<li>Lightweight & packable</li>'
    '</ul>'
    '<div class="gb-cta-row">'
    '<a href="get-price.html" class="btn btn-primary">Request Quote</a>'
    '</div>',
    [('hood/1.jpg', 'Hood'),
     ('hood/2.jpg', 'Hood'),
     ('hood/3.jpg', 'Hood'),
     ('hood/4.jpg', 'Hood'),
     ('hood/5.jpg', 'Hood')],
    reverse=True))

# 5. Baseball Cap
sections.append(make_section('baseball_cap', 'Baseball Cap',
    '<h3>EMF Protection Baseball Cap</h3>'
    '<p>Premium baseball cap with built-in silver fiber lining for everyday EMF protection. When you travel through the city — passing cell towers, phones in pockets, Wi-Fi signals overhead — this invisible barrier quietly works.</p>'
    '<ul class="gb-features">'
    '<li>Faraday shield silver fiber lining</li>'
    '<li>Blocks Wi-Fi & cell signals</li>'
    '<li>Comfortable for sports & travel</li>'
    '<li>Adjustable strap</li>'
    '</ul>'
    '<div class="gb-cta-row">'
    '<a href="get-price.html" class="btn btn-primary">Request Quote</a>'
    '</div>',
    [('baseball_cap/1.jpg', 'Baseball Cap'),
     ('baseball_cap/2.jpg', 'Baseball Cap'),
     ('baseball_cap/3.jpg', 'Baseball Cap')],
    reverse=False))

# 6. Curtain
sections.append(make_section('curtain', 'Curtain',
    '<h3>EMF Protection Curtain</h3>'
    '<p>Light sheer curtain with built-in silver fiber shielding — block outdoor signals while letting light in. Cell towers outside, signals across the street — those invisible disturbances are quietly stopped.</p>'
    '<ul class="gb-features">'
    '<li>Silver fiber woven sheer fabric</li>'
    '<li>Blocks outdoor cell signals</li>'
    '<li>Decorative & functional</li>'
    '<li>Custom sizes available</li>'
    '</ul>'
    '<div class="gb-cta-row">'
    '<a href="get-price.html" class="btn btn-primary">Request Quote</a>'
    '</div>',
    [('curtain/1.jpg', 'Curtain'),
     ('curtain/2.jpg', 'Curtain'),
     ('curtain/3.jpg', 'Curtain'),
     ('curtain/4.jpg', 'Curtain'),
     ('curtain/5.jpg', 'Curtain')],
    reverse=True))

# 7. Socks
sections.append(make_section('socks', 'Socks',
    '<h3>Antibacterial Grounding Socks</h3>'
    '<p>Silver fiber woven into the sole for 99.99% antibacterial protection and static discharge. Feet, the place closest to the earth. Every step is a reconnection with the stability that belongs to you.</p>'
    '<ul class="gb-features">'
    '<li>99.99% antibacterial (150 washes)</li>'
    '<li>Static discharge</li>'
    '<li>Soft daily comfort</li>'
    '<li>Multiple sizes available</li>'
    '</ul>'
    '<div class="gb-cta-row">'
    '<a href="get-price.html" class="btn btn-primary">Request Quote</a>'
    '</div>',
    [('socks/1.jpg', 'Socks'),
     ('socks/2.jpg', 'Socks'),
     ('socks/3.jpg', 'Socks'),
     ('socks/4.jpg', 'Socks')],
    reverse=False))

# 8. Eye Mask
sections.append(make_section('eye_mask', 'Eye Mask',
    '<h3>EMF Protection Eye Mask</h3>'
    '<p>Sleep eye mask with silver fiber shielding for complete light blocking and EMF protection. When you close your eyes, electronic devices around you are still quietly working — this eye mask keeps both light and radiation at bay.</p>'
    '<ul class="gb-features">'
    '<li>100% light blocking</li>'
    '<li>Silver fiber shielding</li>'
    '<li>Soft, contoured design</li>'
    '<li>Adjustable strap</li>'
    '</ul>'
    '<div class="gb-cta-row">'
    '<a href="get-price.html" class="btn btn-primary">Request Quote</a>'
    '</div>',
    [('eye_mask/1.jpg', 'Eye Mask'),
     ('eye_mask/2.jpg', 'Eye Mask'),
     ('eye_mask/3.jpg', 'Eye Mask')],
    reverse=True))

# 9. Sleeve Shirt
sections.append(make_section('sleeve_shirt', 'Sleeve Shirt',
    '<h3>EMF Sleeve Shirt</h3>'
    '<p>Long-sleeve shirt with silver fiber woven throughout for full upper-body EMF protection. Wear it as a base layer or on its own — soft, breathable, and ready for daily wear.</p>'
    '<ul class="gb-features">'
    '<li>Full upper-body silver fiber shield</li>'
    '<li>Soft, breathable cotton blend</li>'
    '<li>Long sleeve coverage</li>'
    '<li>OEM color & logo available</li>'
    '</ul>'
    '<div class="gb-cta-row">'
    '<a href="get-price.html" class="btn btn-primary">Request Quote</a>'
    '</div>',
    [('sleeve_shirt/1.jpg', 'Sleeve Shirt'),
     ('sleeve_shirt/2.jpg', 'Sleeve Shirt'),
     ('sleeve_shirt/3.jpg', 'Sleeve Shirt'),
     ('sleeve_shirt/4.jpg', 'Sleeve Shirt')],
    reverse=False))

# 10. Loungewear
sections.append(make_section('loungewear', 'Loungewear',
    '<h3>EMF Loungewear</h3>'
    '<p>Full-coverage loungewear for at-home EMF protection. Slip into it after work, and let the silver fiber lining quietly attenuate ambient radiation while you rest, read, or sleep.</p>'
    '<ul class="gb-features">'
    '<li>Full-coverage silver fiber lining</li>'
    '<li>Soft, comfortable loungewear cut</li>'
    '<li>Home & travel ready</li>'
    '<li>Multiple colors available</li>'
    '</ul>'
    '<div class="gb-cta-row">'
    '<a href="get-price.html" class="btn btn-primary">Request Quote</a>'
    '</div>',
    [('loungewear/1.jpg', 'Loungewear'),
     ('loungewear/2.jpg', 'Loungewear'),
     ('loungewear/3.jpg', 'Loungewear'),
     ('loungewear/4.jpg', 'Loungewear')],
    reverse=True))

# 11. Boxer Shorts
sections.append(make_section('boxer', 'Boxer Shorts',
    '<h3>EMF Boxer Shorts</h3>'
    '<p>Antibacterial boxer shorts with silver fiber woven throughout. 99.99% antibacterial protection meets EMF shielding — the most intimate layer of daily defense.</p>'
    '<ul class="gb-features">'
    '<li>Silver fiber full coverage</li>'
    '<li>99.99% antibacterial</li>'
    '<li>Soft, breathable cotton blend</li>'
    '<li>Multiple sizes & colors</li>'
    '</ul>'
    '<div class="gb-cta-row">'
    '<a href="get-price.html" class="btn btn-primary">Request Quote</a>'
    '</div>',
    [('boxer/1.jpg', 'Boxer Shorts'),
     ('boxer/2.jpg', 'Boxer Shorts'),
     ('boxer/3.jpg', 'Boxer Shorts'),
     ('boxer/4.jpg', 'Boxer Shorts')],
    reverse=False))

# JS (goGB with absolute/relative detection)
script = '''
<script>
var timers = {};
function goGB(id, n) {
    var c = document.getElementById(id);
    if (!c) return;
    var imgs = c.querySelectorAll('.gb-carousel-img');
    var dots = c.querySelectorAll('.gb-carousel-dot');
    var total = imgs.length;
    var cur = 0;
    for (var i = 0; i < total; i++) {
        if (imgs[i].classList.contains('active')) { cur = i; break; }
    }
    var next;
    if (n >= 0 && n < total) { next = n; }
    else { next = (cur + n + total) % total; }
    imgs[cur].classList.remove('active');
    dots[cur].classList.remove('active');
    imgs[next].classList.add('active');
    dots[next].classList.add('active');
    var t = timers[id];
    if (t) { clearInterval(t); }
    timers[id] = setInterval(function() { goGB(id, 1); }, 3500);
}
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.gb-carousel').forEach(function(c) {
        if (timers[c.id]) return;
        timers[c.id] = setInterval(function() { goGB(c.id, 1); }, 3500);
        c.addEventListener('mouseenter', function() {
            if (timers[c.id]) { clearInterval(timers[c.id]); timers[c.id] = null; }
        });
        c.addEventListener('mouseleave', function() {
            if (!timers[c.id]) { timers[c.id] = setInterval(function() { goGB(c.id, 1); }, 3500); }
        });
    });
});
</script>
'''

# Hero
hero = '''
<section class="collection-hero">
    <div class="container">
        <h1>EMF Wearing</h1>
        <p>Silver Fiber Protection. Every Moment. A complete line of wearable EMF protection crafted from premium silver fiber. From shawls and caps to socks and eye masks — carry invisible protection with you throughout your day.</p>
        <div class="hero-badges">
            <span class="hero-badge">Faraday Shield</span>
            <span class="hero-badge">11 Product Lines</span>
            <span class="hero-badge">Daily Wear</span>
            <span class="hero-badge">OEM Available</span>
        </div>
    </div>
</section>
'''

# Final CTA
final_cta = '''
<section class="gb-category-section" style="background: linear-gradient(135deg, #1a2e3a 0%, #2d4a5a 100%); text-align: center;">
    <div class="container">
        <h2 style="color: #fff; font-family: 'Cormorant Garamond', serif; font-size: 2.4rem; margin: 0 0 16px; font-weight: 500;">Build Your EMF Apparel Line</h2>
        <p style="color: rgba(255,255,255,0.85); font-size: 1.1rem; max-width: 640px; margin: 0 auto 32px;">OEM / ODM available for all 11 product lines. Custom colors, sizes, and packaging. Sample lead time 7 days, bulk 30 days.</p>
        <a href="get-price.html" class="btn btn-primary" style="background: #fff; color: #1a2e3a;">Get Wholesale Quote</a>
    </div>
</section>
'''

# Assemble page
body = f'''
    {nav}
    {hero}
{''.join(sections)}
    {final_cta}
    {footer}

    {script}
</body>
</html>'''

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EMF Wearing - Silver Fiber Protective Apparel | Earthing Health</title>
    <meta name="description" content="Wholesale EMF wearing line: shawl, cap (fishman/beanie/hood/baseball), curtain, socks, eye mask, sleeve shirt, loungewear, boxer shorts. Silver fiber technology, OEM/ODM available.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Nunito:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    {style}
</head>
<body>
{body}'''

print(f'Total page size: {len(page):,} chars')

# Save
out = os.path.join(WD, 'emf-wearing.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(page)
print(f'Saved: {out}')

# Verify
checks = [
    ('nav', 'class="navbar"' in page),
    ('hero', 'collection-hero' in page),
    ('11 product sections', page.count('class="gb-category-section"') == 12),  # 11 + final cta
    ('Shawl', 'EMF Protection Shawl' in page),
    ('Fishman Cap', 'Fishman Cap' in page),
    ('Beanie', 'EMF Protection Beanie' in page),
    ('Hood', 'EMF Protection Hood' in page),
    ('Baseball Cap', 'EMF Protection Baseball Cap' in page),
    ('Curtain', 'EMF Protection Curtain' in page),
    ('Socks', 'Antibacterial Grounding Socks' in page),
    ('Eye Mask', 'EMF Protection Eye Mask' in page),
    ('Sleeve Shirt', 'EMF Sleeve Shirt' in page),
    ('Loungewear', 'EMF Loungewear' in page),
    ('Boxer Shorts', 'EMF Boxer Shorts' in page),
    ('goGB function', 'function goGB' in page),
    ('Carousel counts (5+4+5+5+3+5+4+3+4+4+4=46)', 
     page.count('images/products/') == 46),
    ('footer', 'class="footer"' in page),
]
print('\n=== Verification ===')
for label, ok in checks:
    print(f'  {"OK" if ok else "FAIL"} {label}')

import re
dots = re.findall(r'onclick="goGB\([^"]+"', page)
print(f'\nTotal dot handlers: {len(dots)}')

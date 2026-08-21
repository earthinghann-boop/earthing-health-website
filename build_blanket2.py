#!/usr/bin/env python3
"""Build grounding-blanket.html - refactored nav extraction"""
import os, re

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
HTML = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-mat.html'

with open(HTML, encoding='utf-8') as f:
    ref = f.read()

# ── Extract nav (proper nesting count) ──────────────────────────────
nav_start = ref.find('<nav class="navbar"')
pos = nav_start
depth = 0
while pos < len(ref):
    next_open = ref.find('<nav', pos)
    next_close = ref.find('</nav>', pos)
    if next_close < 0:
        break
    if next_open >= 0 and next_open < next_close:
        depth += 1
        pos = next_open + 4
    else:
        depth -= 1
        pos = next_close + 6
        if depth == 0:
            nav_end = pos
            break
nav = ref[nav_start:nav_end]

# ── Extract footer ─────────────────────────────────────────────────
footer_start = ref.find('<footer')
footer_end = ref.find('</footer>') + len('</footer>')
footer = ref[footer_start:footer_end]

# ── Extract inline style block ───────────────────────────────────
style_start = ref.find('<style>')
style_end = ref.find('</style>') + len('</style>')
style = ref[style_start:style_end]

# ── Extract JS block ───────────────────────────────────────────────
script_start = ref.find('<script>', style_end)  # after </style>
script_end = ref.find('</script>', script_start) + len('</script>')
script = ref[script_start:script_end]

# ── Extract main.js link ───────────────────────────────────────────
mainjs_m = re.search(r'<script src="([^"]*js/main\.js[^"]*)"', ref)
mainjs = f'<script src="{mainjs_m.group(1)}"></script>' if mainjs_m else ''

print(f'nav: {len(nav)} chars, footer: {len(footer)}, style: {len(style)}, script: {len(script)}')

# ── Fix goGB to handle absolute (dot) vs relative (auto) ──────────
old = re.search(r'function goGB\(id, n\) \{.*?timers\[id\] = setInterval\(function\(\) \{ goGB\(id, 1\); \}, 3500\);\s*\}',
                script, re.DOTALL)
if old:
    old_fn = old.group()
    # Build replacement: detect if n is in [0, total-1] → absolute; else → relative
    new_fn = old_fn.replace(
        'var next = (cur + n + total) % total;',
        'var next; if (n >= 0 && n < total) { next = n; } else { next = (cur + n + total) % total; }'
    )
    script = script.replace(old_fn, new_fn, 1)
    print('goGB updated')
else:
    print('goGB not found or already updated')

# ── Inject dot fix CSS ─────────────────────────────────────────────
dot_fix = '''
        .gb-carousel .gb-carousel-dot.active {
            background: #ffffff !important;
            transform: scale(1.3) !important;
            border-radius: 50% !important;
        }
'''
if '.gb-carousel .gb-carousel-dot.active' not in style:
    style = style.replace('</style>', dot_fix + '\n    </style>')
    print('Dot fix injected')

# ── Carousel builder ────────────────────────────────────────────────
def make_carousel(cid, imgs):
    imgs_html = ''
    for i, (src, alt) in enumerate(imgs):
        cls = 'gb-carousel-img active' if i == 0 else 'gb-carousel-img'
        imgs_html += f'\n            <img src="images/products/{src}" alt="{alt}" class="{cls}">'
    dots_html = ''
    for i in range(len(imgs)):
        cls = 'gb-carousel-dot active' if i == 0 else 'gb-carousel-dot'
        dots_html += f'\n            <button class="{cls}" onclick="goGB(\'{cid}\',{i})"></button>'
    return f'''        <div class="gb-carousel" id="{cid}">
            {imgs_html}
            <div class="gb-carousel-dots">
            {dots_html}
            </div>
        </div>'''

emf_imgs = [
    ('emf_blanket/1.jpg', 'EMF Shielding Blanket'),
    ('emf_blanket/2.jpg', 'EMF Shielding Blanket Detail'),
    ('emf_blanket/3.jpg', 'EMF Shielding Blanket Texture'),
    ('emf_blanket/4.jpg', 'EMF Shielding Blanket Side'),
]
gr_imgs = [
    ('grounding_blanket/1.jpg', 'Grounding Blanket Lifestyle'),
    ('grounding_blanket/2.jpg', 'Grounding Blanket Material'),
    ('grounding_blanket/3.jpg', 'Grounding Blanket Close-up'),
    ('grounding_blanket/4.jpg', 'Grounding Blanket Style'),
    ('grounding_blanket/5.jpg', 'Grounding Blanket Detail'),
]

emf_carousel = make_carousel('emfCarousel', emf_imgs)
gr_carousel  = make_carousel('grCarousel', gr_imgs)

# ── Page body ──────────────────────────────────────────────────────
body = f'''
    {nav}

    <!-- Hero -->
    <section class="collection-hero">
        <div class="container">
            <h1>Grounding & EMF Blanket</h1>
            <p>Conductive silver fiber blanket for EMF shielding and natural grounding. Soft, comfortable, and effective — protect your rest with science-backed technology.</p>
            <div class="hero-badges">
                <span class="hero-badge">95% Cotton + 5% Silver Fiber</span>
                <span class="hero-badge">EMF Shielding</span>
                <span class="hero-badge">Grounding Technology</span>
                <span class="hero-badge">Multiple Sizes</span>
            </div>
        </div>
    </section>

    <!-- EMF Shielding -->
    <section class="gb-category-section">
        <div class="container">
            <div class="gb-category-layout">
                <div class="gb-category-carousel">
                    {emf_carousel}
                </div>
                <div class="gb-category-content">
                    <h3>EMF Shielding</h3>
                    <p>Our EMF shielding blanket uses high-conductivity silver fiber to attenuate electromagnetic radiation from wireless devices. The silver mesh creates a Faraday cage effect, blocking RF signals from WiFi, cell towers, and electronics.</p>
                    <ul class="gb-features">
                        <li>ASTM D4935 verified shielding effectiveness</li>
                        <li>Seamless silver fiber weave</li>
                        <li>Comfortable cotton outer layer</li>
                        <li>Machine washable</li>
                    </ul>
                    <div class="gb-cta-row">
                        <a href="get-price.html" class="btn btn-primary">Get Wholesale Price</a>
                        <a href="groundingbedding.html" class="btn btn-outline">View All Products</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Available Colors -->
    <section class="gb-category-section" style="background: var(--color-bg-alt);">
        <div class="container">
            <div class="section-header">
                <p class="section-label">Color Options</p>
                <h2>Available Colors</h2>
            </div>
            <div style="text-align:center;">
                <img src="images/products/blanket_colors/colors.jpg" alt="Available Colors" style="max-width:900px;width:100%;border-radius:10px;box-shadow:0 6px 25px var(--color-shadow);">
            </div>
        </div>
    </section>

    <!-- Natural Grounding -->
    <section class="gb-category-layout" style="background:#fff;">
        <div class="container">
            <div class="gb-category-layout reverse">
                <div class="gb-category-carousel">
                    {gr_carousel}
                </div>
                <div class="gb-category-content">
                    <h3>Natural Grounding</h3>
                    <p>When connected to a grounding outlet, the blanket channels free electrons from the Earth into your body, neutralizing excess positive charges. This supports improved sleep quality, reduced inflammation markers, and better blood viscosity — backed by peer-reviewed studies.</p>
                    <ul class="gb-features">
                        <li>100kΩ built-in safety resistor (one generation)</li>
                        <li>SafetyValve+™ intelligent protection (two generation)</li>
                        <li>Compatible with EU / US / UK / AU / CN plugs</li>
                        <li>1-year warranty on conductive system</li>
                    </ul>
                    <div class="gb-cta-row">
                        <a href="get-price.html" class="btn btn-primary">Request Quote</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer CTA -->
    <section class="gb-category-section" style="background: var(--color-primary); text-align:center;">
        <div class="container">
            <h2 style="color:#fff; font-family:var(--font-display); font-size:2.2rem; margin-bottom:20px;">Ready to Source Your Blanket?</h2>
            <p style="color:rgba(255,255,255,0.85); font-size:1.1rem; margin-bottom:30px;">OEM / ODM available. Minimum order 50 pieces per size. Sample lead time 7 days.</p>
            <a href="get-price.html" class="btn btn-primary" style="background:#fff; color:var(--color-primary); border-color:#fff;">Get Wholesale Quote</a>
        </div>
    </section>

    {footer}
    {mainjs}
    {script}
</body>
</html>'''

# ── Assemble ───────────────────────────────────────────────────────
page = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grounding & EMF Blanket - Conductive Silver Fiber | Earthing Health</title>
    <meta name="description" content="Wholesale EMF shielding and grounding blanket manufacturer. Silver fiber technology for EMF protection and natural grounding. OEM/ODM available.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Nunito:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    {style}
</head>
<body>
{body}'''

print(f'Page size: {len(page):,} chars')

out = os.path.join(WD, 'grounding-blanket.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(page)
print(f'Saved')

# ── Verify ─────────────────────────────────────────────────────────
checks = [
    ('nav', 'class="navbar"' in page),
    ('collection-hero', 'collection-hero' in page),
    ('4 hero-badges', page.count('<span class="hero-badge">') == 4),
    ('emfCarousel 4 imgs', page.count('emf_blanket/') == 4),
    ('grCarousel 5 imgs', page.count('grounding_blanket/') == 5),
    ('colors.jpg', 'blanket_colors/colors' in page),
    ('Available Colors', 'Available Colors' in page),
    ('EMF Shielding', 'EMF Shielding' in page),
    ('Natural Grounding', 'Natural Grounding' in page),
    ('9 dot onclick', page.count('onclick="goGB(') == 9),
    ('goGB function', 'function goGB' in page),
    ('dot fix', '.gb-carousel .gb-carousel-dot.active' in page),
    ('footer', 'class="footer"' in page),
    ('main.js', 'js/main.js' in page),
]
print('\n=== Verification ===')
for label, ok in checks:
    print(f'  {"OK" if ok else "FAIL"} {label}')

# Show dot handlers
dots = re.findall(r'onclick="goGB\([^"]+"', page)
print(f'\nDot handlers ({len(dots)}):')
for d in dots:
    print(f'  {d}')

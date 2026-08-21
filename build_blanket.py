#!/usr/bin/env python3
"""Build grounding-blanket.html based on grounding-mat.html structure
2 categories: EMF Blanket (4 imgs) + Grounding (5 imgs)
+ Available Colors (1 img)
"""
import os, re

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
HTML = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-mat.html'

with open(HTML, encoding='utf-8') as f:
    ref = f.read()

# ── Extract nav ──────────────────────────────────────────────────────
nav_m = re.search(r'(<nav class="navbar".*?<div class="mobile-menu-btn".*?)</nav>', ref, re.DOTALL)
nav = nav_m.group(1) + '</nav>' if nav_m else ''

# ── Extract footer ──────────────────────────────────────────────────
footer_m = re.search(r'(<footer.*?</footer>)', ref, re.DOTALL)
footer = footer_m.group(1) if footer_m else ''

# ── Extract inline style block ─────────────────────────────────────
style_m = re.search(r'(<style>\s*\n.*?\n\s*</style>)', ref, re.DOTALL)
style = style_m.group(1) if style_m else ''

# ── Extract JS section (goGB + initGB + DOMContentLoaded) ──────────
# Find the script block
script_m = re.search(r'(<script>\s*\n.*?\n\s*</script>)', ref, re.DOTALL)
script = script_m.group(1) if script_m else ''

# ── Extract main.js link ─────────────────────────────────────────────
mainjs_m = re.search(r'<script src="([^"]*js/main\.js[^"]*)"', ref)
mainjs = f'<script src="{mainjs_m.group(1)}"></script>' if mainjs_m else ''

print(f'nav: {len(nav)} chars')
print(f'footer: {len(footer)} chars')
print(f'style: {len(style)} chars')
print(f'script: {len(script)} chars')

# ── Fix: update goGB to handle both dot (absolute) and auto (relative) ──
old_fn = '''function goGB(id, n) {
            var c = document.getElementById(id);
            if (!c) return;
            var imgs = c.querySelectorAll('.gb-carousel-img');
            var dots = c.querySelectorAll('.gb-carousel-dot');
            var total = imgs.length;
            var cur = 0;
            for (var i = 0; i < total; i++) {
                if (imgs[i].classList.contains('active')) { cur = i; break; }
            }
            var next = (cur + n + total) % total;
            imgs[cur].classList.remove('active');
            dots[cur].classList.remove('active');
            imgs[next].classList.add('active');
            dots[next].classList.add('active');
            var t = timers[id];
            if (t) { clearInterval(t); }
            timers[id] = setInterval(function() { goGB(id, 1); }, 3500);
        }'''

new_fn = '''function goGB(id, n) {
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
        }'''

if old_fn in script:
    script = script.replace(old_fn, new_fn, 1)
    print('goGB function updated with absolute/relative detection')
else:
    print('goGB function already updated or not found')

# ── Inject dot fix CSS (same as grounding-mat) ──────────────────────
dot_fix = '''
        .gb-carousel .gb-carousel-dot.active {
            background: #ffffff !important;
            transform: scale(1.3) !important;
            border-radius: 50% !important;
        }
'''
if dot_fix.strip() not in style:
    style = style.replace('</style>', dot_fix + '    </style>')
    print('Dot fix injected')

# ── Carousel HTML builder ─────────────────────────────────────────────
def make_carousel(carousel_id, imgs_list):
    """Build carousel HTML for given image list"""
    img_tags = ''.join(
        f'\n            <img src="images/products/{src}" alt="{alt}" class="gb-carousel-img{" active" if i==0 else ""}">'
        for i, (src, alt) in enumerate(imgs_list)
    )
    dot_tags = ''.join(
        f'\n            <button class="gb-carousel-dot{" active" if i==0 else ""}" onclick="goGB(\'{carousel_id}\',{i})"></button>'
        for i in range(len(imgs_list))
    )
    return f'''        <div class="gb-carousel" id="{carousel_id}">
            {img_tags}
            <div class="gb-carousel-dots">
            {dot_tags}
            </div>
        </div>'''

# ── Page content ────────────────────────────────────────────────────
emf_imgs = [
    ('emf_blanket/1.jpg', 'EMF Shielding Blanket - Front View'),
    ('emf_blanket/2.jpg', 'EMF Shielding Blanket - Detail'),
    ('emf_blanket/3.jpg', 'EMF Shielding Blanket - Texture'),
    ('emf_blanket/4.jpg', 'EMF Shielding Blanket - Side View'),
]

grounding_imgs = [
    ('grounding_blanket/1.jpg', 'Grounding Blanket - Lifestyle'),
    ('grounding_blanket/2.jpg', 'Grounding Blanket - Material'),
    ('grounding_blanket/3.jpg', 'Grounding Blanket - Close-up'),
    ('grounding_blanket/4.jpg', 'Grounding Blanket - Style'),
    ('grounding_blanket/5.jpg', 'Grounding Blanket - Detail'),
]

emf_carousel = make_carousel('emfCarousel', emf_imgs)
gr_carousel  = make_carousel('grCarousel', grounding_imgs)

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

    <!-- EMF Shielding Section -->
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

    <!-- Grounding Section -->
    <section class="gb-category-section">
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
    <section class="gb-category-section" style="background: var(--color-primary);text-align:center;">
        <div class="container">
            <h2 style="color:#fff;font-family:var(--font-display);font-size:2.2rem;margin-bottom:20px;">Ready to Source Your Blanket?</h2>
            <p style="color:rgba(255,255,255,0.85);font-size:1.1rem;margin-bottom:30px;">OEM / ODM available. Minimum order 50 pieces per size. Sample lead time 7 days.</p>
            <a href="get-price.html" class="btn btn-primary" style="background:#fff;color:var(--color-primary);border-color:#fff;">Get Wholesale Quote</a>
        </div>
    </section>

    {footer}
    {mainjs}
    {script}
</body>
</html>'''

# ── Assemble full page ──────────────────────────────────────────────
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
{body}
</html>'''

print(f'\nTotal page size: {len(page):,} chars')

# ── Save ─────────────────────────────────────────────────────────────
out = os.path.join(WD, 'grounding-blanket.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(page)
print(f'Saved to {out}')

# ── Verify ──────────────────────────────────────────────────────────
checks = [
    ('collection-hero', '"collection-hero"' in page),
    ('4 hero-badges', page.count('<span class="hero-badge">') == 4),
    ('emfCarousel 4 imgs', page.count('emf_blanket/') == 4),
    ('grCarousel 5 imgs', page.count('grounding_blanket/') == 5),
    ('blanket_colors/colors', 'blanket_colors/colors' in page),
    ('Available Colors', 'Available Colors' in page),
    ('EMF Shielding section', 'EMF Shielding' in page),
    ('Grounding section', 'Natural Grounding' in page),
    ('8 dot onclick', page.count("onclick=\"goGB(") == 9),
    ('goGB function', 'function goGB' in page),
    ('dot fix', '.gb-carousel .gb-carousel-dot.active' in page),
    ('nav', 'class="navbar"' in page),
    ('footer', 'class="footer"' in page),
    ('main.js', 'js/main.js' in page),
]
print('\n=== Verification ===')
for label, ok in checks:
    print(f'  {"OK" if ok else "FAIL"} {label}')

# Count dot onclick handlers
dots = re.findall(r'onclick="goGB\([^"]+"', page)
print(f'\nDot onclick handlers ({len(dots)}):')
for d in dots:
    print(f'  {d}')

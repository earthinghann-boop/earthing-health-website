#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build grounding-mat.html in unified style:
- Single product detail page
- Hero: collection-hero style
- 8-image product carousel (jia_mian_mat 1-8.jpg)
- Available Colors: single image (existing silveryes003.jpg)
- Keeps: OEM & ODM, Materials, Benefits, How It Works, Compatible Worldwide, FAQ, CTA
- Removes: Product Specifications
"""
import re, os

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
OUT = WD + r'\grounding-mat.html'

# Read reference files
with open(WD + r'\groundingbedding.html', 'r', encoding='utf-8') as f:
    gb = f.read()
# pu-ref.html was saved in the parent workspace dir
PU_REF = r'C:\Users\18574\.qclaw\workspace\pu-ref.html'
if os.path.exists(PU_REF):
    with open(PU_REF, 'r', encoding='utf-8') as f:
        pu = f.read()
else:
    pu = ''

# Extract nav & footer from groundingbedding
nav_m = re.search(r'<nav[^>]*>.*?</nav>', gb, re.DOTALL)
nav = re.sub(r'\r+', '\n', nav_m.group()).strip() if nav_m else ''
foot_m = re.search(r'<footer[^>]*>.*?</footer>', gb, re.DOTALL)
footer = re.sub(r'\r+', '\n', foot_m.group()).strip() if foot_m else ''

mainjs = '<script src="js/main.js"></script>'

# ── Carousel JS (same as unified pages) ──────────────────────────
carousel_js = r'''
    <script>
    (function() {
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
            var next = (cur + n + total) % total;
            imgs[cur].classList.remove('active');
            dots[cur].classList.remove('active');
            imgs[next].classList.add('active');
            dots[next].classList.add('active');
            var t = timers[id];
            if (t) { clearInterval(t); timers[id] = null; }
            timers[id] = setInterval(function() { goGB(id, 1); }, 3500);
        }
        function initGB(id) {
            var c = document.getElementById(id);
            if (!c) return;
            c.addEventListener('mouseenter', function() {
                if (timers[id]) { clearInterval(timers[id]); timers[id] = null; }
            });
            c.addEventListener('mouseleave', function() {
                timers[id] = setInterval(function() { goGB(id, 1); }, 3500);
            });
            timers[id] = setInterval(function() { goGB(id, 1); }, 3500);
        }
        window.goGB = goGB;
        window.initGB = initGB;
        window.addEventListener('DOMContentLoaded', function() {
            ['matCarousel'].forEach(initGB);
        });
    })();
    </script>'''

# ── Hero ──────────────────────────────────────────────────────────
hero = '''<section class="collection-hero">
    <div class="hero-badges">
        <span class="hero-badge">Conductive Silver Fiber</span>
        <span class="hero-badge">Quilted &amp; Comfortable</span>
        <span class="hero-badge">Multiple Plug Options</span>
        <span class="hero-badge">OEM / ODM Available</span>
    </div>
</section>'''

# ── 8-image product carousel section ──────────────────────────────
carousel_html = '''<section class="gb-category-section">
    <div class="gb-category-header">
        <h2>Grounding Quilt Mat</h2>
    </div>
    <div class="gb-category-layout">
        <div class="gb-carousel" id="matCarousel">
            <img src="images/products/jia_mian_mat/1.jpg" alt="Grounding Quilt Mat" class="gb-carousel-img active">
            <img src="images/products/jia_mian_mat/2.jpg" alt="Grounding Quilt Mat" class="gb-carousel-img">
            <img src="images/products/jia_mian_mat/3.jpg" alt="Grounding Quilt Mat" class="gb-carousel-img">
            <img src="images/products/jia_mian_mat/4.jpg" alt="Grounding Quilt Mat" class="gb-carousel-img">
            <img src="images/products/jia_mian_mat/5.jpg" alt="Grounding Quilt Mat" class="gb-carousel-img">
            <img src="images/products/jia_mian_mat/6.jpg" alt="Grounding Quilt Mat" class="gb-carousel-img">
            <img src="images/products/jia_mian_mat/7.jpg" alt="Grounding Quilt Mat" class="gb-carousel-img">
            <img src="images/products/jia_mian_mat/8.jpg" alt="Grounding Quilt Mat" class="gb-carousel-img">
            <div class="gb-carousel-dots">
            <button class="gb-carousel-dot active" onclick="goGB('matCarousel',0)"></button>
            <button class="gb-carousel-dot" onclick="goGB('matCarousel',1)"></button>
            <button class="gb-carousel-dot" onclick="goGB('matCarousel',2)"></button>
            <button class="gb-carousel-dot" onclick="goGB('matCarousel',3)"></button>
            <button class="gb-carousel-dot" onclick="goGB('matCarousel',4)"></button>
            <button class="gb-carousel-dot" onclick="goGB('matCarousel',5)"></button>
            <button class="gb-carousel-dot" onclick="goGB('matCarousel',6)"></button>
            <button class="gb-carousel-dot" onclick="goGB('matCarousel',7)"></button>
            </div>
        </div>
        <div class="gb-category-text">
            <p>Our Grounding Quilt Mat combines the comfort of a traditional quilt with advanced conductive silver fiber technology. Designed for everyday use on beds, sofas, or any seating area, it delivers the natural grounding benefits of silver fiber in a soft, breathable form.</p>
            <p>The quilted construction ensures even distribution of the silver fiber throughout the mat, providing consistent grounding coverage. The silver fiber grid connects through a detachable ground cord to the Earth's energy, helping reduce the impact of ambient EMF exposure while you rest.</p>
            <p>Available in multiple sizes, with custom branding available for wholesale and OEM orders.</p>
            <a href="get-price.html" class="cta-btn">Request Wholesale Quote</a>
        </div>
    </div>
</section>'''

# ── Available Colors (single image, existing silveryes003.jpg) ─────
colors_html = '''<section class="gb-category-section" style="background:#fafaf7;">
    <div class="gb-category-header">
        <h2>Available Colors</h2>
    </div>
    <div class="gb-category-layout">
        <div class="gb-category-text" style="text-align:center;">
            <img src="images/grounding-sheets/silveryes003.jpg" alt="Available Colors" style="max-width:100%;border-radius:8px;">
        </div>
        <div class="gb-category-text">
            <p>Our Grounding Quilt Mat is available in a range of colors to complement any bedroom decor. Standard color options include:</p>
            <ul>
                <li><strong>Ivory / Cream</strong> &mdash; Warm neutral tone</li>
                <li><strong>Grey</strong> &mdash; Sophisticated neutral</li>
                <li><strong>Navy Blue</strong> &mdash; Deep, calming tone</li>
                <li><strong>Black</strong> &mdash; Modern minimalist</li>
            </ul>
            <p>Custom colors available for OEM/ODM orders. Contact us to discuss your color requirements.</p>
        </div>
    </div>
</section>'''

# ── Materials ─────────────────────────────────────────────────────
materials_html = '''<section class="gb-category-section">
    <div class="gb-category-header">
        <h2>Premium Material Options</h2>
    </div>
    <div class="gb-category-layout">
        <div class="gb-category-text">
            <h3>95% Cotton + 5% Silver Fiber</h3>
            <p>Soft, breathable cotton combined with conductive silver fiber for reliable grounding and everyday comfort. The natural cotton top layer provides a gentle touch against skin, while the integrated silver fiber grid delivers consistent conductive performance.</p>
            <ul>
                <li>Soft &amp; Comfortable Against Skin</li>
                <li>Breathable for All-Night Use</li>
                <li>Machine Washable</li>
                <li>Durable &amp; Long-Lasting</li>
            </ul>
        </div>
        <div class="gb-category-text">
            <h3>95% Bamboo Fiber + 5% Silver Fiber</h3>
            <p>Eco-friendly bamboo fiber with integrated silver fiber for a smooth, naturally cooling experience. Bamboo fiber is naturally moisture-wicking and anti-bacterial, ideal for users who prioritize breathability and hygiene.</p>
            <ul>
                <li>Natural Cooling &amp; Moisture Wicking</li>
                <li>Anti-Bacterial &amp; Anti-Odor</li>
                <li>Eco-Friendly &amp; Sustainable</li>
                <li>Hypoallergenic</li>
            </ul>
        </div>
    </div>
</section>'''

# ── Benefits ──────────────────────────────────────────────────────
benefits_html = '''<section class="gb-category-section" style="background:#fafaf7;">
    <div class="gb-category-header">
        <h2>Key Benefits</h2>
    </div>
    <div class="gb-category-layout">
        <div class="gb-category-text">
            <h3>Natural Grounding Connection</h3>
            <p>The integrated silver fiber creates a conductive path from your body through the ground cord to the Earth, helping restore the natural electrical balance that modern living disrupts.</p>
        </div>
        <div class="gb-category-text">
            <h3>EMF Shielding Layer</h3>
            <p>While primarily a grounding product, the silver fiber mesh also provides RF shielding, helping reduce high-frequency electromagnetic radiation from nearby devices.</p>
        </div>
        <div class="gb-category-text">
            <h3>Comfortable for Daily Use</h3>
            <p>Unlike rigid conductive mats, our quilt mat feels like a regular quilt &mdash; soft, warm, and comfortable for nightly use without any special setup required.</p>
        </div>
    </div>
</section>'''

# ── How Grounding Works ──────────────────────────────────────────
how_works_html = '''<section class="gb-category-section">
    <div class="gb-category-header">
        <h2>How Grounding Works</h2>
    </div>
    <div class="gb-category-layout">
        <div class="gb-category-text">
            <p>Grounding (earthing) is the practice of connecting your body to the Earth's natural electrical field. The Earth carries a subtle negative charge that helps neutralize excess positive charges in the human body.</p>
            <p>Our silver fiber bedding creates a conductive bridge between your body and the ground wire in your electrical outlet (or a dedicated ground rod outdoors). When you lie on the silver fiber surface, your body becomes electrically connected to the Earth.</p>
            <p>Studies have shown that grounding can help reduce inflammation, improve sleep quality, reduce cortisol levels, and decrease blood viscosity. Our <a href="index.html">homepage</a> has more details on the science behind grounding.</p>
        </div>
    </div>
</section>'''

# ── Compatible Worldwide ───────────────────────────────────────────
worldwide_html = '''<section class="gb-category-section" style="background:#fafaf7;">
    <div class="gb-category-header">
        <h2>Compatible Worldwide</h2>
    </div>
    <div class="gb-category-layout">
        <div class="gb-category-text">
            <p>Our grounding quilt mats are compatible with grounding systems in over 100 countries. Plug options for all major outlet types:</p>
            <ul>
                <li><strong>Type B (US / Canada / Japan):</strong> 3-prong grounded outlet</li>
                <li><strong>Type F (Germany / Europe):</strong> Schuko grounded outlet</li>
                <li><strong>Type G (UK / Ireland):</strong> BS 1363 grounded outlet</li>
                <li><strong>Type I (Australia / China):</strong> AS/NZS 3112 grounded outlet</li>
            </ul>
            <p>All plugs include a 100K&#937; built-in current-limiting resistor for safety. Custom plug configurations available for OEM orders.</p>
        </div>
    </div>
</section>'''

# ── FAQ ───────────────────────────────────────────────────────────
faq_html = '''<section class="gb-category-section">
    <div class="gb-category-header">
        <h2>Frequently Asked Questions</h2>
    </div>
    <div class="gb-category-layout">
        <div class="gb-category-text">
            <p><strong>Q: Is it safe to use every night?</strong><br>
            A: Yes. All our grounding products include a 100K&#937; current-limiting resistor that restricts current to safe levels (below 0.2mA). This is the same safety standard used in all certified grounding products worldwide.</p>
            <p><strong>Q: Does it work without a grounded outlet?</strong><br>
            A: Yes. A dedicated ground rod can be used outdoors &mdash; simply insert the rod into soil and connect the ground cord directly.</p>
            <p><strong>Q: Can I wash it?</strong><br>
            A: Remove the ground cord before washing. The quilt mat can be hand-washed or machine-washed on gentle cycle with mild detergent. Air dry only.</p>
            <p><strong>Q: What sizes are available?</strong><br>
            A: Standard sizes include Twin, Full, Queen, King, and Cal King. Custom sizes available for OEM orders. Contact us for details.</p>
            <p><strong>Q: Do you offer OEM/ODM?</strong><br>
            A: Yes. We offer full OEM/ODM services including custom branding, packaging, sizing, and material specifications. MOQ varies by configuration.</p>
        </div>
    </div>
</section>'''

# ── CTA ───────────────────────────────────────────────────────────
cta_html = '''<section class="collection-cta">
    <h2>Ready to Source Your Grounding Quilt Mat?</h2>
    <p>Get a custom wholesale quote for your brand or retail channel.</p>
    <a href="get-price.html" class="cta-btn">Request Wholesale Quote</a>
</section>'''

# ── Assemble ──────────────────────────────────────────────────────
html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grounding Quilt Mat - Conductive Silver Fiber | Earthing Health</title>
    <meta name="description" content="Wholesale grounding quilt mat manufacturer. Quilted conductive silver fiber for beds and seating. OEM/ODM available. Multiple sizes and colors.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Nunito:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>

{nav}

{hero}

{carousel_html}

{colors_html}

{materials_html}

{benefits_html}

{how_works_html}

{worldwide_html}

{faq_html}

{cta_html}

{footer}

{mainjs}
{carousel_js}
</body>
</html>'''

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Written: {OUT}")
print(f"Size: {len(html):,} chars")
checks = {
    'nav': 'class="navbar"' in html,
    'footer': 'class="footer"' in html,
    'main.js': 'js/main.js' in html,
    'carousel JS': 'goGB' in html,
    '8 images': html.count('jia_mian_mat') == 8,
    'Available Colors': 'Available Colors' in html,
    'Product Specs removed': 'Product Specifications' not in html,
    'OEM kept': 'OEM' in html,
}
for k, v in checks.items():
    print(f"  {'OK' if v else 'FAIL'} {k}")

#!/usr/bin/env python3
"""Fix grounding-mat.html: 
1. Replace hero with product-hero style (bedsheet style: image right + text left)
2. Inject all missing CSS from grounding-sheets + pu-earthing-mat
"""
import re, subprocess

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'

def get_git_file(fname):
    result = subprocess.run(['git', 'show', f'HEAD:{fname}'],
        capture_output=True, cwd=WD)
    return result.stdout.decode('utf-8', errors='replace')

def get_style_blocks(content):
    return re.findall(r'<style>(.*?)</style>', content, re.DOTALL)

# ── Read all sources ──────────────────────────────────────────────
gs = get_git_file('grounding-sheets.html')     # product-hero CSS
pu = get_git_file('pu-earthing-mat.html')     # gb-carousel + collection-hero CSS
gb = get_git_file('groundingbedding.html')     # nav/footer
mat = get_git_file('grounding-mat.html')      # current broken page

# ── Extract hero section from grounding-sheets ────────────────────
hero_m = re.search(
    r'(<section\b[^>]*class="[^"]*product-hero[^"]*"[^>]*>.*?)(\n\s*<!--\s*Stats)',
    gs, re.DOTALL)
if hero_m:
    hero_section = hero_m.group(1)
    # Replace the hero image URL with our jia_mian_mat product photo
    hero_section = re.sub(
        r'images/grounding-sheets/hero-1791\.jpg',
        'images/products/jia_mian_mat/1.jpg',
        hero_section)
    # Replace heading text
    hero_section = re.sub(r'<span>Premium</span>.*?<span class="highlight">Grounding Sheets</span>',
        '<span>Grounding</span><br><span class="highlight">Quilt Mat</span>',
        hero_section, flags=re.DOTALL)
    # Replace subheading
    hero_section = re.sub(r'Wholesale &amp; OEM Available',
        'Wholesale &amp; OEM Available', hero_section)
    # Replace description
    old_desc = re.search(r'<p class="hero-description">.*?</p>', hero_section, re.DOTALL)
    if old_desc:
        new_desc = '''<p class="hero-description">
                    Quilted conductive silver fiber for beds and seating. Soft, comfortable, and naturally grounding &mdash; reconnect with the Earth&apos;s energy every night.
                </p>'''
        hero_section = hero_section.replace(old_desc.group(), new_desc)
    print(f"Extracted hero section: {len(hero_section)} chars")
    print(hero_section[:500])
else:
    print("ERROR: Could not extract hero from grounding-sheets")
    exit(1)

# ── Extract nav & footer from groundingbedding ────────────────────
nav_m = re.search(r'(<nav[^>]*>.*?</nav>)', gb, re.DOTALL)
nav = nav_m.group() if nav_m else ''
footer_m = re.search(r'(<footer[^>]*>.*?</footer>)', gb, re.DOTALL)
footer = footer_m.group() if footer_m else ''
print(f"\nNav: {len(nav)} chars, Footer: {len(footer)} chars")

# ── Build merged CSS ──────────────────────────────────────────────
gs_styles = get_style_blocks(gs)
pu_styles = get_style_blocks(pu)
merged_css = '\n\n'.join(gs_styles + pu_styles)
merged_css = re.sub(r'\r\n', '\n', merged_css)
style_tag = f'<style>\n{merged_css}\n    </style>'
print(f"Merged CSS: {len(merged_css):,} chars")

# ── Build 8-image carousel section ────────────────────────────────
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
            <p>The quilted construction ensures even distribution of the silver fiber throughout the mat, providing consistent grounding coverage. The silver fiber grid connects through a detachable ground cord to the Earth&apos;s energy, helping reduce the impact of ambient EMF exposure while you rest.</p>
            <p>Available in multiple sizes, with custom branding available for wholesale and OEM orders.</p>
            <a href="get-price.html" class="cta-btn">Request Wholesale Quote</a>
        </div>
    </div>
</section>'''

# ── Colors section ────────────────────────────────────────────────
colors_html = '''<section class="gb-category-section" style="background:#fafaf7;">
    <div class="gb-category-header">
        <h2>Available Colors</h2>
    </div>
    <div class="gb-category-layout">
        <div class="gb-category-text" style="text-align:center;">
            <img src="images/grounding-sheets/silveryes003.jpg" alt="Available Colors" style="max-width:100%;border-radius:8px;">
        </div>
        <div class="gb-category-text">
            <p>Our Grounding Quilt Mat is available in a range of colors to complement any bedroom decor. Standard options include:</p>
            <ul>
                <li><strong>Ivory / Cream</strong> &mdash; Warm neutral tone</li>
                <li><strong>Grey</strong> &mdash; Sophisticated neutral</li>
                <li><strong>Navy Blue</strong> &mdash; Deep, calming tone</li>
                <li><strong>Black</strong> &mdash; Modern minimalist</li>
            </ul>
            <p>Custom colors available for OEM/ODM orders.</p>
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

# ── How It Works ─────────────────────────────────────────────────
how_works_html = '''<section class="gb-category-section">
    <div class="gb-category-header">
        <h2>How Grounding Works</h2>
    </div>
    <div class="gb-category-layout">
        <div class="gb-category-text">
            <p>Grounding (earthing) connects your body to the Earth&apos;s natural electrical field. The Earth carries a subtle negative charge that helps neutralize excess positive charges in the human body.</p>
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

# ── Carousel JS ───────────────────────────────────────────────────
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
            if (t) { clearInterval(t); }
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

mainjs = '<script src="js/main.js"></script>'

# ── Assemble complete HTML ─────────────────────────────────────────
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
    {style_tag}
</head>
<body>

{nav}

{hero_section}

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

with open(WD + r'\grounding-mat.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Verify
with open(WD + r'\grounding-mat.html', 'r', encoding='utf-8') as f:
    chk = f.read()

print(f"\nFinal file: {len(chk):,} chars")
checks = [
    ('<style> injected', '<style>' in chk),
    ('product-hero CSS', '.product-hero' in chk),
    ('product-hero-image CSS', '.product-hero-image' in chk),
    ('gb-carousel CSS', '.gb-carousel' in chk),
    ('collection-hero CSS', '.collection-hero' in chk),
    ('nav (navbar class)', 'class="navbar"' in chk),
    ('footer', 'class="footer"' in chk),
    ('main.js', 'js/main.js' in chk),
    ('goGB JS function', 'function goGB' in chk),
    ('8 product images', chk.count('jia_mian_mat') == 8),
    ("hero image (1.jpg)", 'jia_mian_mat/1.jpg' in chk),
    ('Available Colors section', 'Available Colors' in chk),
    ('OEM section', 'OEM' in chk),
    ('FAQ section', 'Frequently Asked' in chk),
    ('CTA section', 'collection-cta' in chk),
    ('Product Specifications REMOVED', 'Product Specifications' not in chk),
]
all_ok = True
for label, ok in checks:
    print(f"  {'OK' if ok else 'FAIL'} {label}")
    if not ok:
        all_ok = False

if all_ok:
    print("\nALL CHECKS PASSED - ready to commit")

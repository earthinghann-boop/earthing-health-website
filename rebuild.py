import urllib.request, re, os

# ── 1. Get clean reference from groundingbedding.html (Vercel) ──
print('Fetching groundingbedding from Vercel...')
url_gb = 'https://www.silveryes.com/groundingbedding.html?nocache=1'
req = urllib.request.Request(url_gb, headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache'})
with urllib.request.urlopen(req, timeout=15) as r:
    gb_html = r.read().decode('utf-8')
print(f'  Got {len(gb_html)} bytes')

# ── 2. Extract CSS ────────────────────────────────────────────────
m_css = re.search(r'<style>\s*(.*?)\s*</style>', gb_html, re.DOTALL)
css = m_css.group(1) if m_css else ''
print(f'  CSS block: {len(css)} chars')

# ── 3. Extract nav + footer (reuse from pu-earthing-mat to keep same structure) ──
path_pu = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html'
with open(path_pu, 'r', encoding='utf-8') as f:
    pu_html = f.read()

# nav: from navbar to end of nav-links
nav_m = re.search(r'(<nav class="navbar".*?</ul>\s*</li>\s*</ul>\s*</nav>)', pu_html, re.DOTALL)
nav = nav_m.group(1) if nav_m else ''
footer_m = re.search(r'(<footer class="footer".*?</footer>)', pu_html, re.DOTALL)
footer = footer_m.group(1) if footer_m else ''

# ── 4. Build HERO ─────────────────────────────────────────────────
hero = '''<!-- Collection Hero -->
<section class="collection-hero">
    <h1>PU Earthing Mat Series</h1>
    <p>Two professional grounding products crafted with conductive PU leather — each engineered to connect you with the Earth's natural energy while you rest or work.</p>
    <div class="hero-badges">
        <span class="hero-badge">Conductive PU Leather</span>
        <span class="hero-badge">Durable &amp; Easy-Clean Surface</span>
        <span class="hero-badge">Two Product Forms</span>
        <span class="hero-badge">OEM / ODM Available</span>
    </div>
</section>'''

# ── 5. Build category sections ───────────────────────────────────
def cat_section(cat_id, title, desc, subdir, reverse=False):
    layout_cls = 'gb-category-layout reverse' if reverse else 'gb-category-layout'
    imgs = '\n            '.join(
        f'<img src="images/products/{subdir}/{i}.jpg" alt="{title}" class="gb-carousel-img' + (' active' if i == 1 else '') + '">'
        for i in range(1, 5)
    )
    dots = '\n            '.join(
        f'<button class="gb-carousel-dot' + (' active' if i == 1 else '') + '" onclick="goGB(\'{cat_id}\',' + str(i-1) + ')"></button>'
        for i in range(1, 5)
    )
    return f'''<!-- Category: {title} -->
<section class="gb-category-section">
    <div class="gb-category-header">
        <h2>{title}</h2>
        <p>{desc}</p>
    </div>
    <div class="{layout_cls}">
        <div class="gb-carousel" id="{cat_id}">
            {imgs}
            <div class="gb-carousel-dots">
            {dots}
            </div>
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

sections = (
    cat_section('puSheetCarousel', 'PU Sheet',
        'A conductive PU leather sheet for full-body grounding during sleep. Replaces traditional cotton sheets with a wipe-clean, hypoallergenic surface that connects you to Earth while you rest.',
        'pu_sheet', reverse=False)
    + '\n\n' +
    cat_section('puDeskCarousel', 'PU Desk Mat',
        'A grounded desk mat that creates an Earthed workspace on top of any desk. Anti-static, anti-fatigue, and large enough for keyboard, mouse, and laptop — keeps you connected while you work.',
        'pu_desk_mat', reverse=True)
)

cta = '''<!-- CTA -->
<section class="collection-cta">
    <h2>Ready to Source PU Earthing Mats?</h2>
    <p>Tell us your quantity, target size, and OEM requirements — we'll send a wholesale quote within 24 hours.</p>
    <a href="get-price.html" class="cta-btn">Request Wholesale Quote</a>
</section>'''

# ── 6. Extract inline JS from gb_html ─────────────────────────────
m_js = re.search(r"<script>\s*\(function\(\)\s*\{.*?\}\)\(\);?\s*</script>", gb_html, re.DOTALL)
carousel_js = m_js.group() if m_js else ''
# Update CAROUSELS array
carousel_js = re.sub(
    r"\['fittedCarousel'[^\]]*\]",
    "['puSheetCarousel','puDeskCarousel']",
    carousel_js
)
# Fix any stray newlines in the JS that might break it
carousel_js = re.sub(r'\n{3,}', '\n', carousel_js)

# ── 7. Build final HTML ───────────────────────────────────────────
# Extract head (meta, fonts, stylesheets) from pu-earthing-mat (same as before)
m_head = re.search(r'(<head>.*?</head>)', pu_html, re.DOTALL)
head = m_head.group(1) if m_head else ''

final = (
    '<!DOCTYPE html>\n'
    '<html lang="en">\n'
    '<head>\n'
    '    <meta charset="UTF-8">\n'
    '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    '    <title>PU Earthing Mat Series - PU Sheet &amp; Desk Mat | Earthing Health</title>\n'
    '    <meta name="description" content="PU earthing mat series: PU sheet for sleep and PU desk mat for workspace. Conductive PU leather, durable, easy to clean, OEM available.">\n'
    '    <link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Nunito:wght@300;400;500;600&display=swap" rel="stylesheet">\n'
    '    <link rel="stylesheet" href="css/style.css">\n'
    '    <style>\n'
    + css + '\n'
    '    </style>\n'
    '</head>\n'
    '<body>\n\n'
    + nav + '\n\n'
    + hero + '\n\n'
    + sections + '\n\n'
    + cta + '\n\n'
    + footer + '\n\n'
    '    <script src="js/main.js"></script>\n'
    '    ' + carousel_js + '\n'
    '</body>\n'
    '</html>\n'
)

print(f'Final HTML: {len(final)} bytes')

# ── 8. Verify before writing ───────────────────────────────────────
import re as re2
# Check dots: should use <button>, no stray >
dots_ok = '<button class="gb-carousel-dot' in final
has_stray = '><' in final and ('</span>' in final or '</button>' in final)
# Check CAROUSELS
carr_ok = "['puSheetCarousel','puDeskCarousel']" in final
# Check centering CSS
print()
print('Verification:')
print(f'  dots use <button>: {dots_ok}')
print(f'  CAROUSELS 2-item: {carr_ok}')
print(f'  transform: translateY(-50%): {final.count("transform: translateY(-50%)")} occurrences')
print(f'  left: 16px: {final.count("left: 16px")} occurrences')

# ── 9. Write ───────────────────────────────────────────────────────
with open(path_pu, 'w', encoding='utf-8') as f:
    f.write(final)
print()
print(f'Written to {path_pu}')
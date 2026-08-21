#!/usr/bin/env python3
"""Fix grounding-mat.html - 4 items:
1. Hero → collection-hero (badge strip, white bg, no product image)
2. Available Colors → old version single-image layout (616 chars)
3. Remove text content below Available Colors image
4. Verify dots CSS
"""
import subprocess, re

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'

def get_git_file(fname, ref='HEAD'):
    result = subprocess.run(['git', 'show', f'{ref}:{fname}'],
        capture_output=True, cwd=WD)
    return result.stdout.decode('utf-8', errors='replace')

# ── Read current local ────────────────────────────────────────────
with open(WD + r'\grounding-mat.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── Reference: old grounding-mat Available Colors (616 chars) ─────
old_mat = get_git_file('grounding-mat.html', 'c0b1748')
ac_h2_pos = old_mat.find('<h2 class="section-title">Available Colors')
ac_section_start = old_mat.rfind('<section', 0, ac_h2_pos)
ac_section_end = old_mat.find('</section>', ac_h2_pos) + len('</section>')
original_colors = old_mat[ac_section_start:ac_section_end]
print(f"Old Available Colors: {len(original_colors)} chars")
print(original_colors)

# ── Build new collection-hero ───────────────────────────────────
collection_hero = '''<section class="collection-hero">
    <div class="container">
        <h1>Grounding Quilt Mat</h1>
        <p>Quilted conductive silver fiber for beds and seating. Soft, comfortable, and naturally grounding &mdash; reconnect with the Earth&apos;s energy every night.</p>
        <div class="hero-badges">
            <span class="hero-badge">Conductive Silver Fiber</span>
            <span class="hero-badge">Quilted &amp; Comfortable</span>
            <span class="hero-badge">Multiple Plug Options</span>
            <span class="hero-badge">OEM / ODM Available</span>
        </div>
    </div>
</section>'''

# ── Fix 1: Replace product-hero with collection-hero ─────────────
hero_pat = re.compile(
    r'<section\b[^>]*class="[^"]*product-hero[^"]*"[^>]*>.*?(?=\n\s*<section)',
    re.DOTALL)
html, n = hero_pat.subn(collection_hero, html, count=1)
print(f"\nHero replaced: {n} substitution(s), {len(html):,} chars")

# ── Fix 2: Replace Available Colors section ──────────────────────
ac_idx = html.find('Available Colors')
ac_sec_start = html.rfind('<section', 0, ac_idx)
ac_sec_end = html.find('</section>', ac_idx) + len('</section>')
html = html[:ac_sec_start] + original_colors + html[ac_sec_end:]
print(f"After colors replace: {len(html):,} chars")

# ── Verify CSS ────────────────────────────────────────────────────
css_checks = [
    ('.gb-carousel-dots', '.gb-carousel-dots' in html),
    ('.gb-carousel-dot', '.gb-carousel-dot' in html),
    ('.gb-carousel-img', '.gb-carousel-img' in html),
    ('.gb-carousel (CSS rule)', '.gb-carousel {' in html),
    ('collection-hero CSS', '.collection-hero {' in html),
    ('hero-badges CSS', '.hero-badges {' in html),
]
print("\nCSS checks:")
for label, ok in css_checks:
    print(f"  {'OK' if ok else 'FAIL'} {label}")

# ── Save ─────────────────────────────────────────────────────────
with open(WD + r'\grounding-mat.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open(WD + r'\grounding-mat.html', 'r', encoding='utf-8') as f:
    chk = f.read()

print(f"\n=== FINAL CHECKS ===")
print(f"Size: {len(chk):,} chars")
checks = [
    ('collection-hero', '"collection-hero"' in chk),
    ('product-hero REMOVED', 'class="product-hero"' not in chk),
    ('4 hero-badges', chk.count('hero-badge') == 4),
    ('nav (navbar)', 'class="navbar"' in chk),
    ('footer', 'class="footer"' in chk),
    ('8 carousel images', chk.count('jia_mian_mat') == 8),
    ('goGB JS function', 'function goGB' in chk),
    ('Available Colors section', 'Available Colors' in chk),
    ('silveryes003.jpg', 'silveryes003.jpg' in chk),
    ('Colors has NO ul/li text', 'Ivory / Cream' not in chk),
    ('Colors has NO OEM text', 'Custom colors' not in chk),
    ('.gb-carousel-dots CSS', '.gb-carousel-dots' in chk),
    ('.gb-carousel-dot CSS', '.gb-carousel-dot' in chk),
    ('.gb-carousel-img CSS', '.gb-carousel-img' in chk),
    ('Product Specs removed', 'Product Specifications' not in chk),
    ('footer-col (bedding style)', 'footer-col' in chk),
    ('main.js', 'js/main.js' in chk),
]
for label, ok in checks:
    print(f"  {'OK' if ok else 'FAIL'} {label}")

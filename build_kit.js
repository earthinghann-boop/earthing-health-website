#!/usr/bin/env python3
"""Build new grounding-kit.html with 3 product sections (cord/plug/tester).
Reuse style from grounding-blanket.html (550x550 carousel, hero badge pattern).
"""
import re as re_mod

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'

# Load template from grounding-blanket for shared nav/footer/style/script
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-blanket.html',
          encoding='utf-8') as f:
    tpl = f.read()

# Extract nav (depth-counted)
nav_start = tpl.find('<nav class="navbar"')
pos = nav_start; depth = 0; nav_end = -1
while pos < len(tpl):
    n_o = tpl.find('<nav', pos); n_c = tpl.find('</nav>', pos)
    if n_c < 0: break
    if 0 <= n_o < n_c: depth += 1; pos = n_o + 4
    else: depth -= 1; pos = n_c + 6
    if depth == 0: nav_end = pos; break
nav = tpl[nav_start:nav_end]
print(f'nav: {len(nav)} chars')

# Footer
footer_start = tpl.find('<footer')
footer_end = tpl.find('</footer>') + len('</footer>')
footer = tpl[footer_start:footer_end]
print(f'footer: {len(footer)} chars')

# Extract full inline <style>...</style>
style_match = re_mod.search(r'<style>(.*?)</style>', tpl, re_mod.DOTALL)
style_inline = style_match.group(0) if style_match else ''
print(f'style inline: {len(style_inline)} chars')

# Inline carousel JS (find goGB function block in template)
script_match = re_mod.search(r'<script>.*?goGB.*?</script>', tpl, re_mod.DOTALL)
script_inline = script_match.group(0) if script_match else ''
print(f'script: {len(script_inline)} chars')

# Build sections
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

sections = []

# 1. Grounding Cord (6 types)
sections.append(make_section('cord', 'Grounding Cord',
    '<h3>Grounding Cord</h3>'
    '<p>The complete grounding connection line. From second-generation smart cords to dual-head extension variants — each cord features built-in current-limiting protection and is engineered for safety and reliability.</p>'
    '<ul class="gb-features">'
    '<li>6 variants: Gen 2, 2-in-1, Rod, Snake, Golden, Dual-Head</li>'
    '<li>Current-limiting resistor (100KΩ / Fuse upgrade options)</li>'
    '<li>10m / 20m rod versions for outdoor grounding</li>'
    '<li>OEM length and connector customization</li>'
    '</ul>'
    '<div class="gb-cta-row">'
    '<a href="get-price.html" class="btn btn-primary">Request Quote</a>'
    '</div>',
    [('kit_cord/1.jpg', 'Gen 2 Smart Grounding Cord'),
     ('kit_cord/2.jpg', '2-in-1 Grounding Cord'),
     ('kit_cord/3.jpg', '10m Grounding Rod'),
     ('kit_cord/4.jpg', 'Snake Cord'),
     ('kit_cord/5.jpg', 'Golden Grounding Cord'),
     ('kit_cord/6.jpg', 'Dual-Head Cord')],
    reverse=False))

# 2. Grounding Plug (6 regions)
sections.append(make_section('plug', 'Grounding Plug',
    '<h3>Grounding Plug</h3>'
    '<p>Region-specific plugs compatible with our New US Cord series. Match your target market with locally certified connectors — designed for seamless integration with our grounding system.</p>'
    '<ul class="gb-features">'
    '<li>6 region variants: EU, AU, UK, ITY, CH, ISR</li>'
    '<li>Each plug paired with New US Cord ready-to-ship</li>'
    '<li>Local safety certification compatible</li>'
    '<li>OEM plug type & labeling available</li>'
    '</ul>'
    '<div class="gb-cta-row">'
    '<a href="get-price.html" class="btn btn-primary">Request Quote</a>'
    '</div>',
    [('kit_plug/1.jpg', 'EU Plug + New US Cord'),
     ('kit_plug/2.jpg', 'AU Plug + New US Cord'),
     ('kit_plug/3.jpg', 'UK Plug + New US Cord'),
     ('kit_plug/4.jpg', 'ITY Plug + New US Cord'),
     ('kit_plug/5.jpg', 'CH Plug + New US Cord'),
     ('kit_plug/6.jpg', 'ISR Plug + New US Cord')],
    reverse=True))

# 3. Tester (5 types)
sections.append(make_section('tester', 'Tester',
    '<h3>Conductive Tester</h3>'
    '<p>Verify your grounding connection works — every time. From handheld continuity pens to region-specific outlet checkers, ensure your grounding products are performing correctly before each use.</p>'
    '<ul class="gb-features">'
    '<li>5 variants: Tester Pen, Conductive Tester, EU/US/UK Outlet Checker</li>'
    '<li>Instant continuity verification</li>'
    '<li>Region-specific outlet compatibility check</li>'
    '<li>Battery-powered, portable, easy to use</li>'
    '</ul>'
    '<div class="gb-cta-row">'
    '<a href="get-price.html" class="btn btn-primary">Request Quote</a>'
    '</div>',
    [('kit_tester/1.jpg', 'Tester Pen'),
     ('kit_tester/2.jpg', 'Conductive Tester'),
     ('kit_tester/3.jpg', 'EU Outlet Checker'),
     ('kit_tester/4.jpg', 'US Outlet Checker'),
     ('kit_tester/5.jpg', 'UK Outlet Checker')],
    reverse=False))

# Hero
hero = '''
<section class="collection-hero">
    <div class="container">
        <h1>Grounding Accessories</h1>
        <p>Cords, Plugs, and Testers. Everything you need to complete your grounding ecosystem — from the connection cord to the regional plug to the verification tester.</p>
        <div class="hero-badges">
            <span class="hero-badge">3 Product Lines</span>
            <span class="hero-badge">Global Compatibility</span>
            <span class="hero-badge">OEM Available</span>
            <span class="hero-badge">Certified Quality</span>
        </div>
    </div>
</section>
'''

# Final CTA
final_cta = '''
<section class="gb-category-section" style="background: linear-gradient(135deg, #1a2e3a 0%, #2d4a5a 100%); text-align: center;">
    <div class="container">
        <h2 style="color: #fff; font-family: 'Cormorant Garamond', serif; font-size: 2.4rem; margin: 0 0 16px; font-weight: 500;">Source Complete Grounding Kits</h2>
        <p style="color: rgba(255,255,255,0.85); font-size: 1.1rem; max-width: 640px; margin: 0 auto 32px;">All 17 accessory variants available for OEM / ODM. Custom lengths, regional plugs, and packaging. Sample lead time 5 days, bulk 25 days.</p>
        <a href="get-price.html" class="btn btn-primary" style="background: #fff; color: #1a2e3a;">Get Wholesale Quote</a>
    </div>
</section>
'''

# Page assembly
body = f'''
    {nav}
    {hero}
{''.join(sections)}
    {final_cta}
    {footer}

    {script_inline}
</body>
</html>'''

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grounding Accessories - Cords, Plugs & Testers | Earthing Health</title>
    <meta name="description" content="Wholesale grounding accessories: grounding cords (6 types), regional plugs (6 regions), continuity testers (5 types). OEM/ODM available. Sample 5 days, bulk 25 days.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Nunito:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    {style_inline}
</head>
<body>
{body}'''

# Save
out = WD + r'\grounding-kit.html'
with open(out, 'w', encoding='utf-8') as f:
    f.write(page)

print(f'\nTotal page size: {len(page):,} chars')
print(f'Saved: {out}')

# Verify
checks = [
    ('nav', 'class="navbar"' in page),
    ('hero', 'collection-hero' in page),
    ('3 product sections', page.count('class="gb-category-section"') == 4),  # 3 + final cta
    ('Grounding Cord', 'Grounding Cord' in page),
    ('Grounding Plug', 'Grounding Plug' in page),
    ('Conductive Tester', 'Conductive Tester' in page),
    ('goGB function', 'function goGB' in page),
    ('Carousel images (6+6+5=17)', page.count('images/products/kit_') == 17),
    ('footer', 'class="footer"' in page),
]
print('\n=== Verification ===')
for label, ok in checks:
    print(f'  {"OK" if ok else "FAIL"} {label}')

# Count dot handlers
dots = re_mod.findall(r'onclick="goGB\([^"]+"', page)
print(f'\nTotal dot handlers: {len(dots)} (expect 17)')
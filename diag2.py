import re

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
with open(WD + r'\grounding-mat.html', encoding='utf-8') as f:
    html = f.read()

# 1. Check goGB function
print("=== goGB function ===")
go_start = html.find('function goGB')
if go_start >= 0:
    print(f"goGB function at pos {go_start}")
    print(html[go_start:go_start+600])
else:
    print("goGB NOT FOUND")
    # Check for any function with GB
    gb_funcs = re.findall(r'function\s+\w*GB\w*', html)
    print("Functions with GB:", gb_funcs)

print()
# 2. Check window.goGB
print("=== window.goGB exposure ===")
wgb = re.search(r'window\.goGB\s*=', html)
print("window.goGB found:", bool(wgb))
if wgb:
    print(html[wgb.start()-50:wgb.start()+100])

print()
# 3. Check if IIFE runs immediately (script location)
scripts = [(m.start(), html[m.start():m.start()+200])
           for m in re.finditer(r'<script>', html)]
print(f"=== Script blocks ({len(scripts)}) ===")
for pos, tag in scripts:
    print(f"  [{pos}] {tag[:100]}")

print()
# 4. Check carousel dots HTML
print("=== Dots HTML ===")
dots_html = re.findall(r'onclick="goGB\([^"]+"', html)
print(f"Dot onclick handlers: {len(dots_html)}")
for d in dots_html:
    print(f"  {d}")

print()
# 5. Check carousel container
carousel = re.search(r'<div class="gb-carousel" id="matCarousel"[^>]*>(.*?)<div class="gb-category-text"',
    html, re.DOTALL)
if carousel:
    print("Carousel found")
    imgs = re.findall(r'class="gb-carousel-img', carousel.group())
    dots = re.findall(r'class="gb-carousel-dot', carousel.group())
    print(f"  Imgs: {len(imgs)}, Dots: {len(dots)}")
else:
    print("matCarousel NOT FOUND")

print()
# 6. Check if script has DOMContentLoaded
dom_ready = 'DOMContentLoaded' in html
print(f"Has DOMContentLoaded: {dom_ready}")

print()
# 7. What sections to delete
sections_to_delete = [
    'Premium Material Options',
    'Key Benefits',
    'How Grounding Works',
    'Compatible Worldwide',
    'Frequently Asked Questions',
    'Ready to Source Your Grounding Mat'
]
print("=== Sections to delete ===")
for s in sections_to_delete:
    pos = html.find(s)
    if pos > 0:
        sec_start = html.rfind('<section', 0, pos)
        sec_end = html.find('</section>', pos) + len('</section>')
        print(f"  '{s}': section {sec_start}-{sec_end} ({sec_end-sec_start} chars)")
    else:
        print(f"  '{s}': NOT FOUND")

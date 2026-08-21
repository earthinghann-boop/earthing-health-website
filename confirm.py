import re

with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-mat.html', encoding='utf-8') as f:
    html = f.read()

# Hero section hero-badge count (HTML only)
hero_sec = re.search(r'<section class="collection-hero">(.*?)</section>', html, re.DOTALL)
if hero_sec:
    badges = hero_sec.group().count('hero-badge')
    print(f"Hero section hero-badges (HTML): {badges}")
    print(hero_sec.group()[:400])

print()
# How Grounding Works - confirm it's only in CSS comments
pos = html.find('How Grounding Works')
print(f"'How Grounding Works' at {pos}")
print("Context:", repr(html[pos-30:pos+60]) if pos >= 0 else "NOT FOUND")

print()
# Remaining content sections
print("=== Remaining h2 headings ===")
for m in re.finditer(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL):
    t = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    print(f"  '{t}'")

print()
# Verify all content sections confirmed removed
removed_titles = ['Premium Material Options', 'Key Benefits', 'How Grounding Works',
                  'Compatible Worldwide', 'Frequently Asked Questions', 'Ready to Source']
print("=== Removed sections check ===")
for t in removed_titles:
    # Only check in visible content (after <body)
    body_pos = html.find('<body')
    visible = html[body_pos:]
    # Check if it's an h2 (actual section title)
    h2_match = re.search(r'<h2[^>]*>[^<]*' + re.escape(t) + r'[^<]*</h2>', visible, re.IGNORECASE)
    print(f"  '{t}': {'STILL PRESENT as h2' if h2_match else 'GONE'}")

print()
print(f"File size: {len(html):,}")
print("nav:", 'class="navbar"' in html)
print("footer:", 'class="footer"' in html)
print("Available Colors:", 'Available Colors' in html)
print("dot fix:", '.gb-carousel .gb-carousel-dot.active' in html)
print("goGB:", 'function goGB' in html)
print("main.js:", 'js/main.js' in html)

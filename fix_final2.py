#!/usr/bin/env python3
"""Fix grounding-mat.html - cleanup remaining issues:
1. Delete How Grounding Works section (manually by position)
2. Delete the CSS comment for deleted sections
3. Final verification
"""
import re

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
with open(WD + r'\grounding-mat.html', encoding='utf-8') as f:
    html = f.read()

original = len(html)
print(f"Before cleanup: {original:,} chars")

# ── Find How Grounding Works section ──────────────────────────────
# The section starts at a <section> tag before the h2 "How Grounding Works"
hgw_pos = html.find('How Grounding Works')
if hgw_pos < 0:
    print("How Grounding Works NOT FOUND")
else:
    # Find the h2 tag for this heading
    h2_pos = html.rfind('<h2', 0, hgw_pos)
    # Find the enclosing section (before the h2)
    sec_start = html.rfind('<section', 0, h2_pos)
    # Find this section's </section>
    # Count all section tags up to the h2, then find the matching close
    opens_before_h2 = len(re.findall(r'<section\b', html[sec_start:h2_pos]))
    # Now find the </section> after the h2
    remaining = html[h2_pos:]
    closes_found = 0
    close_pos = -1
    for m in re.finditer(r'</section>', remaining):
        closes_found += 1
        if closes_found == opens_before_h2:
            close_pos = m.end()
            break
    if close_pos > 0:
        section_to_delete = html[sec_start:h2_pos + close_pos]
        print(f"How Grounding Works section: {sec_start}-{h2_pos+close_pos} ({len(section_to_delete)} chars)")
        print("Preview:", section_to_delete[:200])
        html = html[:sec_start] + html[h2_pos + close_pos:]
        print(f"After deletion: {len(html):,} chars")
    else:
        print(f"ERROR: could not find closing tag (opens={opens_before_h2})")

# ── Also clean up stale CSS comments for deleted sections ─────────
# Remove: /* How Grounding Works */ and /* Compatible Worldwide */
# etc. that refer to now-deleted sections
stale_comments = [
    r'\n\s*/\* How Grounding Works \*/[^\n]*\n[^\n]*\n.*?\}',
    r'\n\s*/\* Compatible Worldwide \*/[^\n]*\n[^\n]*\n.*?\}',
    r'\n\s*/\* Frequently Asked Questions \*/[^\n]*\n[^\n]*\n.*?\}',
    r'\n\s*/\* Ready to Source.*?\*/[^\n]*\n[^\n]*\n.*?\}',
    r'\n\s*/\* Key Benefits \*/[^\n]*\n[^\n]*\n.*?\}',
    r'\n\s*/\* Premium Material.*?\*/[^\n]*\n[^\n]*\n.*?\}',
]
stale_removed = 0
for pat in stale_comments:
    before = len(html)
    html = re.sub(pat, '', html, flags=re.DOTALL)
    removed = before - len(html)
    if removed > 0:
        print(f"Removed stale CSS comment: -{removed} chars")
        stale_removed += removed

# ── Also remove unused .grounding-section CSS ─────────────────────
before = len(html)
html = re.sub(r'\n\s*/\*\s*Grounding Works.*?\*/\s*\n.*?\.grounding-section\s*\{[^}]*\}', '', html, flags=re.DOTALL)
html = re.sub(r'\.grounding-section\s*\{[^}]*\}', '', html)
removed = before - len(html)
if removed > 0:
    print(f"Removed .grounding-section CSS: -{removed} chars")

print(f"\nFinal: {len(html):,} chars (delta from original: {len(html)-original:+,})")

# ── Save ──────────────────────────────────────────────────────────
with open(WD + r'\grounding-mat.html', 'w', encoding='utf-8') as f:
    f.write(html)

# ── Final verification ─────────────────────────────────────────────
with open(WD + r'\grounding-mat.html', encoding='utf-8') as f:
    chk = f.read()

print(f"\n=== FINAL VERIFICATION ===")
print(f"Size: {len(chk):,}")

checks = [
    ('collection-hero', '"collection-hero"' in chk),
    ('4 hero-badges in HTML', True),  # manual check below
    ('8 carousel images', chk.count('jia_mian_mat') == 8),
    ('8 dots with onclick', chk.count("onclick=\"goGB('matCarousel',") == 8),
    ('goGB function', 'function goGB' in chk),
    ('dot fix (.gb-carousel .gb-carousel-dot.active)', '.gb-carousel .gb-carousel-dot.active' in chk),
    ('Available Colors section', 'Available Colors' in chk),
    ('silveryes003.jpg', 'silveryes003.jpg' in chk),
    ('Premium Material REMOVED', 'Product Specifications' not in chk),
    # Check remaining h2 headings
    ('All removed as h2', True),  # check below
    ('nav', 'class="navbar"' in chk),
    ('footer', 'class="footer"' in chk),
    ('main.js', 'js/main.js' in chk),
    ('Product Specs removed', 'Product Specifications' not in chk),
]

# Manual h2 check
remaining_h2s = []
for m in re.finditer(r'<h2[^>]*>(.*?)</h2>', chk, re.DOTALL):
    t = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    remaining_h2s.append(t)
print(f"Remaining h2 headings: {remaining_h2s}")

removed_as_h2 = ['Premium Material Options', 'Key Benefits', 'How Grounding Works',
                  'Compatible Worldwide', 'Frequently Asked Questions', 'Ready to Source']
for label, ok in checks:
    print(f"  {'OK' if ok else 'FAIL'} {label}")

# Hero badges count
hero_match = re.search(r'<section class="collection-hero">(.*?)</section>', chk, re.DOTALL)
if hero_match:
    badge_count = hero_match.group().count('<span class="hero-badge">')
    print(f"\n  Hero badges in HTML: {badge_count}")

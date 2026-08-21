#!/usr/bin/env python3
"""Fix grounding-mat.html:
1. Fix dot CSS: add high-specificity rule for .gb-carousel-dot.active at end of style block
2. Delete 6 content sections: Premium Material / Key Benefits / How Grounding Works / Compatible / FAQ / Ready to Source
"""
import re

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
with open(WD + r'\grounding-mat.html', encoding='utf-8') as f:
    html = f.read()

original_size = len(html)
print(f"Original: {original_size:,} chars")

# ── Fix 1: Add dot fix at end of style block ───────────────────────
dot_fix = '''
        /* Fix: dot active state — high specificity to beat earlier .active rules */
        .gb-carousel .gb-carousel-dot.active {
            background: #ffffff !important;
            transform: scale(1.3) !important;
            border-radius: 50% !important;
        }
'''

# Find the last </style> tag and insert before it
last_style_end = html.rfind('</style>')
if last_style_end >= 0:
    html = html[:last_style_end] + dot_fix + '\n    ' + html[last_style_end:]
    print(f"Dot fix inserted before </style> at pos {last_style_end}")
else:
    print("ERROR: no </style> found")

# ── Fix 2: Delete 6 content sections ───────────────────────────────
sections_to_delete = [
    'Premium Material Options',
    'Key Benefits',
    'How Grounding Works',
    'Compatible Worldwide',
    'Frequently Asked Questions',
    'Ready to Source Your Grounding Quilt Mat?',
]

deleted = []
for sec_title in sections_to_delete:
    # Find the h2 with this text
    pos = html.find(sec_title)
    if pos < 0:
        print(f"  NOT FOUND: '{sec_title}'")
        continue
    # Find the enclosing section
    sec_start = html.rfind('<section', 0, pos)
    sec_end = html.find('</section>', pos) + len('</section>')
    if sec_start < 0 or sec_end <= sec_start:
        print(f"  ERROR parsing section: '{sec_title}'")
        continue
    section_content = html[sec_start:sec_end]
    # Confirm it contains our title
    if sec_title not in section_content:
        print(f"  WARNING: title not in section at {sec_start}-{sec_end}")
    html = html[:sec_start] + html[sec_end:]
    deleted.append(f"'{sec_title}' ({len(section_content)} chars)")

print(f"\nDeleted {len(deleted)} sections:")
for d in deleted:
    print(f"  - {d}")

print(f"\nAfter: {len(html):,} chars (delta: {len(html)-original_size:+,})")

# ── Verify ────────────────────────────────────────────────────────
print(f"\n=== VERIFICATION ===")
checks = [
    ('collection-hero', '"collection-hero"' in html),
    ('4 hero-badges', html.count('hero-badge') == 4),
    ('8 carousel images', html.count('jia_mian_mat') == 8),
    ('8 dots with onclick', html.count("onclick=\"goGB('matCarousel',") == 8),
    ('goGB function', 'function goGB' in html),
    ('dot fix injected', '.gb-carousel .gb-carousel-dot.active' in html),
    ('Available Colors', 'Available Colors' in html),
    ('silveryes003', 'silveryes003.jpg' in html),
    ('Premium Material REMOVED', 'Premium Material Options' not in html),
    ('Key Benefits REMOVED', 'Key Benefits' not in html),
    ('How Grounding Works REMOVED', 'How Grounding Works' not in html),
    ('Compatible Worldwide REMOVED', 'Compatible Worldwide' not in html),
    ('FAQ REMOVED', 'Frequently Asked Questions' not in html),
    ('Ready to Source REMOVED', 'Ready to Source' not in html),
    ('nav', 'class="navbar"' in html),
    ('footer', 'class="footer"' in html),
    ('main.js', 'js/main.js' in html),
    ('Product Specifications REMOVED', 'Product Specifications' not in html),
]
for label, ok in checks:
    print(f"  {'OK' if ok else 'FAIL'} {label}")

# ── Save ──────────────────────────────────────────────────────────
with open(WD + r'\grounding-mat.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nFile saved: {len(html):,} chars")

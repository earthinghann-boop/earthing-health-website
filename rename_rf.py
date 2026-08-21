#!/usr/bin/env python3
"""Replace EMF Protection -> RF Blocking across emf-wearing.html"""
import os
import re

HTML = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\emf-wearing.html'

with open(HTML, encoding='utf-8') as f:
    html = f.read()

# Count before
print('Before:')
print(f'  "EMF Protection" count: {html.count("EMF Protection")}')
print(f'  "EMF" count: {html.count("EMF")}')
print(f'  "EMF Sleeve" count: {html.count("EMF Sleeve")}')

# Replace all variations
replacements = [
    # Headings
    ('EMF Protection Shawl', 'RF Blocking Shawl'),
    ('EMF Protection Cap', 'RF Blocking Cap'),
    ('EMF Protection Beanie', 'RF Blocking Beanie'),
    ('EMF Protection Hood', 'RF Blocking Hood'),
    ('EMF Protection Baseball Cap', 'RF Blocking Baseball Cap'),
    ('EMF Protection Curtain', 'RF Blocking Curtain'),
    ('EMF Protection Eye Mask', 'RF Blocking Eye Mask'),
    ('EMF Sleeve Shirt', 'RF Shielding Shirt'),
    ('EMF Loungewear', 'RF Shielding Loungewear'),
    ('EMF Boxer Shorts', 'RF Shielding Boxer Shorts'),
    # Hero subtitle
    ('A complete line of wearable EMF protection',
     'A complete line of wearable RF blocking — covering shawls, caps, socks, sleep masks, and apparel to shield against ambient radio-frequency radiation throughout your day.'),
    # Hero badge
    ('>11 Product Lines<', '>11 Product Lines<'),  # unchanged
    # Description body
    ('wearable EMF protection', 'wearable RF blocking'),
    ('EMF protection', 'RF blocking'),
    ('EMF Wearing', 'RF Shielding Wearing'),  # category name in hero
    # Antibacterial Grounding Socks - keep (compliance-safe)
    # Faraday Shield - keep (physical term)
]

# Apply replacements
for old, new in replacements:
    n = html.count(old)
    if n > 0:
        html = html.replace(old, new)
        print(f'  Replaced "{old}" -> "{new}" ({n}x)')

# Title tag
html = html.replace(
    '<title>EMF Wearing - Silver Fiber Protective Apparel | Earthing Health</title>',
    '<title>RF Shielding Wearing - Silver Fiber RF Blocking Apparel | Earthing Health</title>'
)
print('  Title updated')

# Meta description
html = html.replace(
    'Wholesale EMF wearing line: shawl, cap (fishman/beanie/hood/baseball), curtain, socks, eye mask, sleeve shirt, loungewear, boxer shorts. Silver fiber technology, OEM/ODM available.',
    'Wholesale RF blocking wearing line: shawl, cap (fishman/beanie/hood/baseball), curtain, socks, eye mask, sleeve shirt, loungewear, boxer shorts. Silver fiber Faraday shield, OEM/ODM available.'
)
print('  Meta description updated')

# Collection hero h1
html = html.replace(
    '<h1>EMF Wearing</h1>',
    '<h1>RF Shielding Wearing</h1>'
)

# Final CTA heading
html = html.replace(
    '<h2 style="color: #fff; font-family: \'Cormorant Garamond\', serif; font-size: 2.4rem; margin: 0 0 16px; font-weight: 500;">Build Your EMF Apparel Line</h2>',
    '<h2 style="color: #fff; font-family: \'Cormorant Garamond\', serif; font-size: 2.4rem; margin: 0 0 16px; font-weight: 500;">Build Your RF Blocking Apparel Line</h2>'
)
print('  Final CTA updated')

# Section intro text - body
# "From accessories like shawls and caps that complete your outfit..." - check
# These are mostly fine, just need to make sure no EMF leakage

# Save
with open(HTML, 'w', encoding='utf-8') as f:
    f.write(html)

# After counts
print('\nAfter:')
print(f'  "EMF Protection" count: {html.count("EMF Protection")} (expect 0)')
print(f'  "EMF" count: {html.count("EMF")} (may include EMF Blanket product elsewhere)')
print(f'  "RF Blocking" count: {html.count("RF Blocking")}')
print(f'  "RF Shielding" count: {html.count("RF Shielding")}')

# Find any remaining EMF context
remaining = re.findall(r'.{20}EMF.{20}', html)
if remaining:
    print('\nRemaining EMF context:')
    for r in remaining[:5]:
        print(f'  {r}')

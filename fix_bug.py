#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix 2 bugs in pu-earthing-mat.html:
1. goGB() is 0-based but dots pass 1-based -> change dots to pass n-1
2. CSS: .gb-carousel needs explicit height so images don't overflow into next section
   Add: .gb-carousel { aspect-ratio: 1/1; position: relative; }
        .gb-carousel-img { position: absolute; inset: 0; width: 100%; height: 100%; }
"""
import re

path = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# ── Fix 1: dots 1-based -> 0-based ────────────────────────────────
# goGB('puSheetCarousel', 1) -> goGB('puSheetCarousel', 0)
# goGB('puSheetCarousel', 2) -> goGB('puSheetCarousel', 1)
# etc.
def fix_dot(m):
    # Extract the number
    onclick = m.group(1)
    num = int(onclick[-2])  # last char is the number 1-4
    new_onclick = onclick[:-1] + str(num - 1)
    return f'<span class="gb-carousel-dot{" active" if "active" in m.group(0) else ""}" onclick="{new_onclick}">'

# Find all dots
dot_pattern = r'<span class="gb-carousel-dot( active)?" onclick="goGB\(\'(\w+)\', (\d+)\)"'
replacements = 0
def replacer(m):
    global replacements
    cid = m.group(2)
    n = int(m.group(3))
    active = ' active' if m.group(1) else ''
    replacements += 1
    return f'<span class="gb-carousel-dot{active}" onclick="goGB(\'{cid}\', {n-1})">'

new_html = re.sub(dot_pattern, replacer, html)
print(f'Fixed {replacements} dots (1-based -> 0-based)')
for cid in ['puSheetCarousel','puDeskCarousel']:
    dots = re.findall(r'<span[^>]+onclick="goGB\(\'' + cid + r'\', (\d+)\)"', new_html)
    print(f'  {cid} dots now: {dots}')

# ── Fix 2: CSS height fix ────────────────────────────────────────
# Find <style> block
style_m = re.search(r'<style>\s*(.*?)\s*</style>', new_html, re.DOTALL)
if style_m:
    css = style_m.group(1)
    # Add fix after .gb-category-layout or at end of style block
    fix_css = '''
/* PU collection: force carousel container to square so images don't overflow */
.gb-carousel {
    aspect-ratio: 1 / 1;
    position: relative;
    overflow: hidden;
}
.gb-carousel-img {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}
'''
    new_html = new_html.replace('</style>', fix_css + '\n</style>')
    print('Added CSS fix for .gb-carousel aspect-ratio + position')
else:
    print('ERROR: could not find <style> block')

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print('File written. Size:', len(new_html))
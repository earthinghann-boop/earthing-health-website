#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix pu-earthing-mat.html:
1. Remove stray > text inside all .gb-carousel-dot spans
2. Fix dots container vertical centering: use flexbox align-center instead of
   transform:translateY(-50%) so dots truly center regardless of gap+padding math
"""
import re

path = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

print('Before:')
# Count stray > in spans
bad = len(re.findall(r'<span[^>]+>[^<]*>', html))
print('  spans with stray text:', bad)
print('  transform: translateY:', html.count('transform: translateY(-50%)'))

# ── Fix 1: Remove > text from dot spans ────────────────────────
# Pattern: <span class="gb-carousel-dot..." ... >...</span>
# The > before </span> is text content. Remove it.
# Replace ">"></span> patterns (with any attrs between > and </span>)
html = re.sub(
    r'(<span[^>]+>)>(?=</span>)',
    lambda m: m.group(1) + ' ',   # keep opening tag, replace stray > with a space
    html
)
html = re.sub(
    r'(<span[^>]+>)\s*</span>',
    lambda m: m.group(1) + '</span>',  # collapse any leftover whitespace
    html
)
# Actually the simplest: fix all spans that end with > text
# Pattern: > at end of opening tag content (between > and </span>)
# Replace "class="xxx">>"  with "class="xxx">"
# But the spans have class= and onclick= - so we need a more careful approach
# Let's just find all dot spans and strip them properly
def fix_span(m):
    # m is the full span from > to </span>
    # Remove any > or whitespace that appears as text
    inner = m.group(0)
    # Remove > that appears just before </span>
    inner = re.sub(r'>\s*</span>', '></span>', inner)
    return inner

# Better approach: find all .gb-carousel-dot spans and ensure they have no text content
def clean_span(m):
    full = m.group(0)
    # Extract tag attributes (everything between <span and >)
    attrs = re.search(r'<span([^>]*)>', full)
    if not attrs:
        return full
    attr_str = attrs.group(1)
    # Remove any text content (stuff between > and </span>)
    return '<span' + attr_str + '></span>'

# This regex matches the whole <span ...>...</span>
span_pat = r'<span[^>]*>.*?</span>'
html = re.sub(span_pat, clean_span, html, flags=re.DOTALL)

print()
print('After fix 1:')
bad2 = len(re.findall(r'<span[^>]*>[^<]', html))
print('  spans with stray text:', bad2)

# Verify: print one dot span
sample = re.search(r'<span[^>]*onclick="goGB[^"]+"[^>]*>', html)
if sample:
    print('  sample span:', repr(sample.group() + '</span>'))

# ── Fix 2: dots vertical centering via flexbox ──────────────────
# Replace:
#   top: 50%; transform: translateY(-50%);
# with:
#   top: 0; bottom: 0; align-items: center;
# This centers via flexbox, no transform needed
html = html.replace(
    'top: 50%;\n            transform: translateY(-50%);',
    'top: 0;\n            bottom: 0;\n            align-items: center;'
)

print()
print('After fix 2:')
print('  transform: translateY(-50%):', html.count('transform: translateY(-50%)'))
print('  align-items: center:', html.count('align-items: center;'))

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print()
print('Written. Size:', len(html))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix centering + > stray char in pu-earthing-mat.html.
Strategy: parse the CSS as rules, replace .gb-carousel-dots rule content entirely.
"""
import re

path = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html'
with open(path, 'rb') as f:
    raw = f.read()

# Work on text
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# ── Fix 1: remove stray > in dot spans ─────────────────────────
# Find all dot spans: <span ...>...</span> where there's stray text
def clean_span(m):
    attrs_m = re.search(r'<span([^>]*)>', m.group(0))
    if not attrs_m:
        return m.group(0)
    return '<span' + attrs_m.group(1) + '></span>'

html = re.sub(r'<span[^>]+>.*?</span>', clean_span, html, flags=re.DOTALL)

# ── Fix 2: replace .gb-carousel-dots rule content ───────────────
# Find the selector, then its block, then replace
new_dots_content = (
    "position: absolute;\n"
    "            left: 0;\n"
    "            top: 0;\n"
    "            bottom: 0;\n"
    "            display: flex;\n"
    "            flex-direction: column;\n"
    "            justify-content: center;\n"
    "            gap: 12px;\n"
    "            z-index: 3;\n"
    "            background: rgba(0,0,0,0.35);\n"
    "            padding: 10px 10px 10px 14px;\n"
    "            border-radius: 0 20px 20px 0;"
)

# Find .gb-carousel-dots { ... } in the style block
# We know there are 56 newlines between properties - use multiline search
dots_start = html.find('.gb-carousel-dots {')
dots_open = html.find('{', dots_start)
# Find the matching close brace
depth = 0
j = dots_open
while j < len(html):
    if html[j] == '{': depth += 1
    elif html[j] == '}':
        depth -= 1
        if depth == 0:
            break
    j += 1
dots_end = j + 1

old_rule = html[dots_start:dots_end]
new_rule = '.gb-carousel-dots {\n' + new_dots_content + '\n            }'

print('Old rule preview (first 200 chars):')
print(repr(old_rule[:200]))
print()
print('Old rule length:', len(old_rule))
print('New rule length:', len(new_rule))

html = html[:dots_start] + new_rule + html[dots_end:]

print()
print('After fix 2:')
print('  transform: translateY(-50%):', html.count('transform: translateY(-50%)'))
print('  justify-content: center:', html.count('justify-content: center'))
print('  > in spans:', html.count('>'))

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print()
print('Written. New size:', len(html))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pull EXACT .gb-carousel-dots CSS from groundingbedding.html (live, confirmed working)
and replace the corresponding rule in pu-earthing-mat.html — byte-for-byte identical.
Also pull the .gb-carousel-img CSS.
"""
import urllib.request, re, time

path_pu = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html'

# ── 1. Get groundingbedding.html from Vercel ────────────────────────
url = 'https://www.silveryes.com/groundingbedding.html?nocache=' + str(int(time.time()*1000))
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache'
})
with urllib.request.urlopen(req, timeout=15) as r:
    gb_html = r.read().decode('utf-8')

# Extract the <style> block
m_css = re.search(r'<style>\s*(.*?)\s*</style>', gb_html, re.DOTALL)
css = m_css.group(1)

# Extract the full .gb-carousel-dots rule text
def get_rule(css, selector):
    idx = css.find(selector + ' {')
    if idx < 0:
        return None
    # Find the { and matching }
    depth = 0; j = idx + len(selector) + 1
    while j < len(css):
        if css[j] == '{': depth += 1
        elif css[j] == '}':
            depth -= 1
            if depth == 0:
                return css[idx:j+1]
        j += 1
    return None

dots_rule_gb = get_rule(css, '.gb-carousel-dots')
img_rule_gb  = get_rule(css, '.gb-carousel-img')
print('groundingbedding .gb-carousel-dots rule:')
print(repr(dots_rule_gb))
print()
print('groundingbedding .gb-carousel-img rule:')
print(repr(img_rule_gb))

# ── 2. Apply to pu-earthing-mat.html ─────────────────────────────────
with open(path_pu, 'r', encoding='utf-8') as f:
    pu = f.read()

# Check what we have
dots_rule_pu = get_rule(pu, '.gb-carousel-dots')
print()
print('pu-earthing-mat .gb-carousel-dots BEFORE:')
print(repr(dots_rule_pu[:200]) if dots_rule_pu else 'NOT FOUND')

# Replace rules in pu HTML
pu = pu.replace(dots_rule_pu, dots_rule_gb)
pu = pu.replace(img_rule_gb,  img_rule_gb)   # same, no-op (just confirm exists)

with open(path_pu, 'w', encoding='utf-8') as f:
    f.write(pu)

dots_rule_after = get_rule(pu, '.gb-carousel-dots')
print()
print('pu-earthing-mat .gb-carousel-dots AFTER:')
print(repr(dots_rule_after))

print()
print('File size:', len(pu))
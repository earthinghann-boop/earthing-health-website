#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inject working nav + footer + main.js into pu-earthing-mat.html.
Pull them live from groundingbedding.html (confirmed working reference).
"""
import urllib.request, re, time

path_pu = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html'

# 1. Fetch groundingbedding.html
url = 'https://www.silveryes.com/groundingbedding.html?nocache=' + str(int(time.time()*1000))
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache'})
with urllib.request.urlopen(req, timeout=15) as r:
    gb_html = r.read().decode('utf-8')

# 2. Extract nav (just the element)
nav = re.search(r'<nav[^>]*>.*?</nav>', gb_html, re.DOTALL).group()
footer = re.search(r'<footer[^>]*>.*?</footer>', gb_html, re.DOTALL).group()

# 3. Strip CRLF noise from groundingbedding (it had weird CRLF on PowerShell push)
# Replace `\r\r\r\r\r\r\r` (multiple \r) with single \n
def clean(s):
    s = re.sub(r'\r+', '\n', s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()

nav_clean = clean(nav)
footer_clean = clean(footer)
print(f'Cleaned nav: {len(nav_clean)} chars')
print(f'Cleaned footer: {len(footer_clean)} chars')

# 4. Apply to pu-earthing-mat.html
with open(path_pu, 'r', encoding='utf-8') as f:
    pu = f.read()

# Remove old nav + footer if any (in case they reappear)
pu = re.sub(r'<nav[^>]*>.*?</nav>\s*', '', pu, flags=re.DOTALL)
pu = re.sub(r'<footer[^>]*>.*?</footer>\s*', '', pu, flags=re.DOTALL)

# Inject new nav right after <body>
pu = re.sub(r'(<body>\s*)', r'\1\n' + nav_clean + '\n\n', pu, count=1)

# Inject main.js before carousel IIFE (or at end of body)
if 'js/main.js' not in pu:
    pu = pu.replace(
        '<script>',
        '<script src="js/main.js"></script>\n    <script>',
        1
    )

# Inject footer before carousel IIFE script
pu = re.sub(
    r'(\s*<script>\s*\(function)',
    '\n' + footer_clean + r'\n\n    \1',
    pu,
    count=1
)

# Write
with open(path_pu, 'w', encoding='utf-8') as f:
    f.write(pu)

print()
print('Final size:', len(pu))
print('class="navbar":', 'class="navbar"' in pu)
print('images/logo/earthing-logo.png:', 'images/logo/earthing-logo.png' in pu)
print('js/main.js ref:', 'js/main.js' in pu)
print('class="footer":', 'class="footer"' in pu)

# Print first 300 chars after <body> for visual check
m = re.search(r'<body>(.*?)</nav>', pu, re.DOTALL)
if m:
    print()
    print('Body start (after nav):')
    print(repr(m.group(1)[:400]))
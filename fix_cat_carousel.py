#!/usr/bin/env python3
import re

with open('earthing-fitted-sheet.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: .cat-carousel needs to fill .cat-image container
# Change from `position: relative; width: 100%; height: 100%;` to `position: absolute; inset: 0;`
old_css = '.cat-carousel { position: relative; width: 100%; height: 100%; }'
new_css = '''.cat-carousel { position: absolute; inset: 0; width: 100%; height: 100%; }'''

if old_css in content:
    content = content.replace(old_css, new_css, 1)
    print('Fixed: .cat-carousel now uses position: absolute; inset: 0')
else:
    print('ERROR: old CSS not found')
    exit(1)

with open('earthing-fitted-sheet.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open('earthing-fitted-sheet.html', 'r', encoding='utf-8') as f:
    verify = f.read()

print(f'\n=== Verification ===')
print(f'File size: {len(verify)} bytes')
print(f'cat-carousel: absolute: {len(re.findall("cat-carousel.*position: absolute", verify))}')
print(f'cat-carousel inset: 0: {len(re.findall("cat-carousel[^{{]*inset: 0", verify))}')
print(f'Product Overview still present: {"Product Overview" in verify}')
target = r'overview-1\.jpg|overview-2\.jpg|overview-3\.jpg|overview-4\.jpg'
n = len(re.findall(target, verify))
print(f'overview refs: {n}')
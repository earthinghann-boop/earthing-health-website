#!/usr/bin/env python3
import subprocess
import re

# Get the Grounding Bedding block from commit d4f9ae1
result = subprocess.run(
    ['git', 'show', 'd4f9ae1:earthing-fitted-sheet.html'],
    capture_output=True, text=True, encoding='utf-8'
)
content = result.stdout

idx1 = content.index('<!-- Grounding Bedding')
idx2 = content.index('<!-- Material Options', idx1)
grounding_block = content[idx1:idx2]
print(f'Extracted {len(grounding_block)} chars from commit d4f9ae1')

# Read current file
with open('earthing-fitted-sheet.html', 'r', encoding='utf-8') as f:
    current = f.read()

# Find insertion point: before <!-- Material Options -->
marker = '    <!-- Material Options -->'
idx = current.index(marker)
print(f'Insertion point: {idx}')

# Insert grounding_block before Material Options
new_content = current[:idx] + grounding_block + '\n    ' + current[idx:]

with open('earthing-fitted-sheet.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

# Verify
with open('earthing-fitted-sheet.html', 'r', encoding='utf-8') as f:
    verify = f.read()

print(f'\n=== Verification ===')
print(f'File size: {len(verify)} bytes')
products = ['Grounding Fitted Sheet', 'Grounding Flat Sheet', 'Grounding Pillow Case', 'Grounding Duvet Cover', "Kid's Bedding"]
for p in products:
    count = verify.count(p)
    print(f'  {p}: {count}')
print(f'\ncategory-block divs: {len(re.findall("category-block", verify))}')
print(f'btn-cat buttons: {len(re.findall("btn-cat", verify))}')
print(f'cat-image divs: {len(re.findall("cat-image", verify))}')
print(f'cat-carousel-img tags: {len(re.findall("cat-carousel-img", verify))}')
print(f'goCatFittedSlide calls: {len(re.findall("goCatFittedSlide", verify))}')
print(f'Product Overview present: {"Product Overview" in verify}')
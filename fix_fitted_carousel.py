#!/usr/bin/env python3
import subprocess
import re

# Get the FULL grounding bedding block from the latest commit that had everything (53ff265 or 22f5c80 parent)
# 53ff265 = "Replace Fitted Sheet category card image with 4-image carousel"
result = subprocess.run(
    ['git', 'show', '53ff265:earthing-fitted-sheet.html'],
    capture_output=True, text=True, encoding='utf-8'
)
content = result.stdout

idx1 = content.index('<!-- Grounding Bedding')
idx2 = content.index('<!-- Material Options', idx1)
grounding_block = content[idx1:idx2]
print(f'Extracted {len(grounding_block)} chars from commit 53ff265 (with 4-image carousel)')

# Read current file
with open('earthing-fitted-sheet.html', 'r', encoding='utf-8') as f:
    current = f.read()

# Find the current (single-image) Fitted Sheet category block to replace
# Current structure: <img src="images/previews/fitted-sheet.jpg" alt="Grounding Fitted Sheet">
# After Fitted Sheet's cat-image, before Flat Sheet's cat-image
marker_old = '<div class="cat-image">\n                        <img src="images/previews/fitted-sheet.jpg" alt="Grounding Fitted Sheet">\n                    </div>'

if marker_old not in current:
    print('ERROR: Could not find single-image Fitted Sheet block')
    exit(1)

# New block: 4-image carousel structure
new_block = '''<div class="cat-image">
                        <div class="cat-carousel">
                            <img src="images/earthing-fitted/overview-1.jpg" alt="Grounding Fitted Sheet" class="cat-carousel-img active">
                            <img src="images/earthing-fitted/overview-2.jpg" alt="Grounding Fitted Sheet" class="cat-carousel-img">
                            <img src="images/earthing-fitted/overview-3.jpg" alt="Grounding Fitted Sheet" class="cat-carousel-img">
                            <img src="images/earthing-fitted/overview-4.jpg" alt="Grounding Fitted Sheet" class="cat-carousel-img">
                            <div class="cat-carousel-dots">
                                <span class="cat-dot active" onclick="goCatFittedSlide(0)"></span>
                                <span class="cat-dot" onclick="goCatFittedSlide(1)"></span>
                                <span class="cat-dot" onclick="goCatFittedSlide(2)"></span>
                                <span class="cat-dot" onclick="goCatFittedSlide(3)"></span>
                            </div>
                        </div>
                    </div>'''

current = current.replace(marker_old, new_block, 1)
print('Replaced single-image Fitted Sheet block with 4-image carousel')

with open('earthing-fitted-sheet.html', 'w', encoding='utf-8') as f:
    f.write(current)

# Verify
with open('earthing-fitted-sheet.html', 'r', encoding='utf-8') as f:
    verify = f.read()

print(f'\n=== Verification ===')
print(f'File size: {len(verify)} bytes')
target = 'previews/fitted-sheet\\.jpg'
n = len(re.findall(target, verify))
print(f'previews/fitted-sheet.jpg refs: {n} (should be 0)')
print(f'cat-carousel-img tags: {len(re.findall("cat-carousel-img", verify))} (4 + 4 CSS = 8)')
print(f'goCatFittedSlide calls: {len(re.findall("goCatFittedSlide", verify))} (4 + 1 = 5)')
print(f'earthing-fitted/overview refs: {len(re.findall("earthing-fitted/overview", verify))} (4 + 4 = 8)')
print(f'Category JS IIFE present: {"Category carousel (Fitted Sheet 4 images)" in verify}')
print(f'Product Overview present: {"Product Overview" in verify}')
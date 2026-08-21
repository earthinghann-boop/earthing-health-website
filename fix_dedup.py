#!/usr/bin/env python3
"""Remove image 6 from grCarousel (duplicate of image 1)"""
import os

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
HTML = os.path.join(WD, 'grounding-blanket.html')
IMG = os.path.join(WD, 'images', 'products', 'grounding_blanket', '6.jpg')

with open(HTML, encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '\n            <img src="images/products/grounding_blanket/6.jpg" alt="Grounding Blanket Extra" class="gb-carousel-img">',
    '', 1
)
html = html.replace(
    '\n            <button class="gb-carousel-dot" onclick="goGB(\'grCarousel\',5)"></button>',
    '', 1
)
print('Removed 6th image and dot from HTML')

with open(HTML, 'w', encoding='utf-8') as f:
    f.write(html)

if os.path.exists(IMG):
    os.remove(IMG)
    print('Deleted 6.jpg')

# Verify
with open(HTML, encoding='utf-8') as f:
    chk = f.read()
img_count = chk.count('grounding_blanket/')
dot_count = chk.count("goGB('grCarousel'")
print(f'grounding_blanket/ refs: {img_count} (expect 5)')
print(f"goGB('grCarousel' refs: {dot_count} (expect 5)")
print(f'6.jpg refs: {chk.count("6.jpg")} (expect 0)')

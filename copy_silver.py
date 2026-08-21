#!/usr/bin/env python3
"""Copy silveryes002.jpg to images/products/groundingbedding/colors/colors.jpg (square-cropped to 900px wide as in blanket style)"""
import os
from PIL import Image
import shutil

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
SRC = r'C:\Users\18574\Desktop\EARTHING\silveryes网站\silveryes002.jpg'
DST_DIR = os.path.join(WD, 'images', 'products', 'groundingbedding', 'colors')
DST = os.path.join(DST_DIR, 'colors.jpg')

os.makedirs(DST_DIR, exist_ok=True)

# Resize to square 900 (matches grounding-blanket Available Colors style)
img = Image.open(SRC).convert('RGBA')
w, h = img.size
print(f'Original: {w}x{h}')
if w > h:
    new_w = h; x = (w - new_w) // 2
    img = img.crop((x, 0, x + new_w, h))
elif h > w:
    new_h = w; y = (h - new_h) // 2
    img = img.crop((0, y, w, y + new_h))
img = img.resize((900, 900), Image.LANCZOS)
bg = Image.new('RGB', (900, 900), (255, 255, 255))
bg.paste(img, (0, 0))
bg.save(DST, 'JPEG', quality=85)
print(f'Saved: {DST}')
print(f'Size: {os.path.getsize(DST):,}b')
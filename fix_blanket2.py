#!/usr/bin/env python3
"""Fix grounding-blanket.html:
1. Available Colors: fix centering (use margin:0 auto instead of text-align:center)
2. Grounding images: re-resize to fill 1200x1200 without white padding
"""
import os
from PIL import Image

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
SRC = r'C:\Users\18574\Desktop\EARTHING\image\法兰绒'

# ── Fix 1: Re-resize grounding images to FILL 1200x1200 (no padding) ──
gr_dir = os.path.join(WD, 'images', 'products', 'grounding_blanket')
gr_files = [
    ('换脸安吉丽娜.png', '1.jpg'),
    ('xxjdfalksjflsajdlfdfdsf.webp', '2.jpg'),
    ('3812581e-fef3-4257-8b20-e2c768025a48.__CR0,0,300,300_PT0_SX300_V1___.jpg', '3.jpg'),
    ('7_ba10d0ec-a41e-4125-ba23-cb33d3955bc7.jpg', '4.jpg'),
    ('71VUT0FboKL._AC_SX679_.jpg', '5.jpg'),
]

def fill_resize(src_path, dst_path, target=1200, quality=85):
    """Resize image to fill 1200x1200 canvas (crop to square if needed)"""
    img = Image.open(src_path).convert('RGBA')
    # Calculate crop to make it square
    w, h = img.size
    if w > h:
        # Wider: crop sides
        new_w = h
        x = (w - new_w) // 2
        img = img.crop((x, 0, x + new_w, h))
    elif h > w:
        # Taller: crop top/bottom
        new_h = w
        y = (h - new_h) // 2
        img = img.crop((0, y, w, y + new_h))
    # Now w == h, resize to target
    img = img.resize((target, target), Image.LANCZOS)
    # Convert to RGB for JPEG
    background = Image.new('RGB', (target, target), (255, 255, 255))
    background.paste(img, (0, 0))
    background.save(dst_path, 'JPEG', quality=quality)
    return os.path.getsize(dst_path)

print('=== Re-resize grounding images (fill 1200x1200) ===')
for src_name, dst_name in gr_files:
    p = os.path.join(SRC, src_name)
    dst = os.path.join(gr_dir, dst_name)
    sz = fill_resize(p, dst)
    print(f'  {src_name} -> {sz:,}b')

# ── Fix 2: Fix Available Colors centering in HTML ─────────────────
with open(os.path.join(WD, 'grounding-blanket.html'), encoding='utf-8') as f:
    html = f.read()

# Find and replace the Available Colors section
old_ac = '''            <div style="text-align:center;">
                <img src="images/products/blanket_colors/colors.jpg" alt="Available Colors" style="max-width:900px;width:100%;border-radius:10px;box-shadow:0 6px 25px var(--color-shadow);">
            </div>'''

new_ac = '''            <div style="max-width:900px;margin:0 auto;">
                <img src="images/products/blanket_colors/colors.jpg" alt="Available Colors" style="width:100%;border-radius:10px;box-shadow:0 6px 25px var(--color-shadow);display:block;">
            </div>'''

if old_ac in html:
    html = html.replace(old_ac, new_ac, 1)
    print('\nAvailable Colors centering fixed')
else:
    print('\nWARNING: old Available Colors block not found')
    # Show what's there
    pos = html.find('Available Colors')
    if pos > 0:
        print(repr(html[pos:pos+500]))

with open(os.path.join(WD, 'grounding-blanket.html'), 'w', encoding='utf-8') as f:
    f.write(html)

print('\nDone!')

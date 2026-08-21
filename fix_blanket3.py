#!/usr/bin/env python3
"""Resize grounding_blanket images to 550x550 fill + update HTML carousel CSS"""
import os
from PIL import Image

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
SRC = r'C:\Users\18574\Desktop\EARTHING\image\法兰绒'
SIZE = 550

gr_dir = os.path.join(WD, 'images', 'products', 'grounding_blanket')
gr_files = [
    ('换脸安吉丽娜.png', '1.jpg'),
    ('xxjdfalksjflsajdlfdfdsf.webp', '2.jpg'),
    ('3812581e-fef3-4257-8b20-e2c768025a48.__CR0,0,300,300_PT0_SX300_V1___.jpg', '3.jpg'),
    ('7_ba10d0ec-a41e-4125-ba23-cb33d3955bc7.jpg', '4.jpg'),
    ('71VUT0FboKL._AC_SX679_.jpg', '5.jpg'),
]

def fill_resize(src_path, dst_path, target=SIZE, quality=85):
    img = Image.open(src_path).convert('RGBA')
    w, h = img.size
    if w > h:
        new_w = h
        x = (w - new_w) // 2
        img = img.crop((x, 0, x + new_w, h))
    elif h > w:
        new_h = w
        y = (h - new_h) // 2
        img = img.crop((0, y, w, y + new_h))
    img = img.resize((target, target), Image.LANCZOS)
    bg = Image.new('RGB', (target, target), (255, 255, 255))
    bg.paste(img, (0, 0))
    bg.save(dst_path, 'JPEG', quality=quality)
    return os.path.getsize(dst_path)

print(f'=== Resize grounding images to {SIZE}x{SIZE} ===')
for src_name, dst_name in gr_files:
    p = os.path.join(SRC, src_name)
    sz = fill_resize(p, os.path.join(gr_dir, dst_name))
    print(f'  {src_name}: {sz:,}b')

# ── Update HTML: fix carousel image CSS ────────────────────────────
with open(os.path.join(WD, 'grounding-blanket.html'), encoding='utf-8') as f:
    html = f.read()

# Update grCarousel CSS to 550x550
old_gr_css = '''        #grCarousel .gb-carousel-img {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 10px;
        }'''
new_gr_css = '''        #grCarousel .gb-carousel-img {
            position: absolute;
            inset: 0;
            width: 550px;
            height: 550px;
            object-fit: cover;
            border-radius: 10px;
            left: 50%;
            transform: translateX(-50%);
        }'''

if old_gr_css in html:
    html = html.replace(old_gr_css, new_gr_css, 1)
    print('\ngrCarousel img CSS updated to 550x550')
else:
    print('\nWARNING: old grCarousel CSS not found')
    # Find it
    pos = html.find('#grCarousel')
    if pos > 0:
        print(repr(html[pos:pos+400]))

# Also update the container dimensions
old_container = '''        #grCarousel {
            position: relative;
            width: 100%;
            aspect-ratio: 1 / 1;
            overflow: hidden;
            border-radius: 10px;
        }'''
new_container = '''        #grCarousel {
            position: relative;
            width: 550px;
            height: 550px;
            overflow: hidden;
            border-radius: 10px;
            margin: 0 auto;
        }'''

if old_container in html:
    html = html.replace(old_container, new_container, 1)
    print('grCarousel container updated to 550x550')
else:
    print('WARNING: old grCarousel container not found')
    pos = html.find('#grCarousel')
    if pos > 0:
        print(repr(html[pos:pos+300]))

# Also update dots container to center
old_dots_css = '''        #grCarousel .gb-carousel-dots {
            position: absolute;
            left: 16px;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            flex-direction: column;
            gap: 8px;
        }'''
new_dots_css = '''        #grCarousel .gb-carousel-dots {
            position: absolute;
            left: 16px;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            flex-direction: column;
            gap: 8px;
            z-index: 10;
        }'''

if old_dots_css in html:
    html = html.replace(old_dots_css, new_dots_css, 1)
    print('grCarousel dots z-index updated')

with open(os.path.join(WD, 'grounding-blanket.html'), 'w', encoding='utf-8') as f:
    f.write(html)
print('\nHTML saved.')

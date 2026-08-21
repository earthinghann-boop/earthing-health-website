#!/usr/bin/env python3
"""Resize images for grounding-blanket.html - EMF + Colors (Grounding 5 images pending confirmation)"""
import os
from PIL import Image

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
SRC = r'C:\Users\18574\Desktop\EARTHING'

def smart_resize(src_path, dst_path, quality=85):
    """Resize to 1200x1200 with white background, convert everything to JPEG"""
    img = Image.open(src_path).convert('RGBA')
    background = Image.new('RGB', (1200, 1200), (255, 255, 255))
    img.thumbnail((1200, 1200), Image.LANCZOS)
    x = (1200 - img.width) // 2
    y = (1200 - img.height) // 2
    background.paste(img, (x, y), img.split()[-1] if img.mode == 'RGBA' else None)
    background.save(dst_path, 'JPEG', quality=quality)
    return os.path.getsize(dst_path)

# ── 1. EMF Blanket images (4 images) ──────────────────────────────
emf_dir = os.path.join(WD, 'images', 'products', 'emf_blanket')
os.makedirs(emf_dir, exist_ok=True)
emf_src = os.path.join(SRC, r'image\盖毯')
emf_files = [
    ('1F0A1813.jpg', '1.jpg'),
    ('1F0A1816.jpg', '2.jpg'),
    ('1F0A1812.jpg', '3.jpg'),
    ('1F0A1820.jpg', '4.jpg'),
]
print('=== EMF images ===')
for src_name, dst_name in emf_files:
    p = os.path.join(emf_src, src_name)
    dst = os.path.join(emf_dir, dst_name)
    sz = smart_resize(p, dst)
    print(f'  {src_name} -> {dst_name}: {sz:,}b')

# ── 2. Available Colors (1 image) ──────────────────────────────────
ac_dir = os.path.join(WD, 'images', 'products', 'blanket_colors')
os.makedirs(ac_dir, exist_ok=True)
ac_src = os.path.join(SRC, r'silveryes网站')
p = os.path.join(ac_src, 'silver004.jpg')
dst = os.path.join(ac_dir, 'colors.jpg')
sz = smart_resize(p, dst)
print(f'\n=== Available Colors ===')
print(f'  silver004.jpg -> colors.jpg: {sz:,}b')

# ── 3. Grounding images (5 images, pending user confirmation) ───────
gr_dir = os.path.join(WD, 'images', 'products', 'grounding_blanket')
os.makedirs(gr_dir, exist_ok=True)
gr_src = os.path.join(SRC, r'image\法兰绒')
gr_files = [
    ('换脸安吉丽娜.png', '1.jpg'),
    ('xxjdfalksjflsajdlfdfdsf.webp', '2.jpg'),
    ('3812581e-fef3-4257-8b20-e2c768025a48.__CR0,0,300,300_PT0_SX300_V1___.jpg', '3.jpg'),
    ('7_ba10d0ec-a41e-4125-ba23-cb33d3955bc7.jpg', '4.jpg'),
    ('71VUT0FboKL._AC_SX679_.jpg', '5.jpg'),
]
print(f'\n=== Grounding images (5, pending confirmation) ===')
for src_name, dst_name in gr_files:
    p = os.path.join(gr_src, src_name)
    dst = os.path.join(gr_dir, dst_name)
    sz = smart_resize(p, dst)
    print(f'  {src_name} -> {dst_name}: {sz:,}b')

print('\nDone!')

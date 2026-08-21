#!/usr/bin/env python3
"""Resize + deploy images for grounding-blanket.html"""
import os, shutil
from PIL import Image

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
SRC = r'C:\Users\18574\Desktop\EARTHING'

sets = {
    'emf_blanket': {
        'src': os.path.join(SRC, r'image\盖毯'),
        'files': [
            ('1F0A1813.jpg', '1.jpg'),
            ('1F0A1816.jpg', '2.jpg'),
            ('1F0A1812.jpg', '3.jpg'),
            ('1F0A1820.jpg', '4.jpg'),
        ]
    },
    'blanket_colors': {
        'src': os.path.join(SRC, r'silveryes网站'),
        'files': [
            ('silver004.jpg', 'colors.jpg'),
        ]
    },
    'grounding_blanket': {
        'src': os.path.join(SRC, r'image\法兰绒'),
        'files': [
            ('换脸安吉丽娜.png', '1.png'),
            ('xxjdfalksjflsajdlfdfdsf.webp', '2.webp'),
            ('3812581e-fef3-4257-8b20-e2c768025a48.__CR0,0,300,300_PT0_SX300_V1___.jpg', '3.jpg'),
            ('7_ba10d0ec-a41e-4125-ba23-cb33d3955bc7.jpg', '4.jpg'),
            ('71VUT0FboKL._AC_SX679_.jpg', '5.jpg'),
        ]
    },
}

def resize(src_path, dst_path, quality=85):
    img = Image.open(src_path)
    # Convert RGBA to RGB if needed (for PNG with transparency)
    if img.mode in ('RGBA', 'P'):
        background = Image.new('RGB', img.size, (255, 255, 255))
        if img.mode == 'P':
            img = img.convert('RGBA')
        background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
        img = background
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Resize to 1200x1200
    img.thumbnail((1200, 1200), Image.LANCZOS)
    # Create white canvas
    canvas = Image.new('RGB', (1200, 1200), (255, 255, 255))
    x = (1200 - img.width) // 2
    y = (1200 - img.height) // 2
    canvas.paste(img, (x, y))
    canvas.save(dst_path, 'JPEG', quality=quality)
    return os.path.getsize(dst_path)

for subdir, info in sets.items():
    dst_dir = os.path.join(WD, 'images', 'products', subdir)
    os.makedirs(dst_dir, exist_ok=True)
    for src_name, dst_name in info['files']:
        src_path = os.path.join(info['src'], src_name)
        dst_path = os.path.join(dst_dir, dst_name)
        if os.path.exists(src_path):
            size = resize(src_path, dst_path)
            print(f'  OK  {src_name} -> {subdir}/{dst_name}: {size:,}b')
        else:
            print(f'  MISSING: {src_path}')

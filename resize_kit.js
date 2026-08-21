#!/usr/bin/env python3
"""Resize grounding-kit images to 550x550 fill (white background)"""
import os
from PIL import Image

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
SRC = r'C:\Users\18574\Desktop\EARTHING\接地线资料\plugs'
SIZE = 550

# Categories
specs = {
    # 1. Grounding cord - 6 types
    'cord': [
        ('二代线轮播1.png', '1.jpg'),       # gen 2
        ('2 in1cord1.png', '2.jpg'),        # 2 in 1 cord
        ('10m接地棒.png', '3.jpg'),         # rod cord
        ('snake cord1.jpg', '4.jpg'),       # snake cord
        ('golden us cord1.png', '5.jpg'),   # golden cord
        ('双头线.png', '6.jpg'),            # DBL-ends cord
    ],
    # 2. Plugs - 6 regions with New US Cord
    'plug': [
        ('New US+plugs/EU+New US Cord.png', '1.jpg'),  # EU
        ('New US+plugs/AU+New US Cord.png', '2.jpg'),  # AU
        ('New US+plugs/UK+New US Cord.png', '3.jpg'),  # UK
        ('New US+plugs/ITY+New US Cord.png', '4.jpg'), # ITY
        ('New US+plugs/CH+New US Cord.png', '5.jpg'),  # CH
        ('New US+plugs/ISR+New US Cord.png', '6.jpg'), # ISR
    ],
    # 3. Tester - 5 types
    'tester': [
        ('cords&plugs/白仪.avif', '1.jpg'),     # tester pen (white)
        ('51r0MAxGZXL._AC_SX679_.jpg', '2.jpg'), # conductive tester
        ('EU Outlet Checker.png', '3.jpg'),
        ('US Outlet Checker.png', '4.jpg'),
        ('UK Outlet Checker.png', '5.jpg'),
    ],
}

def fill_resize(src_path, dst_path, target=SIZE, quality=85):
    img = Image.open(src_path).convert('RGBA')
    w, h = img.size
    if w > h:
        new_w = h; x = (w - new_w) // 2
        img = img.crop((x, 0, x + new_w, h))
    elif h > w:
        new_h = w; y = (h - new_h) // 2
        img = img.crop((0, y, w, y + new_h))
    img = img.resize((target, target), Image.LANCZOS)
    bg = Image.new('RGB', (target, target), (255, 255, 255))
    bg.paste(img, (0, 0))
    bg.save(dst_path, 'JPEG', quality=quality)
    return os.path.getsize(dst_path)

for cat, items in specs.items():
    dst_dir = os.path.join(WD, 'images', 'products', 'kit_' + cat)
    os.makedirs(dst_dir, exist_ok=True)
    print(f'--- kit_{cat} ---')
    for src_rel, dst_name in items:
        src = os.path.join(SRC, src_rel)
        dst = os.path.join(dst_dir, dst_name)
        if not os.path.exists(src):
            print(f'  MISSING: {src}')
            continue
        sz = fill_resize(src, dst)
        print(f'  {src_rel} -> {dst_name}: {sz:,}b')

print('Done!')
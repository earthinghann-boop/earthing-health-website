#!/usr/bin/env python3
"""Update kit_plug (use bare plugs, not cord+plug combo)
Update kit_tester/2.jpg to use 测试笔/ea6d1130...jpg
"""
import os
from PIL import Image

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
SRC = r'C:\Users\18574\Desktop\EARTHING\接地线资料\plugs'
TESTER_DIR = r'C:\Users\18574\Desktop\EARTHING\接地线资料\测试笔'
SIZE = 550

# Plugs - 6 bare plugs from plugs root
plug_specs = [
    ('EU插头.png', '1.jpg'),
    ('AU插头.png', '2.jpg'),
    ('UK插头.png', '3.jpg'),
    ('ITY插头.png', '4.jpg'),
    ('CH插头.png', '5.jpg'),
    ('ISR插头.png', '6.jpg'),
]

# Tester - update 2.jpg only
tester_2 = (TESTER_DIR + r'\ea6d1130-7beb-4f63-a6e9-03d0eb3d3145.__CR0,0,300,300_PT0_SX300_V1___.jpg',
            r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\images\products\kit_tester\2.jpg')

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

# Process plugs
print('=== kit_plug (bare) ===')
plug_dst_dir = os.path.join(WD, 'images', 'products', 'kit_plug')
for src_name, dst_name in plug_specs:
    src = os.path.join(SRC, src_name)
    dst = os.path.join(plug_dst_dir, dst_name)
    if not os.path.exists(src):
        print(f'  MISSING: {src_name}')
        continue
    sz = fill_resize(src, dst)
    print(f'  {src_name} -> {dst_name}: {sz:,}b')

# Process tester/2.jpg
print('\n=== kit_tester/2.jpg ===')
src, dst = tester_2
if os.path.exists(src):
    sz = fill_resize(src, dst)
    print(f'  ea6d1130 -> 2.jpg: {sz:,}b')
else:
    print('  MISSING:', src)

print('Done!')
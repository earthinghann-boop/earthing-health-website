#!/usr/bin/env python3
"""Replace grounding images 1 and 6 with 脸替换图片2.png (550x550)"""
import os
from PIL import Image

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
SRC = r'C:\Users\18574\Desktop\EARTHING\image\法兰绒'
DST = os.path.join(WD, 'images', 'products', 'grounding_blanket')
SIZE = 550

src = os.path.join(SRC, '脸替换图片2.png')

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

sz1 = fill_resize(src, os.path.join(DST, '1.jpg'))
sz6 = fill_resize(src, os.path.join(DST, '6.jpg'))
print(f'1.jpg: {sz1:,}b')
print(f'6.jpg: {sz6:,}b')
print('Done!')

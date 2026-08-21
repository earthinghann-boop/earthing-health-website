import os
from PIL import Image

SRC = r'C:\Users\18574\Desktop\EARTHING\image\法兰绒'
imgs = [
    '微信图片_20251110104448_510_19.jpg',
    '微信图片_20251110104512_511_19.jpg',
]
for f in imgs:
    p = os.path.join(SRC, f)
    if os.path.exists(p):
        sz = os.path.getsize(p)
        img = Image.open(p)
        print(f'OK  {f}: {img.size} {sz:,}b')
    else:
        print(f'MISSING: {f}')

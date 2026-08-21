#!/usr/bin/env python3
"""Resize all EMF wearing images to 550x550 fill (square, cropped center)"""
import os
from PIL import Image

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
EAR = r'C:\Users\18574\Desktop\EARTHING'
SIZE = 550

sets = {
    # 1. shawl
    'shawl': (os.path.join(EAR, r'image\披风'),
              [('Se7cbd550064b47f888c7b4974d51601f3.png', '1.jpg'),
               ('S06e25cff543f45c88009f3e87b2065d5T.png', '2.jpg'),
               ('Sf5c8285e1ac243498f3abfe333293b79M.png', '3.jpg'),
               ('S34f66e3f88124b7cbe04dbac7842bf39k.png', '4.jpg'),
               ('Sef778ae1471f45d09eb20f3a12c88947M.png', '5.jpg')]),
    # 2. fishman cap
    'fishman_cap': (os.path.join(EAR, r'image\cap\fishman cap'),
                    [('黑女帽.png', '1.jpg'),
                     ('白男帽.png', '2.jpg'),
                     ('ChatGPT Image 2026年7月22日 11_35_23.png', '3.jpg'),
                     ('623380f3d0390f2533c6291042bbc525.jpg', '4.jpg')]),
    # 3. beanie
    'beanie': (os.path.join(EAR, r'image\cap\Beanie\beanie自己拍\原图'),
               [('1.jpg', '1.jpg'),
                ('2.jpg', '2.jpg'),
                ('3.jpg', '3.jpg'),
                ('4.jpg', '4.jpg'),
                ('5.jpg', '5.jpg')]),
    # 4. hood
    'hood': (os.path.join(EAR, r'image\cap\Hood'),
             [('81EIqkla9fL._AC_SY550_.jpg', '1.jpg'),
              ('71d3opedxoL._AC_SX569_.jpg', '2.jpg'),
              ('81NfzfaURvL._AC_SY879_.png', '3.jpg'),
              ('81I4OTpEPxL._AC_SY879_.jpg', '4.jpg'),
              ('91s4ZovQPML._AC_SY879_.jpg', '5.jpg')]),
    # 5. baseball cap
    'baseball_cap': (os.path.join(EAR, r'image\cap\鸭舌帽'),
                     [('鸭舌帽侧面.png', '1.jpg'),
                      ('鸭舌帽正面.png', '2.jpg'),
                      ('ScreenShot_2026-08-21_142810_822.png', '3.jpg')]),
    # 6. curtain (5 .avif files)
    'curtain': (os.path.join(EAR, r'image\curtain'),
                [('H1d5d758eb330424d9f24cf7cc3b1aca2X.avif', '1.jpg'),
                 ('H43118939a51844e0aa6ae9582530665d8.avif', '2.jpg'),
                 ('Ha753ee4036464bf5b74143d7215ab538N.avif', '3.jpg'),
                 ('Hd7814b7f8d6347edb9b88e6ab800cc00D.avif', '4.jpg'),
                 ('He5042a9910924b999daec2428a7d9f0bm.avif', '5.jpg')]),
    # 7. socks
    'socks': (os.path.join(EAR, r'image\袜子'),
              [('H84bbddc4af784b4bb35458d6d82a91523.png', '1.jpg'),
               ('H876cb02d80334a00ae58c60ad6fb1ac8B.png', '2.jpg'),
               ('H7838b2b13cee469d93b110f19f4234317.png', '3.jpg'),
               ('Sed54d91371084fc2bc6fff86eb6fec5fK.png', '4.jpg')]),
    # 8. eye mask
    'eye_mask': (os.path.join(EAR, r'image\眼罩'),
                 [('微信图片_20260722104525_11983_15.png', '1.jpg'),
                  ('全部颜色.png', '2.jpg'),
                  ('微信图片_20260722104348_11979_15.jpg', '3.jpg')]),
    # 9. sleeve shirt - 衬衫2/衬衫3 子目录
    'sleeve_shirt': (None,
                     [('衬衫2/342.jpg', '1.jpg'),
                      ('衬衫2/346.jpg', '2.jpg'),
                      ('衬衫3/124.jpg', '3.jpg'),
                      ('衬衫3/122.jpg', '4.jpg')]),
    # 10. loungewear - 2 from Ma's宝拉 + 2 from 模特床
    'loungewear': (None,
                   [("服装/Ma's 宝拉3件 已修/2277 - 副本.jpg", '1.jpg'),
                    ("服装/Ma's 宝拉3件 已修/2283 - 副本.jpg", '2.jpg'),
                    ('模特床/DSC08124.JPG', '3.jpg'),
                    ('模特床/DSC08100.JPG', '4.jpg')]),
    # 11. boxer shorts
    'boxer': (os.path.join(EAR, r'image\服装\1.30马特\1'),
              [('1725.jpg', '1.jpg'),
               ('1729.jpg', '2.jpg'),
               ('1743.jpg', '3.jpg'),
               ('1748.jpg', '4.jpg')]),
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

for name, (base, files) in sets.items():
    if base is None:
        base = os.path.join(EAR, r'image\衬衫' if 'shirt' in name else r'image')
    dst_dir = os.path.join(WD, 'images', 'products', name)
    os.makedirs(dst_dir, exist_ok=True)
    print(f'--- {name} ---')
    for src_rel, dst_name in files:
        src = os.path.join(base, src_rel)
        dst = os.path.join(dst_dir, dst_name)
        if not os.path.exists(src):
            print(f'  MISSING: {src}')
            continue
        sz = fill_resize(src, dst)
        print(f'  {src_rel} -> {dst_name}: {sz:,}b')
print('Done!')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
一次性完成所有修改：
1. resize PU Sheet 4张 -> pu_sheet/1..4.jpg
2. resize PU Desk Mat 4张 -> pu_desk_mat/1..4.jpg
3. 重写 pu-earthing-mat.html（删PU Yoga Mat；换图路径；hero badge从3改成2）
4. 验证
"""
import os, re, shutil
from PIL import Image

OUT = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
os.chdir(OUT)

# ── 1. resize & save ──────────────────────────────────────────────
def resize_save(src, dst):
    im = Image.open(src).convert('RGB')
    im.thumbnail((1200, 1200), Image.LANCZOS)
    if im.size[0] != im.size[1]:
        w, h = im.size
        s = max(w, h)
        pad = Image.new('RGB', (s, s), (255, 255, 255))
        pad.paste(im, ((s-w)//2, (s-h)//2))
        im = pad
    im.save(dst, 'JPEG', quality=85, optimize=True)
    print(f'  -> {os.path.getsize(dst)//1024}KB  {dst}')

print('[1] PU Sheet 4张')
src_sheet = r'C:\Users\18574\Desktop\EARTHING\image\PU垫\皮革垫\WPS图片批量处理'
sheet_order = ['445A4539.jpg','445A4529.jpg','445A4527.jpg','1F0A4103.jpg']
for i, f in enumerate(sheet_order, 1):
    resize_save(os.path.join(src_sheet, f), f'images/products/pu_sheet/{i}.jpg')

print('[2] PU Desk Mat 4张')
src_desk = r'C:\Users\18574\Desktop\EARTHING\image\台垫26x68'
desk_order = [
    'Conductive-Keyboard-Foot-Mat-Sleep-Earthed-Plug-Cable-1-Full-Keyboard-Desk-Closeup-Web-1500.jpg',
    'earthing-and-grounding-mat-68-x-25-cm-5342316.webp',
    '61cObI19fpL._AC_.jpg',
    '81v9WvyxERL._AC_SX679_.jpg'
]
for i, f in enumerate(desk_order, 1):
    resize_save(os.path.join(src_desk, f), f'images/products/pu_desk_mat/{i}.jpg')

# ── 2. 重写 HTML ─────────────────────────────────────────────────
with open('pu-earthing-mat.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 2a. 删除 pu_yoga_mat 整个 section（从 <!-- Category: PU Yoga Mat --> 到 </section>）
html = re.sub(
    r'\n\n<!-- Category: PU Yoga Mat -->.*?\n</section>',
    '',
    html,
    flags=re.DOTALL
)

# 2b. 删掉 pu_yoga_mat 图片目录（不再需要）
for i in range(1, 5):
    p = f'images/products/pu_yoga_mat/{i}.jpg'
    if os.path.exists(p):
        os.remove(p)
        print(f'  rm {p}')
if os.path.exists('images/products/pu_yoga_mat'):
    os.rmdir('images/products/pu_yoga_mat')
    print('  rmdir pu_yoga_mat/')

# 2c. 把 CAROUSELS 数组从3项改成2项
html = re.sub(
    r"\['puSheetCarousel','puDeskCarousel','puYogaCarousel'\]",
    "['puSheetCarousel','puDeskCarousel']",
    html
)

# 2d. hero badge 从 "Three Product Forms" 改成 "Two Product Forms"
html = html.replace(
    '<span class="hero-badge">Three Product Forms</span>',
    '<span class="hero-badge">Two Product Forms</span>'
)

# 2e. hero description 也更新（从 "three" 改成 "two"）
html = html.replace(
    'three professional grounding products',
    'two professional grounding products'
)

# 2f. PU Desk Mat section：图片路径从 pu_desk_mat/1~4 确认不变
#     (已经在HTML里写的是 pu_desk_mat/1.jpg ... 无需改)
#     PU Sheet 路径已在HTML里是 pu_sheet/1.jpg ... 无需改

with open('pu-earthing-mat.html', 'w', encoding='utf-8') as f:
    f.write(html)

# ── 3. 验证 ───────────────────────────────────────────────────────
with open('pu-earthing-mat.html', 'r', encoding='utf-8') as f:
    t = f.read()

print()
print('[3] 验证')
print('  size:', len(t))
print('  gb-category-section blocks:', t.count('<section class="gb-category-section">'))
print('  gb-carousel-img:', t.count('<img'))
print('  CAROUSELS 2项:', "['puSheetCarousel','puDeskCarousel']" in t)
print('  Yoga section removed:', 'PU Yoga Mat' not in t)
print('  hero 3->2:', 'Two Product Forms' in t)
print('  Three Product Forms gone:', 'Three Product Forms' not in t)

for cat in ['pu_sheet','pu_desk_mat']:
    ok = sum(1 for i in [1,2,3,4] if f'images/products/{cat}/{i}.jpg' in t)
    print(f'  {cat} imgs in HTML: {ok}/4')

print()
print('local imgs:')
for cat in ['pu_sheet','pu_desk_mat']:
    sz = sum(os.path.getsize(f'images/products/{cat}/{i}.jpg') for i in [1,2,3,4] if os.path.exists(f'images/products/{cat}/{i}.jpg'))
    print(f'  {cat}: {sz//1024}KB total')
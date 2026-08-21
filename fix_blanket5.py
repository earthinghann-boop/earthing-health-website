#!/usr/bin/env python3
"""Fix grounding-blanket.html:
1. Replace grounding image 1 (安吉丽娜 -> 微信图1)
2. Add grounding image 6 (微信图2) -> becomes 6th carousel image
3. Fix Natural Grounding section: wrong class + add carousel width constraint
4. Resize 550x550
"""
import os
from PIL import Image

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
SRC = r'C:\Users\18574\Desktop\EARTHING\image\法兰绒'
DST = os.path.join(WD, 'images', 'products', 'grounding_blanket')
SIZE = 550

# ── 1. Replace image 1 + add image 6 ──────────────────────────────
img_map = [
    ('微信图片_20251110104448_510_19.jpg', '1.jpg'),
    ('微信图片_20251110104512_511_19.jpg', '6.jpg'),
]

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

print('=== Resize new grounding images ===')
for src_name, dst_name in img_map:
    p = os.path.join(SRC, src_name)
    sz = fill_resize(p, os.path.join(DST, dst_name))
    print(f'  {src_name} -> {dst_name}: {sz:,}b')

# ── 2. Update HTML ────────────────────────────────────────────────
with open(os.path.join(WD, 'grounding-blanket.html'), encoding='utf-8') as f:
    html = f.read()

# Replace old image 1 with new
old_img1 = 'src="images/products/grounding_blanket/1.jpg"'
new_img1 = 'src="images/products/grounding_blanket/1.jpg"'  # same path, file already replaced
print(f'\nImage 1 replaced (file on disk)')

# Find grCarousel img block and add 6th image after 5th
old_carousel_imgs = '''            <img src="images/products/grounding_blanket/1.jpg" alt="Grounding Blanket Lifestyle" class="gb-carousel-img active">
            <img src="images/products/grounding_blanket/2.jpg" alt="Grounding Blanket Material" class="gb-carousel-img">
            <img src="images/products/grounding_blanket/3.jpg" alt="Grounding Blanket Close-up" class="gb-carousel-img">
            <img src="images/products/grounding_blanket/4.jpg" alt="Grounding Blanket Style" class="gb-carousel-img">
            <img src="images/products/grounding_blanket/5.jpg" alt="Grounding Blanket Detail" class="gb-carousel-img">'''

new_carousel_imgs = '''            <img src="images/products/grounding_blanket/1.jpg" alt="Grounding Blanket Lifestyle" class="gb-carousel-img active">
            <img src="images/products/grounding_blanket/2.jpg" alt="Grounding Blanket Material" class="gb-carousel-img">
            <img src="images/products/grounding_blanket/3.jpg" alt="Grounding Blanket Close-up" class="gb-carousel-img">
            <img src="images/products/grounding_blanket/4.jpg" alt="Grounding Blanket Style" class="gb-carousel-img">
            <img src="images/products/grounding_blanket/5.jpg" alt="Grounding Blanket Detail" class="gb-carousel-img">
            <img src="images/products/grounding_blanket/6.jpg" alt="Grounding Blanket Extra" class="gb-carousel-img">'''

if old_carousel_imgs in html:
    html = html.replace(old_carousel_imgs, new_carousel_imgs, 1)
    print('Added 6th image to grCarousel')
else:
    print('WARNING: old carousel images block not found')

# Update dot count to 6
old_dots = '''            <button class="gb-carousel-dot active" onclick="goGB('grCarousel',0)"></button>
            <button class="gb-carousel-dot" onclick="goGB('grCarousel',1)"></button>
            <button class="gb-carousel-dot" onclick="goGB('grCarousel',2)"></button>
            <button class="gb-carousel-dot" onclick="goGB('grCarousel',3)"></button>
            <button class="gb-carousel-dot" onclick="goGB('grCarousel',4)"></button>'''

new_dots = '''            <button class="gb-carousel-dot active" onclick="goGB('grCarousel',0)"></button>
            <button class="gb-carousel-dot" onclick="goGB('grCarousel',1)"></button>
            <button class="gb-carousel-dot" onclick="goGB('grCarousel',2)"></button>
            <button class="gb-carousel-dot" onclick="goGB('grCarousel',3)"></button>
            <button class="gb-carousel-dot" onclick="goGB('grCarousel',4)"></button>
            <button class="gb-carousel-dot" onclick="goGB('grCarousel',5)"></button>'''

if old_dots in html:
    html = html.replace(old_dots, new_dots, 1)
    print('Added 6th dot to grCarousel')
else:
    print('WARNING: old dots block not found')

# ── Fix Natural Grounding section class ────────────────────────────
# Change from wrong "gb-category-layout" to proper "gb-category-section"
old_ng_section = '''    <!-- Natural Grounding -->
    <section class="gb-category-layout" style="background:#fff;">
        <div class="container">
            <div class="gb-category-layout reverse">'''

new_ng_section = '''    <!-- Natural Grounding -->
    <section class="gb-category-section">
        <div class="container">
            <div class="gb-category-layout">'''

if old_ng_section in html:
    html = html.replace(old_ng_section, new_ng_section, 1)
    print('Fixed Natural Grounding section class: gb-category-section + removed reverse')
else:
    print('WARNING: Natural Grounding section class not found')
    pos = html.find('Natural Grounding')
    print(repr(html[pos-100:pos+200]))

# ── Inject carousel width constraint CSS ─────────────────────────
# Add constraint to gb-category-carousel so it doesn't stretch full width
old_carousel_wrap_css = ''
new_carousel_wrap_css = '''
        /* Constrain carousel containers to actual carousel size */
        .gb-category-carousel {
            flex: 0 0 auto;
            min-width: 0;
        }
'''

# Find where to inject - after the last .gb-carousel rule in the CSS
# Inject before the injected #grCarousel rule
gr_inject_pos = html.find('/* grCarousel: fixed 550x550 size */')
if gr_inject_pos > 0:
    html = html[:gr_inject_pos] + new_carousel_wrap_css + html[gr_inject_pos:]
    print('Injected .gb-category-carousel width constraint')
else:
    print('WARNING: grCarousel inject point not found')

with open(os.path.join(WD, 'grounding-blanket.html'), 'w', encoding='utf-8') as f:
    f.write(html)

# ── Verify ─────────────────────────────────────────────────────────
with open(os.path.join(WD, 'grounding-blanket.html'), encoding='utf-8') as f:
    chk = f.read()

checks = [
    ('Natural Grounding section class', 'class="gb-category-section"' in chk and 'gb-category-layout reverse' not in chk[chk.find('Natural Grounding')-100:chk.find('Natural Grounding')+200]),
    ('6 images in grCarousel', chk.count('grounding_blanket/') == 6),
    ('6 dots in grCarousel', chk.count("goGB('grCarousel'" ) == 6),
    ('Available Colors margin auto', 'margin:0 auto' in chk),
    ('#grCarousel 550px', '550px' in chk),
    ('.gb-category-carousel flex', 'gb-category-carousel' in chk and 'flex: 0 0 auto' in chk),
]
print('\n=== Verification ===')
for label, ok in checks:
    print(f'  {"OK" if ok else "FAIL"} {label}')

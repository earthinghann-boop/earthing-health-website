import subprocess, re

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'

# Read current deployed page + local
with open(WD + r'\grounding-mat.html', 'r', encoding='utf-8') as f:
    mat = f.read()

print("=== CURRENT grounding-mat.html DIAGNOSIS ===")
print(f"Size: {len(mat):,} chars")

# 1. Hero class
hero_cls = re.search(r'<section[^>]*class="([^"]*hero[^"]*)"', mat)
print(f"Hero class: {hero_cls.group(1) if hero_cls else 'NOT FOUND'}")

# 2. Hero image
hero_imgs = re.findall(r'<section[^>]*class="[^"]*hero[^"]*"[^>]*>.*?</section>',
    mat[:3000], re.DOTALL)
has_hero_img = bool(re.search(r'<img[^>]+class="product-hero-image"', mat[:2000]))
print('Hero image in hero section:', has_hero_img)

# 3. Carousel dots: count and onclick
dots = re.findall(r'onclick="goGB\([^"]+', mat)
print(f"Total dot onclick handlers: {len(dots)}")
for d in dots:
    print(f"  {d}")

# 4. Carousel structure check
carousel_divs = re.findall(r'<div class="gb-carousel" id="([^"]+)"', mat)
print(f"\nCarousel divs: {carousel_divs}")

# 5. Check carousel images in the HTML
carousel_imgs = re.findall(r'id="matCarousel"[^>]*>.*?</div>', mat, re.DOTALL)
print(f"matCarousel found: {len(carousel_imgs)}")

# 6. Check dot button tags
dot_btns = re.findall(r'<button class="gb-carousel-dot[^>]*>', mat)
print(f"\nDot buttons: {len(dot_btns)}")
for b in dot_btns[:5]:
    print(f"  {b}")

# 7. Available Colors section
ac_start = mat.find('Available Colors')
if ac_start > 0:
    sec_start = mat.rfind('<section', 0, ac_start)
    sec_end = mat.find('</section>', ac_start) + len('</section>')
    ac_section = mat[sec_start:sec_end]
    print(f"\n=== Available Colors section ({sec_end-sec_start} chars) ===")
    print(ac_section[:1500])

# 8. What comes after Available Colors
ac_end = mat.find('</section>', ac_start) + len('</section>')
next_h2 = mat.find('<h2', ac_end)
next_h2_text = re.sub(r'<[^>]+>', '', mat[next_h2:next_h2+200]).strip()[:80] if next_h2 > 0 else 'NOT FOUND'
print(f"\nNext section after Available Colors: h2={next_h2_text}")

# 9. Check groundingbedding collection-hero for reference
result = subprocess.run(['git', 'show', 'HEAD:groundingbedding.html'],
    capture_output=True, cwd=WD)
gb = result.stdout.decode('utf-8', errors='replace')
# Extract collection-hero
hero_m = re.search(r'(<section\b[^>]*class="[^"]*collection-hero[^"]*"[^>]*>.*?)(?=\n\s*<section)',
    gb, re.DOTALL)
if hero_m:
    print(f"\n=== Reference: groundingbedding collection-hero ({len(hero_m.group(1))} chars) ===")
    print(hero_m.group(1)[:1500])

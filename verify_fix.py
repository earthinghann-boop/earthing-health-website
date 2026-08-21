import re
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html', 'r', encoding='utf-8') as f:
    t = f.read()

print('=== Dots check ===')
for cid in ['puSheetCarousel','puDeskCarousel']:
    dots = re.findall(r'<span[^>]+onclick="goGB\(\'' + cid + r'\', (\d+)\)"', t)
    print(f'  {cid}: {dots}')

print()
print('=== CSS check ===')
print('aspect-ratio: 1 / 1' in t)
print('.gb-carousel-img' in t and 'inset: 0' in t)
print('object-fit: cover' in t)
print()
print('=== Section count ===')
print('<section class="gb-category-section">:', t.count('<section class="gb-category-section">'))
print('size:', len(t))
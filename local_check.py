import re
# Check local pu-earthing-mat.html
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html', encoding='utf-8') as f:
    t = f.read()
print('Local pu-earthing-mat.html size:', len(t))
for cid in ['puSheetCarousel','puDeskCarousel']:
    dots = re.findall(r'<span[^>]+onclick="goGB\(\'' + cid + r'\', (\d+)\)"', t)
    print(f'  {cid} dots: {dots}')
print('aspect-ratio: 1 / 1:', 'aspect-ratio: 1 / 1' in t)
print('inset: 0 in .gb-carousel-img:', 'inset: 0' in t)
print()
# Also check groundingbedding.html - does it have the same dot off-by-one?
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', encoding='utf-8') as f:
    gb = f.read()
print('groundingbedding.html size:', len(gb))
for cid in ['fittedCarousel','flatCarousel']:
    dots = re.findall(r'<span[^>]+onclick="goGB\(\'' + cid + r'\', (\d+)\)"', gb)
    print(f'  {cid} dots: {dots}')
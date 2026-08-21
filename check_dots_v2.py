import re
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html', encoding='utf-8') as f:
    t = f.read()
print('size:', len(t))
for cid in ['puSheetCarousel','puDeskCarousel']:
    idx = t.find('id="' + cid + '"')
    seg = t[idx:idx+2000]
    dots_idx = seg.find('gb-carousel-dots')
    if dots_idx >= 0:
        dots_area = seg[dots_idx:dots_idx+500]
        print(cid)
        print(repr(dots_area))
        print()
# Check CSS for left: 16px
print('transform translateY:', t.count('transform: translateY(-50%)'))
print('left: 16px:', t.count('left: 16px'))
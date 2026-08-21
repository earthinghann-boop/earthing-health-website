import re
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html', 'rb') as f:
    t = f.read().decode('utf-8')

cnt = len(re.findall(r'<section class="gb-category-section">', t))
print('Actual section blocks:', cnt)

cnt2 = len(re.findall(r'<img[^>]*gb-carousel-img[^>]*>', t))
print('Actual img tags with gb-carousel-img:', cnt2)

cnt3 = len(re.findall(r'<span[^>]*gb-carousel-dot[^>]*>', t))
print('Actual dot spans:', cnt3)
import os
p = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html'
size = os.path.getsize(p)
print('Size:', size, 'bytes')
with open(p, 'rb') as f:
    content = f.read()
text = content.decode('utf-8')
for c in ['DOCTYPE', 'fittedCarousel', 'flatCarousel', 'pillowCarousel', 'duvetCarousel', 'kidsCarousel', 'goGB', 'moveGB', 'gb-carousel-img active', '</html>']:
    status = 'OK' if c in text else 'MISSING'
    print(status, c)
for sid in ['fitted-sheet', 'flat-sheet', 'pillow-case', 'duvet-cover', 'kids-bedding']:
    tag = 'id="' + sid + '"'
    status = 'OK' if tag in text else 'MISSING'
    print(status, tag)
for cat in ['fitted_sheet', 'flat_sheet', 'pillow_case', 'duvet_cover', 'kids_bedding']:
    for i in range(1, 5):
        path = 'images/products/' + cat + '/' + str(i) + '.jpg'
        status = 'OK' if path in text else 'MISSING'
        print(status, path)

import re

with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', 'rb') as f:
    text = f.read().decode('utf-8')

print('=== Grounding Bedding local file ===')
print('File size:', len(text))
print()

print('=== Carousel sections (5 expected) ===')
for cid in ['fittedCarousel','flatCarousel','pillowCarousel','duvetCarousel','kidsCarousel']:
    cnt = text.count('id="' + cid + '"')
    print('  [', 'OK' if cnt==1 else 'MISS', ']', cnt, 'x id="' + cid + '"')

print()
print('=== Arrow buttons ===')
print('Prev arrow classes:', text.count('gb-carousel-prev'))
print('Next arrow classes:', text.count('gb-carousel-next'))

print()
print('=== Dot positioning (left side) ===')
m = re.search(r'\.gb-carousel-dots\s*\{([^}]+)\}', text)
if m:
    print(m.group())

print()
print('=== Dot click exposure ===')
m2 = re.search(r'window\.goGB\s*=\s*goGB', text)
print('Found:', m2 is not None)

print()
print('=== Image paths for 5 carousels ===')
for cat in ['fitted_sheet','flat_sheet','pillow_case','duvet_cover','kids_bedding']:
    ok = 0
    for i in [1,2,3,4]:
        if 'images/products/' + cat + '/' + str(i) + '.jpg' in text:
            ok += 1
    print('  [', 'OK' if ok==4 else 'MISS', ']', cat, '-', ok, '/4 images')

print()
print('=== onclick on dots (4 dots per carousel x 5 = 20) ===')
print('onclick="goGB count:', text.count('onclick="goGB'))
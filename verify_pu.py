with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html', 'rb') as f:
    t = f.read().decode('utf-8')

print('=== File size:', len(t))
print()
print('=== Carousels ===')
for cid in ['puSheetCarousel','puDeskCarousel','puYogaCarousel']:
    print('  [', 'OK' if t.count('id="'+cid+'"')==1 else 'MISS', ']', cid, t.count('id="'+cid+'"'))

print()
print('=== Section count ===')
print('gb-category-section:', t.count('gb-category-section'))
print('gb-carousel-img:', t.count('gb-carousel-img'))
print('gb-carousel-dot:', t.count('gb-carousel-dot'))

print()
print('=== Image paths ===')
for cat in ['pu_sheet','pu_desk_mat','pu_yoga_mat']:
    ok = sum(1 for i in [1,2,3,4] if f'images/products/{cat}/{i}.jpg' in t)
    print('  [', 'OK' if ok==4 else 'MISS', ']', cat, ok, '/4')

print()
print('=== JS / onclick ===')
print('window.goGB = goGB:', t.count('window.goGB = goGB'))
print('onclick=goGB count:', t.count('onclick="goGB'))
print('CAROUSELS list:', "['puSheetCarousel','puDeskCarousel','puYogaCarousel']" in t)

print()
print('=== Nav/footer ===')
print('class="navbar":', t.count('class="navbar"'))
print('class="logo":', t.count('class="logo"'))
print('class="nav-links":', t.count('class="nav-links"'))
print('js/main.js:', t.count('js/main.js'))
print('footer-col:', t.count('footer-col'))
print('images/logo/earthing-logo.png:', t.count('images/logo/earthing-logo.png'))
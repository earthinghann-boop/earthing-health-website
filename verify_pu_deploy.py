import urllib.request

url = 'https://www.silveryes.com/pu-earthing-mat.html'
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache'})
with urllib.request.urlopen(req, timeout=15) as r:
    t = r.read().decode('utf-8')

print('Vercel size:', len(t))
print('gb-category-section:', t.count('gb-category-section'))
print('CAROUSELS list:', "['puSheetCarousel','puDeskCarousel','puYogaCarousel']" in t)
print('window.goGB = goGB:', t.count('window.goGB = goGB'))
print('images/products/pu_sheet/1.jpg:', t.count('images/products/pu_sheet/1.jpg'))
print('images/products/pu_desk_mat/1.jpg:', t.count('images/products/pu_desk_mat/1.jpg'))
print('images/products/pu_yoga_mat/1.jpg:', t.count('images/products/pu_yoga_mat/1.jpg'))
print('navbar:', t.count('class="navbar"'))
print('main.js:', t.count('js/main.js'))

# Check images
for cat in ['pu_sheet','pu_desk_mat','pu_yoga_mat']:
    for i in [1,2,3,4]:
        u = f'https://www.silveryes.com/images/products/{cat}/{i}.jpg'
        try:
            rq = urllib.request.Request(u, method='HEAD', headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(rq, timeout=5) as rr:
                print('  [OK]', rr.status, rr.headers.get('Content-Length', '?'), 'bytes', u)
        except Exception as e:
            print('  [ERR]', e, u)
import urllib.request, urllib.error
url = 'https://www.silveryes.com/pu-earthing-mat.html?nocache=999'
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache','Pragma':'no-cache'})
try:
    with urllib.request.urlopen(req, timeout=15) as r:
        t = r.read().decode('utf-8')
    print('Vercel with no-cache size:', len(t))
    print('gb-category-section:', t.count('gb-category-section'))
    needles = ["['puSheetCarousel','puDeskCarousel','puYogaCarousel']", 'window.goGB = goGB', 'puSheetCarousel', 'images/products/pu_sheet/1.jpg']
    for n in needles:
        print('  ', repr(n)[:60], '->', t.count(n))
except urllib.error.HTTPError as e:
    print('HTTP Error:', e.code)
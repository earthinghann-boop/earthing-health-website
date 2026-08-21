import urllib.request, re
url = 'https://www.silveryes.com/pu-earthing-mat.html?nocache=777'
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache'})
with urllib.request.urlopen(req, timeout=15) as r:
    html = r.read().decode('utf-8')

print('Vercel size:', len(html))
print()
print('=== Dot onclick values ===')
for cid in ['puSheetCarousel','puDeskCarousel']:
    dots = re.findall(r'<span[^>]+onclick="goGB\(\'' + cid + r'\', (\d+)\)"', html)
    print(f'  {cid}: {dots}')

print()
print('=== CSS fixes ===')
print('aspect-ratio: 1 / 1:', 'aspect-ratio: 1 / 1' in html)
print('object-fit: cover:', 'object-fit: cover' in html)
print()
print('=== puSheetCarousel actual imgs (substring isolation) ===')
idx = html.find('id="puSheetCarousel"')
end = html.find('id="puDeskCarousel"')
segment = html[idx:end]
imgs = re.findall(r'images/products/pu_sheet/\d\.jpg', segment)
print('  pu_sheet imgs:', imgs)
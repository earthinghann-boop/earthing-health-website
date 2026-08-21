import urllib.request, re, time

# Get groundingbedding.html dots (reference - this works correctly)
url = f'https://www.silveryes.com/groundingbedding.html?nocache={int(time.time()*1000)}'
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache'})
with urllib.request.urlopen(req, timeout=15) as r:
    html = r.read().decode('utf-8')

idx = html.find('id="fittedCarousel"')
end = html.find('id="flatCarousel"')
seg = html[idx:end]
print('groundingbedding fittedCarousel dots area:')
print(repr(seg[seg.find('gb-carousel-dots'):seg.find('gb-carousel-dots')+600]))
print()

# Now check pu-earthing-mat.html
url2 = f'https://www.silveryes.com/pu-earthing-mat.html?nocache={int(time.time()*1000)}'
req2 = urllib.request.Request(url2, headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache'})
with urllib.request.urlopen(req2, timeout=15) as r:
    html2 = r.read().decode('utf-8')

idx2 = html2.find('id="puSheetCarousel"')
end2 = html2.find('id="puDeskCarousel"')
seg2 = html2[idx2:end2]
print('pu-earthing-mat puSheetCarousel dots area:')
print(repr(seg2[seg2.find('gb-carousel-dots'):seg2.find('gb-carousel-dots')+600]))
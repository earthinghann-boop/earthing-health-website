import urllib.request
url = 'https://www.silveryes.com/pu-earthing-mat.html?nocache=888'
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache'})
with urllib.request.urlopen(req, timeout=15) as r:
    t = r.read().decode('utf-8')
print('Vercel HTML size:', len(t))
print('gb-category-section:', t.count('<section class="gb-category-section">'))
print('Two Product Forms:', 'Two Product Forms' in t)
print('Three Product Forms:', 'Three Product Forms' in t)
print('PU Yoga Mat present:', 'PU Yoga Mat' in t)
print()
for cat in ['pu_sheet','pu_desk_mat']:
    for i in [1,2,3,4]:
        u = f'https://www.silveryes.com/images/products/{cat}/{i}.jpg?nocache=888'
        rq = urllib.request.Request(u, method='HEAD', headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache'})
        try:
            with urllib.request.urlopen(rq, timeout=5) as rr:
                print('  [OK]', rr.headers.get('Content-Length'), 'bytes', cat+'/'+str(i)+'.jpg')
        except Exception as e:
            print('  [ERR]', e, cat+'/'+str(i)+'.jpg')
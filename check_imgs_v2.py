import urllib.request
cats = ['fitted_sheet','flat_sheet','pillow_case','duvet_cover','kids_bedding']
ok = miss = 0
for cat in cats:
    for i in [1,2,3,4]:
        url = 'https://www.silveryes.com/images/products/' + cat + '/' + str(i) + '.jpg'
        try:
            req = urllib.request.Request(url, method='HEAD', headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as r:
                code = r.status
                size = r.headers.get('Content-Length', 'unknown')
                print('  [OK]', code, size, 'bytes', url)
                ok += 1
        except Exception as e:
            print('  [MISS]', e, url)
            miss += 1
print()
print('Total: OK=', ok, ' MISS=', miss)
import urllib.request
for cat in ['pu_sheet','pu_desk_mat','pu_yoga_mat']:
    for i in [1,2,3,4]:
        u = f'https://www.silveryes.com/images/products/{cat}/{i}.jpg?v=999'
        try:
            rq = urllib.request.Request(u, method='HEAD', headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache'})
            with urllib.request.urlopen(rq, timeout=5) as rr:
                print('  [OK]', rr.status, rr.headers.get('Content-Length', '?'), 'bytes', u)
        except Exception as e:
            print('  [ERR]', e, u)
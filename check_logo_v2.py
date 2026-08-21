import urllib.request
urls = [
    'https://www.silveryes.com/images/logo.svg',
    'https://www.silveryes.com/images/logo/earthing-logo.png'
]
for url in urls:
    try:
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            print(r.status, r.headers.get('Content-Length', '?'), 'bytes', url)
    except Exception as e:
        print('ERROR', e, url)
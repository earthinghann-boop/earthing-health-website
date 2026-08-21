import urllib.request
url = 'https://www.silveryes.com/images/logo/earthing-logo.png'
try:
    req = urllib.request.Request(url, method='HEAD', headers={'User-Agent':'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as r:
        print(r.status, r.headers.get('Content-Length', '?'), 'bytes')
except Exception as e:
    print('ERROR', e)
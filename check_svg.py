import os, urllib.request

local = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\images\logo.svg'
if os.path.exists(local):
    print('Local logo.svg:', os.path.getsize(local), 'bytes')
else:
    print('Local logo.svg MISSING')

print()
req = urllib.request.Request('https://www.silveryes.com/images/logo.svg', method='HEAD', headers={'User-Agent':'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        print('Vercel /images/logo.svg:', r.status, 'size', r.headers.get('Content-Length'))
except Exception as e:
    print('Vercel /images/logo.svg error:', e)

req = urllib.request.Request('https://www.silveryes.com/logo.svg', method='HEAD', headers={'User-Agent':'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        print('Vercel /logo.svg:', r.status, 'size', r.headers.get('Content-Length'))
except Exception as e:
    print('Vercel /logo.svg error:', e)
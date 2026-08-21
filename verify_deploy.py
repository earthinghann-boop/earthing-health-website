import urllib.request
req = urllib.request.Request('https://www.silveryes.com/groundingbedding.html', headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache'})
with urllib.request.urlopen(req, timeout=15) as r:
    text = r.read().decode('utf-8')
print('Vercel size:', len(text))
print('navbar:', text.count('class="navbar"'))
print('logo img:', text.count('class="logo"'))
print('nav-links:', text.count('nav-links'))
print('mobile-menu-btn:', text.count('mobile-menu-btn'))
print('footer-col:', text.count('footer-col'))
print('footer-logo:', text.count('footer-logo'))
print('js/main.js:', text.count('js/main.js'))
print('class="nav-logo":', text.count('class="nav-logo"'))
print('height="36":', text.count('height="36"'))
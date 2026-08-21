import urllib.request, re, time

url = 'https://www.silveryes.com/pu-earthing-mat.html?nocache=' + str(int(time.time()*1000))
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache'})
with urllib.request.urlopen(req, timeout=15) as r:
    html = r.read().decode('utf-8')

print('Vercel size:', len(html))
print()
print('class="navbar":', 'class="navbar"' in html)
print('class="logo":', 'class="logo"' in html)
print('images/logo/earthing-logo.png:', 'images/logo/earthing-logo.png' in html)
print('js/main.js:', 'js/main.js' in html)
print('<footer class="footer":', '<footer class="footer"' in html)
print()
# Print nav block first 400 chars
m = re.search(r'<nav[^>]*>.*?</nav>', html, re.DOTALL)
if m:
    nav = m.group()
    print(f'Nav block: {len(nav)} chars')
    # Count li items (Products menu)
    lis = re.findall(r'<li[^>]*>', nav)
    print(f'Nav <li> items: {len(lis)}')
else:
    print('NO NAV!')
import urllib.request, re, time

# Pull from groundingbedding.html (live, confirmed nav works)
url = 'https://www.silveryes.com/groundingbedding.html?nocache=' + str(int(time.time()*1000))
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache'})
with urllib.request.urlopen(req, timeout=15) as r:
    html = r.read().decode('utf-8')

# Find <nav ...>...</nav>
m = re.search(r'<nav[^>]*>.*?</nav>', html, re.DOTALL)
if m:
    nav = m.group()
    print(f'groundingbedding nav: {len(nav)} chars')
    # Save to file for inspection
    with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\nav_gb.txt', 'w', encoding='utf-8') as f:
        f.write(nav)
    print('Saved to nav_gb.txt')
    # Show first 300 chars
    print(repr(nav[:400]))
else:
    print('No nav found!')

# Same for footer
m2 = re.search(r'<footer[^>]*>.*?</footer>', html, re.DOTALL)
if m2:
    footer = m2.group()
    with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\footer_gb.txt', 'w', encoding='utf-8') as f:
        f.write(footer)
    print(f'\ngroundingbedding footer: {len(footer)} chars')
else:
    print('No footer found!')
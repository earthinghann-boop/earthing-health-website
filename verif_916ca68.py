import urllib.request, re, time

url = 'https://www.silveryes.com/pu-earthing-mat.html?nocache=' + str(int(time.time()*1000))
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache'})
with urllib.request.urlopen(req, timeout=15) as r:
    html = r.read().decode('utf-8')

print('Vercel size:', len(html), '(expect ~17024)')
print()

# Check for stray > in dots
dot_spans = re.findall(r'<button class="gb-carousel-dot[^"]*" onclick="goGB[^"]+"[^>]*></button>', html)
print(f'Dot spans (clean): {len(dot_spans)} (expect 8)')
bad = [d for d in dot_spans if '>' in d and '</button>' not in d.split('>')[1]]
print(f'Bad dot spans: {len(bad)}')

# Show first dot
if dot_spans:
    print('First dot:', repr(dot_spans[0]))
    print('Last dot:', repr(dot_spans[-1]))

# CSS check
print()
print('CSS:')
m = re.search(r'\.gb-carousel-dots \{(.*?)\}', html, re.DOTALL)
if m:
    print(re.sub(r'\s+', ' ', m.group(1)).strip()[:300])

print()
print('CAROUSELS JS:')
m2 = re.search(r'var CAROUSELS = (\[[^\]]+\])', html)
if m2:
    print(m2.group(1))
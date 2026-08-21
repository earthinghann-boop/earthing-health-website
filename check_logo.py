import urllib.request, re
req = urllib.request.Request('https://www.silveryes.com/groundingbedding.html', headers={'User-Agent':'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as r:
    text = r.read().decode('utf-8')

print('=== Find logo context ===')
for m in re.finditer(r'nav-logo', text):
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 300)
    print('--- nav-logo match ---')
    print(text[start:end])
    print()

print('=== Find logo.svg ===')
for m in re.finditer(r'logo\.svg', text):
    start = max(0, m.start() - 200)
    end = min(len(text), m.end() + 50)
    print('--- logo.svg match ---')
    print(text[start:end])
    print()
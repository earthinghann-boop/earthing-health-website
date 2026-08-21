import urllib.request, re

# Check Vercel live
req = urllib.request.Request('https://www.silveryes.com/', headers={'User-Agent':'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as r:
    text = r.read().decode('utf-8')

# Find all href containing the old fitted-sheet URL, fitted, bedding
print('=== All hrefs in nav-dropdown-menu ===')
m = re.search(r'<ul class="nav-dropdown-menu">(.*?)</ul>', text, re.DOTALL)
if m:
    ul = m.group(1)
    for hm in re.finditer(r'<a href="([^"]+)">([^<]+)</a>', ul):
        print('  href=', hm.group(1), '| text=', hm.group(2))

print()
print('=== Grounding Bedding product-category area ===')
m = re.search(r'id="grounding-bedding"(.*?)(?=product-category|footer)', text, re.DOTALL)
if m:
    area = m.group(1)
    for hm in re.finditer(r'href="([^"]+)"', area):
        href = hm.group(1)
        if not href.startswith('#') and 'javascript' not in href:
            print('  ', href)
print()
print('=== Total counts ===')
print('earthing-fitted-sheet.html:', len(re.findall(r'earthing-fitted-sheet', text)))
print('groundingbedding.html:', len(re.findall(r'groundingbedding', text)))
print('fitted-sheet in text:', len(re.findall(r'fitted-sheet', text)))
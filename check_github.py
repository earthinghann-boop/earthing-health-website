import urllib.request, re
req = urllib.request.Request('https://raw.githubusercontent.com/earthinghann-boop/earthing-health-website/master/index.html')
with urllib.request.urlopen(req, timeout=15) as r:
    text = r.read().decode('utf-8')
print('github raw size:', len(text))
print('earthing-fitted-sheet count:', len(re.findall(r'earthing-fitted-sheet', text)))
print('groundingbedding count:', len(re.findall(r'groundingbedding', text)))
print()
# Show all href refs containing fitted/grounding/bedding
for m in re.finditer(r'href="[^"]*"', text):
    href = m.group()
    lower = href.lower()
    if 'fitted' in lower or 'bedding' in lower or 'grounding' in lower:
        print('  ', href)
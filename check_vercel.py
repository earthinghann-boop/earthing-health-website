import urllib.request, re
req = urllib.request.Request('https://www.silveryes.com/', headers={'User-Agent':'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as r:
    text = r.read().decode('utf-8')
print('vercel size:', len(text))
print('earthing-fitted-sheet count:', len(re.findall(r'earthing-fitted-sheet', text)))
print('groundingbedding count:', len(re.findall(r'groundingbedding', text)))
print()
# Find the Grounding Bedding menu context
for m in re.finditer(r'Grounding Bedding', text):
    start = max(0, m.start()-150)
    end = min(len(text), m.end()+50)
    print('--- pos=', m.start(), '---')
    print(text[start:end])
    print()
import re
p = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html'
with open(p, 'rb') as f:
    text = f.read().decode('utf-8')

print('=== File size:', len(text))
print()

# Find current section structure
print('=== Major sections (h1/h2 with class) ===')
for m in re.finditer(r'<h1[^>]*>(.*?)</h1>|<h2[^>]*>(.*?)</h2>', text):
    s = m.group(1) or m.group(2)
    print('  ', s[:80])
print()

# Find img tags
print('=== Image tags ===')
for m in re.finditer(r'<img[^>]*src="([^"]*\.jpg)"[^>]*>', text):
    print('  ', m.group(1))
print()

# Find PU product mentions
print('=== References to PU product types ===')
for kw in ['PU Sheet', 'PU Desk', 'PU Yoga', 'sheet', 'desk mat', 'yoga mat', 'yoga', 'desk']:
    print('  ', kw, '->', len(re.findall(kw, text, re.IGNORECASE)))
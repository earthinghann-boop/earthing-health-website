import re
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\css\style.css', 'rb') as f:
    css = f.read().decode('utf-8')

# Find rules with nav-container or nav-brand
for kw in ['nav-container', 'nav-brand', 'brand', 'logo']:
    print(f'=== {kw} ===')
    for m in re.finditer(rf'[^{{]*\b{kw}\b[^{{]*\{{[^}}]+\}}', css):
        s = m.group()
        if 'height' in s or 'width' in s or 'max-' in s or 'size' in s:
            print(s[:300])
            print('---')
    print()
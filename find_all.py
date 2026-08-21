import re, os

base = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
old_url = 'earthing-fitted-sheet.html'
old_id = '#gb-bedding'  # anchor if used

print('=== All remaining earthing-fitted-sheet.html refs ===')
for f in os.listdir(base):
    if not f.endswith('.html'):
        continue
    p = os.path.join(base, f)
    with open(p, 'rb') as fp:
        text = fp.read().decode('utf-8')
    for m in re.finditer(re.escape(old_url), text):
        start = max(0, m.start() - 80)
        end = min(len(text), m.end() + 50)
        print(f'[{f} pos={m.start()}] ...{text[start:end]}...')
        print()

print('=== Now also find groundingbedding.html (the new) ===')
for f in os.listdir(base):
    if not f.endswith('.html'):
        continue
    p = os.path.join(base, f)
    with open(p, 'rb') as fp:
        text = fp.read().decode('utf-8')
    for m in re.finditer(r'groundingbedding\.html', text):
        start = max(0, m.start() - 80)
        end = min(len(text), m.end() + 30)
        print(f'[{f} pos={m.start()}] ...{text[start:end]}...')
        print()
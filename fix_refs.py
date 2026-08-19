import os, re

base = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
old = 'earthing-fitted-sheet.html'
new = 'groundingbedding.html'

files_changed = []
total_refs = 0

for fname in os.listdir(base):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(base, fname)
    with open(fpath, 'rb') as f:
        content = f.read()
    text = content.decode('utf-8')
    # Only replace href values, not attribute names
    new_text = re.sub(r'href="' + re.escape(old) + r'"', 'href="' + new + '"', text)
    if new_text != text:
        count = len(re.findall(r'href="' + re.escape(new) + r'"', new_text))
        files_changed.append((fname, count))
        total_refs += count
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_text)

print('Files updated:', len(files_changed))
print('Total refs changed:', total_refs)
for fname, count in files_changed:
    print(' ', fname, '->', count, 'refs')

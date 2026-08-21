import re, os

# For each HTML, find nav structure and logo size attribute
for f in os.listdir(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'):
    if not f.endswith('.html'):
        continue
    p = os.path.join(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website', f)
    with open(p, 'rb') as fp:
        t = fp.read().decode('utf-8')

    nav_tag = re.search(r'<nav[^>]*>', t)
    logo_img = re.search(r'<img[^>]*earthing-logo[^>]*>', t)

    print(f)
    print(' nav:', nav_tag.group() if nav_tag else 'NONE')
    print(' logo:', logo_img.group() if logo_img else 'NONE')
    print()
import re

# Find which page uses the OLD nav structure (nav-logo / nav-menu)
import os
for f in sorted(os.listdir(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website')):
    if not f.endswith('.html'):
        continue
    p = os.path.join(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website', f)
    with open(p, 'rb') as fp:
        t = fp.read().decode('utf-8')
    if 'class="nav-logo"' in t:
        print('OLD nav-logo found in:', f)
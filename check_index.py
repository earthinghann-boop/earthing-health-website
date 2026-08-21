import re

# Check index.html for inline style or nav structure
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\index.html', 'rb') as f:
    idx = f.read().decode('utf-8')

print('=== index.html nav tag ===')
m = re.search(r'<nav[^>]*>', idx)
if m:
    print(m.group())
print()
m = re.search(r'<img[^>]*earthing-logo[^>]*>', idx)
if m:
    print('index logo img:', m.group())

print()
print('=== Index has inline <style> with nav-logo? ===')
for m in re.finditer(r'<style[^>]*>(.*?)</style>', idx, re.DOTALL):
    s = m.group(1)
    if 'nav-logo' in s or 'nav-menu' in s:
        print('FOUND inline nav CSS, length=', len(s))
        for ln in s.split('\n'):
            if 'nav-logo' in ln or 'nav-menu' in ln or '.nav' in ln[:30]:
                print('  ', ln[:120])

# search for navbar
print()
print('index.html navbar count:', idx.count('class="navbar"'))
print('index.html nav-menu count:', idx.count('nav-menu'))
print('index.html nav-logo count:', idx.count('nav-logo'))
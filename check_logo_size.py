import re
# Find nav-logo CSS in style.css
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\css\style.css', 'rb') as f:
    css = f.read().decode('utf-8')

# Find nav-related rules
print('=== nav-logo CSS ===')
m = re.search(r'\.nav-logo[^{]*\{[^}]+\}', css)
if m:
    print(m.group())
print()
m = re.search(r'\.nav-menu[^{]*\{[^}]+\}', css)
if m:
    print(m.group())
print()
m = re.search(r'\.nav[^{]*\{[^}]+\}', css)
if m:
    print(m.group())
print()
# What does index.html use for nav-logo size?
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\index.html', 'rb') as f:
    idx = f.read().decode('utf-8')
m = re.search(r'<a[^>]*nav-logo[^>]*>(.*?)</a>', idx, re.DOTALL)
if m:
    print('index.html nav-logo content:')
    print(m.group(0)[:500])
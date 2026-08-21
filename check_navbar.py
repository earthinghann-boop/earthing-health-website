import re
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\css\style.css', 'rb') as f:
    css = f.read().decode('utf-8')

print('=== .navbar rules ===')
for m in re.finditer(r'\.navbar\b[^{]*\{[^}]+\}', css):
    print(m.group()[:200])
    print('---')

print()
print('=== .nav-menu, .nav-dropdown, .nav-logo in any form ===')
for pat in ['nav-menu', 'nav-logo', 'nav-container', 'nav-dropdown', 'nav-link']:
    print('  ', pat, ':', css.count(pat))

print()
# Check if groundingbedding.html uses class="nav" or class="navbar"
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', 'rb') as f:
    g = f.read().decode('utf-8')
print('=== groundingbedding.html nav tag ===')
for m in re.finditer(r'<nav[^>]*>', g):
    print(m.group())

print()
print('=== groundingbedding.html nav-logo usage ===')
for m in re.finditer(r'class="[^"]*logo[^"]*"', g):
    print(m.group())

print()
print('=== groundingbedding.html nav-menu usage ===')
for m in re.finditer(r'class="[^"]*menu[^"]*"', g):
    print(m.group())
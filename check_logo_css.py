import re
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\css\style.css', 'rb') as f:
    css = f.read().decode('utf-8')

# Find rules that reference logo image
print('=== Rules with navbar img / brand ===')
for m in re.finditer(r'(\.navbar[^,{]*img[^{]*|\.navbar[^,{]*brand[^{]*)\s*\{[^}]+\}', css):
    print(m.group()[:300])
    print('---')

print()
print('=== Rules with .navbar (all) ===')
for m in re.finditer(r'\.navbar[^{,]*[^{]*\{[^}]+\}', css):
    s = m.group()
    if len(s) < 400:
        print(s)
        print('---')
import re
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html', encoding='utf-8') as f:
    t = f.read()

# CSS checks
print('=== CSS checks ===')
print('left: 16px:', t.count('left: 16px'), '(should be 0 — already set left:0 in rebuild)')
print('left: 0;:', t.count('left: 0;'), '(should include dots rule)')
print('transform translateY:', t.count('transform: translateY(-50%)'))
print('justify-content: center:', t.count('justify-content: center'))

# Extract .gb-carousel-dots rule
m = re.search(r'\.gb-carousel-dots \{([^}]+)\}', t, re.DOTALL)
if m:
    print()
    print('.gb-carousel-dots rule:')
    print(re.sub(r'\s+', ' ', m.group(1)).strip())

print()
print('=== Dot spans (no stray > text) ===')
dots = re.findall(r'<button class="gb-carousel-dot[^"]*" onclick="goGB\([^)]+\)"></button>', t)
print(f'Clean dot spans: {len(dots)} (expect 8)')
for d in dots:
    print(' ', d)

print()
print('File size:', len(t))
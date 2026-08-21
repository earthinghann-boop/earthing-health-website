import os

p = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html'
with open(p, 'rb') as f:
    text = f.read().decode('utf-8')

old = 'images/logo.svg'
new = 'images/logo/earthing-logo.png'

cnt = text.count(old)
text = text.replace(old, new)

with open(p, 'w', encoding='utf-8') as f:
    f.write(text)

print('Replacements:', cnt)
print('Remaining old refs:', text.count(old))
print('New refs:', text.count(new))
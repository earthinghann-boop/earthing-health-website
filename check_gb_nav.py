import re

p = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html'
with open(p, 'rb') as fp:
    t = fp.read().decode('utf-8')

m = re.search(r'<nav[^>]*>.*?</nav>', t, re.DOTALL)
if m:
    print('=== current groundingbedding.html nav ===')
    print(m.group())
    print()
    print('--- LENGTH:', len(m.group()))

# Also get the footer to check
m2 = re.search(r'<footer[^>]*>.*?</footer>', t, re.DOTALL)
if m2:
    print('=== current groundingbedding.html footer ===')
    print(m2.group())
    print()
    print('--- LENGTH:', len(m2.group()))
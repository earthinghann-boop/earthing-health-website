import re
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\emf-wearing.html', 'rb') as f:
    emf = f.read().decode('utf-8')

# Find scripts at bottom
print('=== scripts in emf-wearing.html ===')
for m in re.finditer(r'<script[^>]*>.*?</script>', emf, re.DOTALL):
    s = m.group()[:120].replace('\n', ' ')
    print(s)
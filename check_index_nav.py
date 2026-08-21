import re
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\index.html', 'rb') as f:
    idx = f.read().decode('utf-8')

# Find nav block
m = re.search(r'<nav[^>]*>(.*?)</nav>', idx, re.DOTALL)
if m:
    print('=== index.html nav block ===')
    print(m.group()[:2000])
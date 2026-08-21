import re
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\emf-wearing.html', 'rb') as f:
    emf = f.read().decode('utf-8')

m = re.search(r'<footer[^>]*>.*?</footer>', emf, re.DOTALL)
if m:
    print('=== emf-wearing.html footer ===')
    print(m.group())
HTML = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\emf-wearing.html'
with open(HTML, encoding='utf-8') as f:
    html = f.read()
import re
# Find positions of every EMF occurrence
for m in re.finditer(r'EMF', html):
    s = max(0, m.start() - 40)
    e = min(len(html), m.end() + 40)
    print(f'@{m.start()}: ...{html[s:e]}...')
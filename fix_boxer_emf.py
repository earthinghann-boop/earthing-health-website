HTML = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\emf-wearing.html'
with open(HTML, encoding='utf-8') as f:
    html = f.read()
html = html.replace(
    'antibacterial protection meets EMF shielding',
    'antibacterial protection meets RF blocking'
)
with open(HTML, 'w', encoding='utf-8') as f:
    f.write(html)
print('EMF count after fix:', html.count('EMF'))
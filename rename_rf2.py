"""Final cleanup: alt tags + any remaining EMF"""
HTML = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\emf-wearing.html'

with open(HTML, encoding='utf-8') as f:
    html = f.read()

# alt attributes
html = html.replace('alt="EMF Shawl"', 'alt="RF Blocking Shawl"')
html = html.replace('alt="Fishman Cap"', 'alt="RF Blocking Fishman Cap"')
html = html.replace('alt="Beanie"', 'alt="RF Blocking Beanie"')
html = html.replace('alt="Hood"', 'alt="RF Blocking Hood"')
html = html.replace('alt="Baseball Cap"', 'alt="RF Blocking Baseball Cap"')
html = html.replace('alt="Curtain"', 'alt="RF Blocking Curtain"')
html = html.replace('alt="Socks"', 'alt="Grounding Socks"')
html = html.replace('alt="Eye Mask"', 'alt="RF Blocking Eye Mask"')
html = html.replace('alt="Sleeve Shirt"', 'alt="RF Shielding Shirt"')
html = html.replace('alt="Loungewear"', 'alt="RF Shielding Loungewear"')
html = html.replace('alt="Boxer Shorts"', 'alt="RF Shielding Boxer Shorts"')

with open(HTML, 'w', encoding='utf-8') as f:
    f.write(html)

# Verify
print('Final EMF count:', html.count('EMF'))
print('RF Blocking count:', html.count('RF Blocking'))
print('RF Shielding count:', html.count('RF Shielding'))

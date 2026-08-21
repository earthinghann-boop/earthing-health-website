"""Read current emf-wearing.html to extract nav/footer/style/JS"""
import os

HTML = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\emf-wearing.html'
with open(HTML, encoding='utf-8') as f:
    html = f.read()

# Find nav
nav_start = html.find('<nav class="navbar"')
pos = nav_start; depth = 0
while pos < len(html):
    n_o = html.find('<nav', pos); n_c = html.find('</nav>', pos)
    if n_c < 0: break
    if 0 <= n_o < n_c: depth += 1; pos = n_o + 4
    else: depth -= 1; pos = n_c + 6
    if depth == 0: nav_end = pos; break
nav = html[nav_start:nav_end]
print(f'nav: {len(nav)} chars')

# Footer
footer_start = html.find('<footer')
footer_end = html.find('</footer>') + len('</footer>')
footer = html[footer_start:footer_end]
print(f'footer: {len(footer)} chars')

# Save to temp files for reuse
os.makedirs(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\temp', exist_ok=True)
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\temp\wearing_nav.html', 'w', encoding='utf-8') as f:
    f.write(nav)
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\temp\wearing_footer.html', 'w', encoding='utf-8') as f:
    f.write(footer)
print('Saved')

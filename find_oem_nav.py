import sys; sys.stdout.reconfigure(encoding='utf-8')
html = open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\index.html','r',encoding='utf-8').read()
idx = html.find('nav-links')
print(repr(html[idx:idx+600]))

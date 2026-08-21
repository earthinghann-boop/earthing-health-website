with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-mat.html', encoding='utf-8') as f:
    html = f.read()

pos = html.find('function goGB')
print(f'goGB at: {pos}')
print(html[pos:pos+800])

with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html', encoding='utf-8') as f:
    t = f.read()
idx = t.find('top: 50%')
snippet = t[idx:idx+300]
print('newlines between 50% and transform:', snippet.count('\n'))
print(repr(snippet[:200]))
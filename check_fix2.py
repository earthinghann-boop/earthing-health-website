import re
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html', encoding='utf-8') as f:
    t = f.read()

idx = t.find('.gb-carousel-dots')
snippet = t[idx:idx+400]
print('dots CSS:')
print(repr(snippet[:300]))
print()
# Check dots HTML
idx2 = t.find('gb-carousel-dots')
end2 = t.find('</div>', idx2)
seg = t[idx2:end2]
print('dots HTML:')
print(repr(seg[:300]))
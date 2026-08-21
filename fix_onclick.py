import re
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html', encoding='utf-8') as f:
    t = f.read()

# Find all goGB onclick values
onclicks = re.findall(r'onclick="goGB\([^)]+\)"', t)
for o in onclicks:
    print(o)

print()
print('Total goGB calls:', len(onclicks))
print('{cat_id} still present:', "'{cat_id}'" in t)
import re
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html', encoding='utf-8') as f:
    t = f.read()

# Replace {cat_id} in dots HTML with actual IDs
t = t.replace("goGB('{cat_id}',0)", "goGB('puSheetCarousel',0)")
t = t.replace("goGB('{cat_id}',1)", "goGB('puSheetCarousel',1)")
t = t.replace("goGB('{cat_id}',2)", "goGB('puSheetCarousel',2)")
t = t.replace("goGB('{cat_id}',3)", "goGB('puSheetCarousel',3)")
t = t.replace("goGB('{cat_id}',0)", "goGB('puDeskCarousel',0)")  # this fires second
t = t.replace("goGB('{cat_id}',1)", "goGB('puDeskCarousel',1)")
t = t.replace("goGB('{cat_id}',2)", "goGB('puDeskCarousel',2)")
t = t.replace("goGB('{cat_id}',3)", "goGB('puDeskCarousel',3)")

# Fix the last stray goGB(...)
# Find context around it
idx = t.find("goGB(...)")
print('goGB(...) context:')
print(repr(t[idx-50:idx+50]))
# Replace it with the correct last item
t = t.replace("goGB(...)", "goGB('puDeskCarousel',3)")

print()
print('{cat_id} remaining:', t.count('{cat_id}'))
onclicks = re.findall(r'onclick="goGB\([^)]+\)"', t)
for o in onclicks:
    print(o)

with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html', 'w', encoding='utf-8') as f:
    f.write(t)
print()
print('Written. Size:', len(t))
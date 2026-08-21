with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-mat.html', encoding='utf-8') as f:
    ref = f.read()

# Find nav
pos = ref.find('class="navbar"')
print(f'navbar at: {pos}')
print(repr(ref[pos-20:pos+200]))

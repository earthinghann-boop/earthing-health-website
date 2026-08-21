import re

with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-mat.html', encoding='utf-8') as f:
    ref = f.read()

# Find nav start
nav_start = ref.find('<nav class="navbar"')
# Find nav end - count nesting
pos = nav_start
depth = 0
while pos < len(ref):
    next_open = ref.find('<nav', pos)
    next_close = ref.find('</nav>', pos)
    if next_close < 0:
        break
    if next_open >= 0 and next_open < next_close:
        depth += 1
        pos = next_open + 4
    else:
        depth -= 1
        pos = next_close + 6
        if depth == 0:
            nav_end = pos
            break

print(f'Nav: {nav_start} - {nav_end} ({nav_end-nav_start} chars)')
print('Start:', repr(ref[nav_start:nav_start+100]))
print('End:', repr(ref[nav_end-100:nav_end]))

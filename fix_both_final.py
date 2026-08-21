import re
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html', encoding='utf-8') as f:
    t = f.read()

# ── Locate each carousel block by its section boundary ─────────────
def get_block(html, start_kw, end_kw):
    s = html.find(start_kw)
    e = html.find(end_kw, s + 1)
    return s, e

# puSheetCarousel block: from id to next id
s1s, s1e = get_block(t, 'id="puSheetCarousel"', 'id="puDeskCarousel"')
# puDeskCarousel block: from id to next section/cta
s2s, s2e = get_block(t, 'id="puDeskCarousel"', '<section class="collection-cta"')

# In each block, replace the dots onclick with correct carousel ID
def fix_dots(html, block_s, block_e, cid):
    block = html[block_s:block_e]
    for i in range(4):
        old = f"onclick=\"goGB('puSheetCarousel',{i})\""
        new = f"onclick=\"goGB('{cid}',{i})\""
        # Only replace within this block
        block_new = block.replace(old, new, 1)
        if block_new != block:
            block = block_new
        else:
            # Already correct or was different (puDesk->puSheet already happened)
            # Try current id pattern
            pass
    return html[:block_s] + block + html[block_e:]

# Fix puDeskCarousel: restore puDesk IDs from wrongly-applied puSheet replacements
# Pattern: in puDeskCarousel block, dots should have cid='puDeskCarousel'
# Find puDeskCarousel dots in block and fix them
block2 = t[s2s:s2e]
print('Before fix, puDeskCarousel block dots:')
dots_in_block2 = re.findall(r"onclick=\"goGB\([^)]+\)\"", block2)
for d in dots_in_block2:
    print(' ', d)

# Do targeted replacements within puDeskCarousel block
for i in range(4):
    old_wrong = f"onclick=\"goGB('puSheetCarousel',{i})\""
    new_right = f"onclick=\"goGB('puDeskCarousel',{i})\""
    block2_new = block2.replace(old_wrong, new_right, 1)
    if block2_new != block2:
        print(f'Fixed dot {i} in puDeskCarousel block')
        block2 = block2_new

print()
print('After fix, puDeskCarousel block dots:')
dots_after = re.findall(r"onclick=\"goGB\([^)]+\)\"", block2)
for d in dots_after:
    print(' ', d)

t = t[:s2s] + block2 + t[s2e:]

# Remove stray goGB(...)
t = t.replace("goGB(...)", "/* inline handler */")

with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html', 'w', encoding='utf-8') as f:
    f.write(t)

# Final verification
print()
print('Final verification:')
all_onclicks = re.findall(r"onclick=\"goGB\([^)]+\)\"", t)
for o in all_onclicks:
    print(' ', o)
print('Total:', len(all_onclicks))
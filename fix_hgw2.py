import re

with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-mat.html', encoding='utf-8') as f:
    html = f.read()

# "How Grounding Works" is an h2 at the END of the file content
# (it's the 3rd remaining h2: Grounding Quilt Mat, Available Colors, How Grounding Works)
# Since we removed all others, let's find it and backtrack

hgw_pos = html.find('How Grounding Works')
print(f"Text at: {hgw_pos}")

# Find the h2 tag
h2_tag_pos = html.rfind('<h2', 0, hgw_pos)
print(f"h2 tag at: {h2_tag_pos}")

# Find the <section> before this h2
# Walk backward from h2_tag_pos to find <section
pos = h2_tag_pos
while pos >= 0:
    if html[pos:pos+9] == '<section ' or html[pos:pos+9] == '<section>':
        break
    pos -= 1
sec_start = pos
print(f"Section starts at {sec_start}: {repr(html[sec_start:sec_start+60])}")

# Now find the matching </section>
# Walk forward from sec_start, count nesting
depth = 0
pos = sec_start
while pos < len(html):
    next_open = html.find('<section', pos)
    next_close = html.find('</section>', pos)
    if next_open < 0 and next_close < 0:
        break
    if next_close < 0 or (0 <= next_open < next_close):
        # next open comes first
        depth += 1
        pos = next_open + 9
    else:
        # next close comes first
        depth -= 1
        pos = next_close + 10
        if depth == 0:
            sec_end = pos
            break

print(f"Section ends at {sec_end}: {repr(html[sec_end-20:sec_end])}")
section = html[sec_start:sec_end]
print(f"Section size: {len(section)} chars")

# Confirm it has our heading
if 'How Grounding Works' in section:
    print("CONFIRMED: contains 'How Grounding Works'")
else:
    print("ERROR: does not contain 'How Grounding Works'")
    # Debug: print surrounding context
    print("Context around h2:", repr(html[h2_tag_pos-100:h2_tag_pos+100]))

# Delete
html = html[:sec_start] + html[sec_end:]
print(f"\nAfter deletion: {len(html):,} chars")

with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-mat.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Verify
remaining = [re.sub(r'<[^>]+>','',m.group()).strip() for m in re.finditer(r'<h2[^>]*>(.*?)</h2>',html,re.DOTALL)]
print(f"Remaining h2s: {remaining}")
print("'How Grounding Works' still there?", 'How Grounding Works' in html)
print("Size:", len(html))

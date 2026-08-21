import re

with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-mat.html', encoding='utf-8') as f:
    html = f.read()

# Find the section with h2 "How Grounding Works"
# Strategy: find h2, backtrack to <section, forward to </section>
h2_pos = html.find('<h2') + html[html.find('<h2')+4:].find('<h2')
# More reliable: find "How Grounding Works" and backtrack
hgw_text = 'How Grounding Works'
hgw_pos = html.find(hgw_text)
print(f"'How Grounding Works' text at: {hgw_pos}")

# Backtrack from h2 to find section open
pos = hgw_pos
while pos >= 0 and not html[pos:pos+9].startswith('<section'):
    pos -= 1
sec_start = pos
print(f"Section start: {sec_start} -> {html[sec_start:sec_start+50]}")

# Forward from section start to find section close
# The section at 47428 closes at 49357
pos = sec_start
while pos < len(html):
    end = html.find('</section>', pos)
    if end < 0:
        break
    # Check if this </section> belongs to our section
    # Count <section> tags between sec_start and this </section>
    inner = html[sec_start:end]
    opens = inner.count('<section')
    closes = inner.count('</section>')
    if opens == closes:
        sec_end = end + len('</section>')
        break
    pos = end + len('</section>')

print(f"Section end: {sec_end} -> {html[sec_end-20:sec_end]}")
section_content = html[sec_start:sec_end]
print(f"Section length: {len(section_content)} chars")
print("Preview:", section_content[:200])

# Delete it
html = html[:sec_start] + html[sec_end:]
print(f"\nAfter deletion: {len(html):,} chars")

# Save
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-mat.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Verify
remaining_h2 = [re.sub(r'<[^>]+>', '', m.group()).strip()
                for m in re.finditer(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL)]
print(f"\nRemaining h2 headings: {remaining_h2}")
print(f"Size: {len(html):,}")
print("How Grounding Works still there?", 'How Grounding Works' in html)

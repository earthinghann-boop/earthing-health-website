import re

with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-mat.html', encoding='utf-8') as f:
    html = f.read()

# Check remaining sections
print("=== Remaining h2 headings ===")
for m in re.finditer(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL):
    t = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    print(f"  {t}")

print()
# Check How Grounding Works context
pos = html.find('How Grounding Works')
if pos >= 0:
    print(f"How Grounding Works at pos {pos}")
    print(html[pos-200:pos+300])
else:
    print("How Grounding Works NOT in file")

print()
# Check hero-badge count
print(f"hero-badge count: {html.count('hero-badge')}")

# Find all collection-hero sections
for m in re.finditer(r'class="collection-hero"', html):
    start = html.rfind('<section', 0, m.start())
    end = html.find('</section>', m.start()) + len('</section>')
    print(f"\ncollection-hero section: {end-start} chars")
    print(html[start:end][:500])

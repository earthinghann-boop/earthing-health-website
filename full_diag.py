import re

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
with open(WD + r'\grounding-mat.html', encoding='utf-8') as f:
    html = f.read()

# Find all section boundaries
print("=== ALL <section> and </section> positions ===")
sec_starts = [(m.start(), m.group()) for m in re.finditer(r'<section\b', html)]
sec_ends = [(m.start(), m.group()) for m in re.finditer(r'</section>', html)]
print(f"Opens: {len(sec_starts)}, Closes: {len(sec_ends)}")
for pos, tag in sec_starts:
    cls = re.search(r'class="([^"]*)"', tag)
    h_match = re.search(r'<h[12][^>]*>(.*?)</h[12]>', html[pos:pos+2000], re.DOTALL)
    htext = re.sub(r'<[^>]+>', '', h_match.group(1)).strip()[:40] if h_match else ''
    print(f"  OPEN {pos}: {cls.group(1)[:30] if cls else 'no-class'} | h={htext}")
for pos, tag in sec_ends:
    prev_h = re.search(r'<h[12][^>]*>(.*?)</h[12]>', html[max(0,pos-2000):pos], re.DOTALL)
    htext = re.sub(r'<[^>]+>', '', prev_h.group(1)).strip()[:40] if prev_h else ''
    print(f"  CLOSE {pos}: {htext}")

print()
# Where is "How Grounding Works"?
pos_hgw = html.find('How Grounding Works')
print(f"'How Grounding Works' at pos: {pos_hgw}")
# Find all h2 headings
for m in re.finditer(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL):
    t = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    print(f"  h2 '{t}' at {m.start()}")

print()
# Check CSS dots rules with specificity
print("=== CSS .gb-carousel-dot rules ===")
for m in re.finditer(r'\.gb-carousel-dot\s*\{[^}]*\}', html, re.DOTALL):
    print(f"  Rule: {m.group()[:200]}")

print()
print("=== CSS .gb-carousel-dots rules ===")
for m in re.finditer(r'\.gb-carousel-dots\s*\{[^}]*\}', html, re.DOTALL):
    print(f"  Rule: {m.group()[:200]}")

print()
print("=== CSS .gb-carousel rules ===")
for m in re.finditer(r'\.gb-carousel\s*\{[^}]*\}', html, re.DOTALL):
    print(f"  Rule: {m.group()[:200]}")

print()
# Show carousel CSS area
gb_start = html.find('.gb-carousel {')
if gb_start >= 0:
    print("=== gb-carousel CSS area (500 chars) ===")
    print(html[gb_start:gb_start+500])

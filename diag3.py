import re

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
with open(WD + r'\grounding-mat.html', encoding='utf-8') as f:
    html = f.read()

# Find all .active rules
print("=== All CSS .active rules ===")
for m in re.finditer(r'(?<![.#\w])\.active\s*\{[^}]*\}', html, re.DOTALL):
    print(m.group()[:200])

print()
# Find all .gb-carousel-dot.active rules
print("=== .gb-carousel-dot.active rules ===")
for m in re.finditer(r'\.gb-carousel-dot\.active\s*\{[^}]*\}', html, re.DOTALL):
    print(m.group()[:200])

print()
# Check what rules reference .active after .gb-carousel-dot
# Show the CSS area around the dots
dot_pos = html.find('.gb-carousel-dot')
# Find the style block that contains it
style_m = re.search(r'<style>(.*?\.gb-carousel-dots.*?)</style>', html, re.DOTALL)
if style_m:
    print("=== Style block containing dots ===")
    content = style_m.group(1)
    # Show from .gb-carousel-dots to end of that section
    dots_start = content.find('.gb-carousel-dots')
    dots_end = content.find('.gb-category-text', dots_start)
    if dots_end < 0:
        dots_end = dots_start + 2000
    print(content[dots_start:dots_end])

print()
# Key question: where is .active { background } coming from?
# Search for just ".active {" in CSS
for m in re.finditer(r'\.active\s*\{', html):
    pos = m.start()
    rule_content = html[pos:pos+150]
    print(f"At {pos}: {rule_content[:120]}")
    print()

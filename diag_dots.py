import re

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
with open(WD + r'\grounding-mat.html', encoding='utf-8') as f:
    html = f.read()

# Find matCarousel and show its full content
carousel_match = re.search(
    r'(<div class="gb-carousel" id="matCarousel"[^>]*>.*?)(?=\n\s*<div class="gb-category-text")',
    html, re.DOTALL)
if carousel_match:
    content = carousel_match.group(1)
    print("=== matCarousel HTML ===")
    print(content)
    print()
    print("=== Dot elements ===")
    dots = list(re.finditer(r'<button[^>]*class="gb-carousel-dot[^"]*"[^>]*>', content))
    for i, d in enumerate(dots):
        print(f"[{i}] {d.group()}")
    print(f"Total dots: {len(dots)}")
    onclick_dots = list(re.finditer(r'<button[^>]*onclick="goGB\([^"]+"', content))
    print(f"Total dots with onclick: {len(onclick_dots)}")

print()
# Check how grounding works
pos = html.find('How Grounding Works')
if pos >= 0:
    # Find enclosing section
    sec_start = html.rfind('<section', 0, pos)
    print(f"How Grounding Works pos: {pos}")
    print(f"Section start: {sec_start}")
    # Print 100 chars around section start
    if sec_start >= 0:
        print("Context around section start:")
        print(repr(html[sec_start-50:sec_start+100]))
    # Find the section end
    # First check if there's a preceding </section>
    prev_close = html.rfind('</section>', 0, pos)
    print(f"Previous </section> at: {prev_close}")
    # Section content
    if sec_start >= 0:
        sec_end = html.find('</section>', pos)
        print(f"Section ends at: {sec_end}")
        # How many sections total
        sections = [(m.start(), re.search(r'<h[12][^>]*>(.*?)</h[12]>', html[m.start():m.start()+500], re.DOTALL))
                    for m in re.finditer(r'<section', html)]
        print(f"\nTotal sections: {len(sections)}")
        for i, (spos, hm) in enumerate(sections):
            htext = re.sub(r'<[^>]+>', '', hm.group(1)).strip()[:50] if hm else '(no h)'
            print(f"  [{i}] pos={spos} h={htext}")

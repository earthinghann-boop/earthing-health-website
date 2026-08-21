import urllib.request, re, time

url = f'https://www.silveryes.com/pu-earthing-mat.html?nocache={int(time.time()*1000)}'
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache','Pragma':'no-cache'})
with urllib.request.urlopen(req, timeout=15) as r:
    html = r.read().decode('utf-8')

print('Vercel size:', len(html))

# 1. Find all .gb-carousel rules and print them all
style_m = re.search(r'<style>\s*(.*?)\s*</style>', html, re.DOTALL)
css = style_m.group(1) if style_m else ''

rules = {}
i = 0
while i < len(css):
    sel_start = css.find('.', i)
    if sel_start == -1: break
    brace = css.find('{', sel_start)
    if brace == -1: break
    selector = css[sel_start:brace].strip()
    depth = 1; j = brace+1
    while j < len(css) and depth > 0:
        if css[j] == '{': depth += 1
        elif css[j] == '}': depth -= 1
        j += 1
    if depth == 0:
        content = re.sub(r'\s+', ' ', css[brace+1:j-1]).strip()
        rules[selector] = content
        i = j
    else:
        break

print()
print('=== ALL .gb-carousel / .gb-carousel-dots / .gb-carousel-dot rules ===')
for sel, content in sorted(rules.items()):
    if 'carousel' in sel:
        print(f'{sel}: {{ {content} }}')

# 2. Show carousel HTML structure
print()
print('=== puSheetCarousel HTML (first 800 chars) ===')
idx = html.find('id="puSheetCarousel"')
end = html.find('id="puDeskCarousel"')
seg = html[idx:end+200]
print(repr(seg[:800]))

# 3. Show any > characters visible in the rendered area
print()
print('=== Looking for > in carousel area ===')
# Find all text nodes near > in the carousel section
for match in re.finditer(r'&gt;|<[^/!][^>]*>', seg):
    print('  Found:', repr(match.group()))
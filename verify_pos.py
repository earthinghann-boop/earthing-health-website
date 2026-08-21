import urllib.request, re, time

url = f'https://www.silveryes.com/pu-earthing-mat.html?nocache={int(time.time()*1000)}'
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache','Pragma':'no-cache'})
with urllib.request.urlopen(req, timeout=15) as r:
    html = r.read().decode('utf-8')

print('Vercel size:', len(html))
print()

# Extract .gb-carousel-dots CSS rule
style_m = re.search(r'<style>\s*(.*?)\s*</style>', html, re.DOTALL)
css = style_m.group(1) if style_m else ''

# Find .gb-carousel-dots rule
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
        content = css[brace+1:j-1]
        rules[selector] = content
        i = j
    else:
        break

dots = rules.get('.gb-carousel-dots', 'NOT FOUND')
print('.gb-carousel-dots CSS:')
print('  ' + dots.strip())

print()
dots_css = rules.get('.gb-carousel-dot', 'NOT FOUND')
print('.gb-carousel-dot CSS:')
print('  ' + dots_css.strip())
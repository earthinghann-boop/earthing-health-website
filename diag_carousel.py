import urllib.request, re, time

for page, name in [
    ('https://www.silveryes.com/groundingbedding.html', 'groundingbedding'),
    ('https://www.silveryes.com/pu-earthing-mat.html', 'pu-earthing-mat'),
]:
    url = page + '?nocache=' + str(int(time.time()*1000))
    req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache'})
    with urllib.request.urlopen(req, timeout=15) as r:
        html = r.read().decode('utf-8')

    m_css = re.search(r'<style>\s*(.*?)\s*</style>', html, re.DOTALL)
    css = m_css.group(1) if m_css else ''

    def get_rule(css, sel):
        idx = css.find(sel + ' {')
        if idx < 0: return None
        depth=0; j=idx+len(sel)+1
        while j < len(css):
            if css[j]=='{': depth+=1
            elif css[j]=='}':
                depth-=1
                if depth==0: return css[idx:j+1]
            j+=1
        return None

    print(f'=== {name} ===')

    for sel in ['.gb-carousel', '.gb-category-section', '.gb-category-layout', '.collection-hero']:
        rule = get_rule(css, sel)
        if rule:
            # Normalize whitespace
            clean = re.sub(r'\s+', ' ', rule).strip()
            print(f'  {sel}: {clean[:200]}')
        else:
            print(f'  {sel}: NOT FOUND')

    # Check hero section height
    hero_h = re.search(r'\.collection-hero[^}]*\{([^}]+)\}', css)
    if hero_h:
        props = hero_h.group(1)
        for line in props.split('\n'):
            line = line.strip()
            if line:
                print(f'  hero prop: {line}')
    print()
import urllib.request, re, time

# Get groundingbedding CSS from Vercel (confirmed working)
url = 'https://www.silveryes.com/groundingbedding.html?nocache=' + str(int(time.time()*1000))
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache'})
with urllib.request.urlopen(req, timeout=15) as r:
    gb_html = r.read().decode('utf-8')

m = re.search(r'\.gb-carousel-dots \{([^}]+)\}', gb_html, re.DOTALL)
if m:
    print('groundingbedding .gb-carousel-dots:')
    props = m.group(1)
    print(props[:500])
    print()
    # Parse each property
    for line in props.split('\n'):
        line = line.strip()
        if line and not line.startswith('//'):
            print(' ', line)

print()
print('='*50)
print('pu-earthing-mat local .gb-carousel-dots:')
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html', encoding='utf-8') as f:
    pu = f.read()
m2 = re.search(r'\.gb-carousel-dots \{([^}]+)\}', pu, re.DOTALL)
if m2:
    props2 = m2.group(1)
    print(props2[:500])
    for line in props2.split('\n'):
        line = line.strip()
        if line:
            print(' ', line)
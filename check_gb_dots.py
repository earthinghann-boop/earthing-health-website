import re
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', encoding='utf-8') as f:
    gb = f.read()

print('groundingbedding.html size:', len(gb))

# Check dots structure
for cid in ['fittedCarousel','flatCarousel','pillowCarousel']:
    idx = gb.find(f'id="{cid}"')
    if idx >= 0:
        end = idx + 1500
        segment = gb[idx:end]
        dots_match = re.findall(r'<span[^>]*>[^<]*</span>', segment)
        onclick_match = re.findall(r'onclick="([^"]+)"', segment)
        print(f'\n{cid}:')
        print('  spans:', dots_match[:6])
        print('  onclicks:', onclick_match[:6])
        print('  imgs in segment:', re.findall(r'images/[^"]+\.(jpg|png)', segment))
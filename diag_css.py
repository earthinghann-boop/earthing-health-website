with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-blanket.html', encoding='utf-8') as f:
    html = f.read()

# Find grCarousel
pos = html.find('#grCarousel')
if pos > 0:
    print(f'#grCarousel at {pos}:')
    print(repr(html[pos:pos+800]))
else:
    print('Not found by #grCarousel')
    # Try grCarousel
    pos = html.find('grCarousel')
    if pos > 0:
        print(f'grCarousel at {pos}:')
        print(repr(html[pos-50:pos+600]))

# Also show what's in style block for carousel
pos2 = html.find('.gb-carousel')
if pos2 > 0:
    print(f'\n.gb-carousel at {pos2}:')
    print(repr(html[pos2:pos2+500]))

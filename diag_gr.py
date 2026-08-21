with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-blanket.html', encoding='utf-8') as f:
    html = f.read()

# Find Natural Grounding section
pos = html.find('Natural Grounding')
if pos > 0:
    print(f'Natural Grounding at {pos}:')
    # Show 2000 chars
    snippet = html[pos-50:pos+2000]
    print(snippet)

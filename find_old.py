import re
with open('index.html', 'rb') as f:
    text = f.read().decode('utf-8')
# Find all old refs with line context
for m in re.finditer(r'earthing-fitted-sheet\.html', text):
    start = max(0, m.start() - 150)
    end = min(len(text), m.end() + 50)
    print('--- match at pos', m.start(), '---')
    print(text[start:end])
    print()
import re
files = ['index.html','emf-wearing.html','grounding-blanket.html','grounding-kit.html','grounding-mat.html','grounding-pillow-cases.html','grounding-sheets.html','pu-earthing-mat.html']
for f in files:
    with open(f, 'rb') as fp:
        text = fp.read().decode('utf-8')
    matches = re.findall(r'href="([^"]*fitted-sheet[^"]*|[^"]*groundingbedding[^"]*)"', text)
    if matches:
        print(f, matches)
print('---DONE---')
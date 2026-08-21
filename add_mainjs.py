with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', 'rb') as f:
    text = f.read().decode('utf-8')

# Insert <script src="js/main.js"></script> right before the existing carousel inline script
# The inline script is the last <script> block. Find it and add main.js before it.
needle = '<script>\n        /* Grounding Bedding Collection'
if needle in text:
    text = text.replace(needle, '<script src="js/main.js"></script>\n    <script>\n        /* Grounding Bedding Collection', 1)
    print('Inserted main.js before carousel script')
else:
    print('Needle not found - trying alt')
    # Try simpler
    if '<script>' in text and '/* Grounding Bedding' in text:
        # Just find first <script> and prepend main.js
        idx = text.find('<script>')
        text = text[:idx] + '<script src="js/main.js"></script>\n    ' + text[idx:]
        print('Inserted before first inline script')

with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', 'w', encoding='utf-8') as f:
    f.write(text)

import os
print('New size:', os.path.getsize(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html'))
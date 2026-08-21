with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', 'rb') as f:
    text = f.read().decode('utf-8')

old = '<script>\n(function(){\n    var CAROUSELS'
new = '<script src="js/main.js"></script>\n    <script>\n(function(){\n    var CAROUSELS'

if old in text:
    text = text.replace(old, new, 1)
    print('Replaced inline-script opener')
else:
    # alt: just look for the first "<script>" not preceded by src=
    idx = text.find('<script>')
    print('First <script> at:', idx)
    print('Context:', repr(text[idx-30:idx+30]))
    text = text[:idx] + '<script src="js/main.js"></script>\n    ' + text[idx:]
    print('Fallback: inserted before first <script>')

with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', 'w', encoding='utf-8') as f:
    f.write(text)

import os
print('New size:', os.path.getsize(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html'))
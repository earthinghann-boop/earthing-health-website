#!/usr/bin/env python3
"""Inject 550x550 fixed-size CSS for #grCarousel into grounding-blanket.html"""
import os

WD = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
HTML = os.path.join(WD, 'grounding-blanket.html')

with open(HTML, encoding='utf-8') as f:
    html = f.read()

# ── Inject fixed-size CSS for grCarousel ────────────────────────────
# Inject before </style>
gr_fix_css = '''
        /* grCarousel: fixed 550x550 size */
        #grCarousel {
            width: 550px !important;
            height: 550px !important;
            aspect-ratio: unset !important;
            flex-shrink: 0;
        }
        #grCarousel .gb-carousel-img {
            width: 550px !important;
            height: 550px !important;
        }
        /* emfCarousel: keep responsive (optional: can also fix here) */
        #emfCarousel {
            width: 100%;
            height: auto;
            aspect-ratio: 1/1;
        }
        #emfCarousel .gb-carousel-img {
            width: 100%;
            height: 100%;
        }
'''

# Find </style> tag
style_close = html.rfind('</style>')
if style_close < 0:
    print('ERROR: </style> not found')
else:
    html = html[:style_close] + gr_fix_css + '\n    ' + html[style_close:]
    print(f'Injected CSS before </style> at {style_close}')

with open(HTML, 'w', encoding='utf-8') as f:
    f.write(html)

print('Saved. Verifying...')

# Quick check
with open(HTML, encoding='utf-8') as f:
    chk = f.read()
pos = chk.find('#grCarousel')
print(f'#grCarousel CSS at: {pos}')
print(chk[pos:pos+300])

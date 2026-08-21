import os
from PIL import Image

sets = {
    'EMF': (r'C:\Users\18574\Desktop\EARTHING\image\盖毯',
             ['1F0A1813.jpg','1F0A1816.jpg','1F0A1812.jpg','1F0A1820.jpg']),
    'Colors': (r'C:\Users\18574\Desktop\EARTHING\silveryes网站',
               ['silver004.jpg']),
    'Grounding': (r'C:\Users\18574\Desktop\EARTHING\image\法兰绒',
                  ['换脸安吉丽娜.png','xxjdfalksjflsajdlfdfdsf.webp',
                   '3812581e-fef3-4257-8b20-e2c768025a48.__CR0,0,300,300_PT0_SX300_V1___.jpg',
                   '7_ba10d0ec-a41e-4125-ba23-cb33d3955bc7.jpg',
                   '71VUT0FboKL._AC_SX679_.jpg']),
}

for name, (dir_, files) in sets.items():
    print(f'\n=== {name} ===')
    for f in files:
        p = os.path.join(dir_, f)
        if os.path.exists(p):
            sz = os.path.getsize(p)
            try:
                img = Image.open(p)
                print(f'  OK  {f}: {img.size} {sz:,}b')
            except Exception as e:
                print(f'  IMG ERR {f}: {e} {sz:,}b')
        else:
            print(f'  MISSING {f}')

import os
from PIL import Image

# Search for the file
search_paths = [
    r'C:\Users\18574\Desktop\EARTHING\image\法兰绒',
    r'C:\Users\18574\Desktop\EARTHING\image',
    r'C:\Users\18574\Desktop\EARTHING',
]
for p in search_paths:
    if os.path.exists(p):
        for f in os.listdir(p):
            if '脸替换' in f or '脸' in f:
                fp = os.path.join(p, f)
                sz = os.path.getsize(fp)
                img = Image.open(fp)
                print(f'Found: {fp}\n  size={img.size}, {sz:,}b')

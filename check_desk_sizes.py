from PIL import Image
import os

base = r'C:\Users\18574\Desktop\EARTHING\image\台垫26x68'
for f in [
    'Conductive-Keyboard-Foot-Mat-Sleep-Earthed-Plug-Cable-1-Full-Keyboard-Desk-Closeup-Web-1500.jpg',
    'earthing-and-grounding-mat-68-x-25-cm-5342316.webp',
    '61cObI19fpL._AC_.jpg',
    '81v9WvyxERL._AC_SX679_.jpg'
]:
    p = os.path.join(base, f)
    im = Image.open(p)
    print(f'{im.size[0]:5}x{im.size[1]:5}  {os.path.getsize(p)//1024:>6}KB  {f}')
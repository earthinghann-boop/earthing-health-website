import os
src1 = r'C:\Users\18574\Desktop\EARTHING\image\PU垫\皮革垫\WPS图片批量处理'
print('=== PU Sheet sources (in', src1, ') ===')
for f in ['445A4539.jpg','445A4529.jpg','445A4527.jpg','1F0A4103.jpg']:
    p = os.path.join(src1, f)
    if os.path.exists(p):
        from PIL import Image
        try:
            im = Image.open(p)
            print(f'  OK {im.size[0]}x{im.size[1]:5}  {os.path.getsize(p)//1024}KB  {f}')
        except Exception as e:
            print('  ERR', f, e)
    else:
        print('  MISS', p)

print()
print('=== PU Desk Mat sources (in C:\\Users\\18574\\Desktop\\EARTHING\\image) ===')
src2 = r'C:\Users\18574\Desktop\EARTHING\image'
for f in [
    'Conductive-Keyboard-Foot-Mat-Sleep-Earthed-Plug-Cable-1-Full-Keyboard-Desk-Closeup-Web-1500.jpg',
    'earthing-and-grounding-mat-68-x-25-cm-5342316.webp',
    '61cObI19fpL._AC_.jpg',
    '81v9WvyxERL._AC_SX679_.jpg'
]:
    p = os.path.join(src2, f)
    if os.path.exists(p):
        from PIL import Image
        try:
            im = Image.open(p)
            print(f'  OK {im.size[0]}x{im.size[1]:5}  {os.path.getsize(p)//1024}KB  {f}')
        except Exception as e:
            print('  ERR', f, e)
    else:
        print('  MISS', p)
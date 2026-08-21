from PIL import Image
import os

# Check actual dimensions of candidate images
paths = [
    r'C:\Users\18574\Desktop\EARTHING\image\PU垫图片\2.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\PU垫图片\主图1.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\PU垫图片\主图3_1.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\PU垫图片\主图5.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\PU垫图片\主图6.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\1.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\2.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\blue.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\green.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\细节1.png',
    r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\细节2.png',
    r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\灰.png',
    r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\小.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\实景.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\台垫26x68\1_2.webp',
    r'C:\Users\18574\Desktop\EARTHING\image\台垫26x68\微信图片_20250104100804.jpg' if False else None,
    r'C:\Users\18574\Desktop\EARTHING\image\PU垫\皮革垫.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\PU垫\主图4.png',
    r'C:\Users\18574\Desktop\EARTHING\image\PU垫\主图5.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\PU垫\主图6.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\PU垫\主图7.png',
    r'C:\Users\18574\Desktop\EARTHING\image\PU垫\原图1.png',
    r'C:\Users\18574\Desktop\EARTHING\image\PU垫\原图2.png',
    r'C:\Users\18574\Desktop\EARTHING\image\PU垫\原图3.png',
    r'C:\Users\18574\Desktop\EARTHING\image\PU垫\原图4.png',
    r'C:\Users\18574\Desktop\EARTHING\image\PU垫\配件.png',
    r'C:\Users\18574\Desktop\EARTHING\image\PU垫图片\B0CVVTY7HG.PT06.jpg.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\PU垫\微信截图_20241202172017.png',
    r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\微信图片_20241205125136.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\微信图片_20241205130115.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\微信图片_20241205131051.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\微信图片_20241205131648.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\微信图片_20241205133943.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\微信图片_20241205134659.jpg',
    r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\微信图片_20241205135556.jpg',
]
for p in paths:
    if p is None or not os.path.exists(p):
        continue
    try:
        im = Image.open(p)
        w, h = im.size
        print(f'  {w}x{h:5}  {os.path.basename(p):30s}  {os.path.getsize(p)//1024:5d}KB  {os.path.dirname(p)[-10:]}')
    except Exception as e:
        print('  ERR', p, e)
from PIL import Image
import os
import shutil

OUT_BASE = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\images\products'
os.makedirs(OUT_BASE, exist_ok=True)

# (subdir, source_filename) pairs
selections = {
    'pu_sheet': [
        r'C:\Users\18574\Desktop\EARTHING\image\PU垫图片\主图1.jpg',
        r'C:\Users\18574\Desktop\EARTHING\image\PU垫图片\主图3_1.jpg',
        r'C:\Users\18574\Desktop\EARTHING\image\PU垫图片\主图5.jpg',
        r'C:\Users\18574\Desktop\EARTHING\image\PU垫图片\主图6.jpg',
    ],
    'pu_desk_mat': [
        r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\1.jpg',
        r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\2.jpg',
        r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\blue.jpg',
        r'C:\Users\18574\Desktop\EARTHING\image\鼠标垫彩色\green.jpg',
    ],
    'pu_yoga_mat': [
        r'C:\Users\18574\Desktop\EARTHING\image\PU垫\原图1.png',
        r'C:\Users\18574\Desktop\EARTHING\image\PU垫\原图2.png',
        r'C:\Users\18574\Desktop\EARTHING\image\PU垫\原图3.png',
        r'C:\Users\18574\Desktop\EARTHING\image\PU垫\原图4.png',
    ],
}

for sub, files in selections.items():
    out_dir = os.path.join(OUT_BASE, sub)
    os.makedirs(out_dir, exist_ok=True)
    for i, src in enumerate(files, 1):
        if not os.path.exists(src):
            print('  MISS', src)
            continue
        out_path = os.path.join(out_dir, f'{i}.jpg')
        try:
            im = Image.open(src)
            im = im.convert('RGB')
            # Resize to max 1200x1200 (keep aspect, fit into square)
            im.thumbnail((1200, 1200), Image.LANCZOS)
            # If not square, pad to square with white
            if im.size[0] != im.size[1]:
                w, h = im.size
                size = max(w, h)
                new = Image.new('RGB', (size, size), (255, 255, 255))
                offset = ((size - w) // 2, (size - h) // 2)
                new.paste(im, offset)
                im = new
            im.save(out_path, 'JPEG', quality=85, optimize=True)
            print(f'  OK  {sub}/{i}.jpg  {os.path.getsize(out_path)//1024}KB')
        except Exception as e:
            print(f'  ERR {sub}/{i}.jpg: {e}')
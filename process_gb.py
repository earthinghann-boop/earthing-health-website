import os, shutil
from PIL import Image

# ============ Step 1: Resize & copy images ============
src_map = {
    'fitted_sheet': (r'C:\Users\18574\Desktop\EARTHING\image\原图\海军蓝', ['9D2A1907.jpg','9D2A1905.jpg','9D2A1913.jpg','9D2A1837.jpg']),
    'flat_sheet': (r'C:\Users\18574\Desktop\EARTHING\image\原图\蓝色床单床笠', ['1F0A2579.jpg','1F0A2581.jpg','1F0A2591.jpg','1F0A2589.jpg']),
    'pillow_case': (r'C:\Users\18574\Desktop\EARTHING\image\原图\白碎花', ['9D2A1993.jpg','9D2A2000.jpg','9D2A1995.jpg','9D2A1996.jpg']),
    'duvet_cover': (r'C:\Users\18574\Desktop\EARTHING\image\原图\绿色', ['445A4388.jpg','445A4390.jpg','445A4398.jpg','445A4399.jpg']),
    'kids_bedding': (r'C:\Users\18574\Desktop\EARTHING\image\儿童盖毯', ['1F0A1625.jpg','1F0A1648.jpg','1F0A1711.jpg','1F0A1718.jpg'])
}
dst_base = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\images\products'
MAX_DIM = 1200  # max width or height in px

print('=== Resizing & copying images ===')
for cat, (src_dir, fnames) in src_map.items():
    dst_dir = os.path.join(dst_base, cat)
    os.makedirs(dst_dir, exist_ok=True)
    for i, fname in enumerate(fnames, start=1):
        src_p = os.path.join(src_dir, fname)
        # Output always 1.jpg, 2.jpg, 3.jpg, 4.jpg in dst
        dst_p = os.path.join(dst_dir, str(i) + '.jpg')
        try:
            img = Image.open(src_p)
            img = img.convert('RGB')
            w, h = img.size
            if w > MAX_DIM or h > MAX_DIM:
                if w >= h:
                    new_w = MAX_DIM
                    new_h = int(h * MAX_DIM / w)
                else:
                    new_h = MAX_DIM
                    new_w = int(w * MAX_DIM / h)
                img = img.resize((new_w, new_h), Image.LANCZOS)
            img.save(dst_p, 'JPEG', quality=85, optimize=True)
            out_size = os.path.getsize(dst_p)
            print('  [OK]', cat, str(i)+'.jpg', '(', img.size[0], 'x', img.size[1], ',', out_size, 'bytes )')
        except Exception as e:
            print('  [FAIL]', cat, str(i)+'.jpg', '-', e)
print()
print('=== Done ===')
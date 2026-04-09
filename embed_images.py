# -*- coding: utf-8 -*-
import os
import re
import base64
import sys
from PIL import Image

SITE_ROOT = r"C:\Users\18574\.qclaw\workspace\earthinghealth-website"
HTML_PATH = os.path.join(SITE_ROOT, "index.html")
OUTPUT_PATH = os.path.join(SITE_ROOT, "earthing_singlefile.html")
MAX_WIDTH = 1200
QUALITY = 80

def compress_image(src_path, site_root):
    """Compress image and return (data_url, mime)."""
    full = os.path.join(site_root, src_path)
    if not os.path.exists(full):
        print(f"  [SKIP] not found: {src_path}")
        return src_path

    ext = os.path.splitext(src_path)[1].lower()
    # Convert to jpeg for compression
    if ext in ['.jpg', '.jpeg', '.png', '.webp', '.gif']:
        try:
            img = Image.open(full)
            # Convert RGBA to RGB
            if img.mode in ('RGBA', 'P'):
                rgb = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                rgb.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = rgb
            elif img.mode != 'RGB':
                img = img.convert('RGB')

            # Resize if too large
            if img.width > MAX_WIDTH:
                ratio = MAX_WIDTH / img.width
                new_h = int(img.height * ratio)
                img = img.resize((MAX_WIDTH, new_h), Image.LANCZOS)

            # Save to bytes
            import io
            buf = io.BytesIO()
            img.save(buf, format='JPEG', quality=QUALITY, optimize=True)
            data = buf.getvalue()

            mime = 'image/jpeg'
            b64 = base64.b64encode(data).decode('ascii')
            orig_size = os.path.getsize(full)
            new_size = len(data)
            ratio_pct = new_size / orig_size * 100
            print(f"  {src_path}: {orig_size//1024}KB -> {new_size//1024}KB ({ratio_pct:.0f}%)")
            return f"data:{mime};base64,{b64}"
        except Exception as e:
            print(f"  [ERROR] {src_path}: {e}")
            return src_path
    return src_path

# Read HTML
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace image src with embedded data URLs
# Match src="..." for img tags
pattern = re.compile(r'src="((?!data:)[^"]+\.(jpg|jpeg|png|webp|gif))"', re.IGNORECASE)

def replacer(m):
    src = m.group(1)
    data_url = compress_image(src, SITE_ROOT)
    return f'src="{data_url}"'

print("Embedding images...")
new_content = pattern.sub(replacer, content)
print("\nDone embedding. Writing output file...")

with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Saved: {OUTPUT_PATH}")
print(f"File size: {os.path.getsize(OUTPUT_PATH) // 1024 // 1024} MB")

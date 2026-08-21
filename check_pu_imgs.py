import os

# Check available PU images
for d in ['previews', 'pu-earthing']:
    full = os.path.join(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\images', d)
    if os.path.isdir(full):
        print(f'=== images/{d} ===')
        for f in sorted(os.listdir(full)):
            if 'pu' in f.lower() or 'sheet' in f.lower() or 'desk' in f.lower() or 'mouse' in f.lower() or 'yoga' in f.lower() or 'mat' in f.lower():
                p = os.path.join(full, f)
                print('  ', os.path.getsize(p), f)
        print()

# Also check products/
print('=== images/products/ all dirs ===')
p = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\images\products'
if os.path.isdir(p):
    for d in sorted(os.listdir(p)):
        full = os.path.join(p, d)
        if os.path.isdir(full):
            count = len([f for f in os.listdir(full) if f.lower().endswith(('.jpg','.png'))])
            if count > 0:
                print(f'  {d}/  ({count} files)')
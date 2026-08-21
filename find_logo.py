import os, re, urllib.request

# 1. 检查 workspace images 目录有什么
img_dir = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\images'
print('=== images/ directory contents ===')
if os.path.exists(img_dir):
    for f in sorted(os.listdir(img_dir)):
        p = os.path.join(img_dir, f)
        if os.path.isdir(p):
            print(' [DIR] ', f)
            try:
                for ff in sorted(os.listdir(p))[:10]:
                    print('   ', ff)
                if len(os.listdir(p)) > 10:
                    print('   ... and', len(os.listdir(p))-10, 'more')
            except:
                pass
        else:
            print(' [FILE]', os.path.getsize(p), 'bytes', f)
else:
    print('MISSING:', img_dir)

print()
print('=== Search all HTML files for logo src ===')
for f in os.listdir(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'):
    if f.endswith('.html'):
        with open(os.path.join(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website', f), 'rb') as fp:
            t = fp.read().decode('utf-8')
        for m in re.finditer(r'src="([^"]*logo[^"]*)"', t):
            print('  ', f, '->', m.group(1))
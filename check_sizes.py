import subprocess
r = subprocess.run(['git', 'show', '87fa741:index.html'], capture_output=True, cwd=r'C:\Users\18574\.qclaw\workspace\earthinghealth-website')
head_bytes = r.stdout
print('HEAD bytes len:', len(head_bytes))

with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\index.html', 'rb') as f:
    disk_bytes = f.read()
print('Disk bytes len:', len(disk_bytes))

# Compare byte by byte
if head_bytes == disk_bytes:
    print('IDENTICAL bytes')
else:
    print('DIFFERENT')
    # Find first difference
    for i, (a, b) in enumerate(zip(head_bytes, disk_bytes)):
        if a != b:
            print(f'First diff at byte {i}: HEAD=0x{a:02x} disk=0x{b:02x}')
            ctx_start = max(0, i-30)
            print('HEAD context:', head_bytes[ctx_start:i+30])
            print('disk context:', disk_bytes[ctx_start:i+30])
            break
    else:
        if len(head_bytes) < len(disk_bytes):
            print(f'Disk has extra bytes after HEAD: {disk_bytes[len(head_bytes):len(head_bytes)+50]!r}')
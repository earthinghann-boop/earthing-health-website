import os
d = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'
for f in sorted(os.listdir(d)):
    if not f.endswith('.html'):
        continue
    p = os.path.join(d, f)
    with open(p, 'rb') as fp:
        b = fp.read()
    crlf = b.count(b'\r\n')
    lf = b.count(b'\n') - crlf
    print(f, 'CRLF:', crlf, 'LF:', lf)
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', 'rb') as f:
    b = f.read()
crlf = b.count(b'\r\n')
lf = b.count(b'\n') - crlf
print('CRLF:', crlf)
print('LF only:', lf)
print('Total bytes:', len(b))
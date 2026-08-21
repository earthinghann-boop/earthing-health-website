with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html', 'rb') as f:
    raw = f.read()
print('size:', len(raw))
print('has .gb-carousel-dots:', b'.gb-carousel-dots' in raw)
print('has left: 16px:', b'left: 16px' in raw)
idx = raw.find(b'carousel-dots')
print('carousel-dots at byte:', idx)
if idx >= 0:
    print(repr(raw[idx-5:idx+500]))
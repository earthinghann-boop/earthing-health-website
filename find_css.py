with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', 'rb') as f:
    text = f.read().decode('utf-8')
idx = text.find('.gb-carousel-dots')
print('Dots CSS start at:', idx)
if idx >= 0:
    print('---context---')
    print(repr(text[idx:idx+600]))
print()
print('=== btn CSS ===')
idx2 = text.find('.gb-carousel-btn {')
print('Btn CSS start at:', idx2)
if idx2 >= 0:
    print(repr(text[idx2:idx2+500]))
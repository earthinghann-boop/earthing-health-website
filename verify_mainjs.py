with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', 'rb') as f:
    t = f.read().decode('utf-8')
print('main.js ref:', t.count('js/main.js'))
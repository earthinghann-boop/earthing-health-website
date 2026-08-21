with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', 'rb') as f:
    t = f.read().decode('utf-8')

print('main.js ref:', t.count('js/main.js'))
print('total scripts:', t.count('<script'))
print()
i = t.find('<script')
print('First script area:')
print(t[max(0,i-30):i+200])
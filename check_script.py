with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', 'rb') as f:
    t = f.read().decode('utf-8')

i = t.find('/* Grounding Bedding')
print('GB script at:', i)
print(t[max(0,i-200):i+50])
print('---')
print('total <script> tags:', t.count('<script>'))
print('main.js refs:', t.count('main.js'))
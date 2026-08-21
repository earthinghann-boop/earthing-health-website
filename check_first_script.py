with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', 'rb') as f:
    t = f.read().decode('utf-8')

i = t.find('<script>')
print('First <script> at:', i)
print(t[max(0,i-100):i+500])
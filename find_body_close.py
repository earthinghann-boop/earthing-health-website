with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', 'rb') as f:
    t = f.read().decode('utf-8')

# Find </body> and the line before it
i = t.rfind('</body>')
print('Bytes before </body>:', t[:i][-200:])
print()
print('--- ---')
print(t[i:i+50])
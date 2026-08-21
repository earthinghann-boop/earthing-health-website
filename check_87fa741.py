import subprocess, re

# 1) HEAD 提交里 index.html 的 blob
r = subprocess.run(['git', 'show', '87fa741:index.html'], capture_output=True, text=True, cwd=r'C:\Users\18574\.qclaw\workspace\earthinghealth-website', encoding='utf-8', errors='replace')
head_text = r.stdout
print('=== HEAD (87fa741) index.html ===')
print('size:', len(head_text))
print('earthing-fitted-sheet count:', len(re.findall(r'earthing-fitted-sheet', head_text)))
print('groundingbedding count:', len(re.findall(r'groundingbedding', head_text)))
print()

# 2) 磁盘实际
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\index.html', 'rb') as f:
    disk_text = f.read().decode('utf-8')
print('=== DISK index.html ===')
print('size:', len(disk_text))
print('earthing-fitted-sheet count:', len(re.findall(r'earthing-fitted-sheet', disk_text)))
print('groundingbedding count:', len(re.findall(r'groundingbedding', disk_text)))
print()

# 3) 上一版 HEAD~1 (before 87fa741)
r2 = subprocess.run(['git', 'show', 'HEAD~1:index.html'], capture_output=True, text=True, cwd=r'C:\Users\18574\.qclaw\workspace\earthinghealth-website', encoding='utf-8', errors='replace')
prev_text = r2.stdout
print('=== HEAD~1 (before 87fa741) index.html ===')
print('size:', len(prev_text))
print('earthing-fitted-sheet count:', len(re.findall(r'earthing-fitted-sheet', prev_text)))
print('groundingbedding count:', len(re.findall(r'groundingbedding', prev_text)))

import subprocess, difflib

r = subprocess.run(['git', 'show', '87fa741:index.html'], capture_output=True, text=True, cwd=r'C:\Users\18574\.qclaw\workspace\earthinghealth-website', encoding='utf-8', errors='replace')
head_text = r.stdout

with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\index.html', 'rb') as f:
    disk_text = f.read().decode('utf-8')

# Find lines that differ
head_lines = head_text.splitlines()
disk_lines = disk_text.splitlines()

# Use unified diff
diff = list(difflib.unified_diff(head_lines, disk_lines, lineterm='', n=1))
print('=== Diff (disk vs HEAD) ===')
print('Total diff lines:', len(diff))
for line in diff[:40]:
    print(line)
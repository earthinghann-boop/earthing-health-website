#!/usr/bin/env python3
import re

path = 'earthing-fitted-sheet.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the entire intro carousel IIFE block
pattern = r'\n\n        // Intro carousel \(4 images\)\n        \(function\(\) \{[\s\S]*?\}\)\(\);'
new_content, n = re.subn(pattern, '\n\n        // Intro carousel removed (HTML section deleted)', content)

print(f'Replacements made: {n}')
print(f'Old size: {len(content)}, New size: {len(new_content)}')

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Verify
with open(path, 'r', encoding='utf-8') as f:
    verify = f.read()
print(f"goFittedIntroSlide refs: {len(re.findall('goFittedIntroSlide', verify))}")
target = 'Intro carousel \\(4 images\\)'
print(f'Intro carousel (4 images) refs: {len(re.findall(target, verify))}')
print(f"Product Introduction refs: {len(re.findall('Product Introduction', verify))}")
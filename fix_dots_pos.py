#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix dot container position in pu-earthing-mat.html inline <style>:
- Change .gb-carousel-dots { left: 16px; ... padding: 10px 6px; border-radius: 20px; }
  to:                                  left: 0;   ... padding: 10px 10px 10px 14px; border-radius: 0 20px 20px 0;
This fixes the offset between dots background box and actual clickable dot area.
"""
import re

path = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\pu-earthing-mat.html'
with open(path, 'rb') as f:
    raw = f.read()

# The style block has 7x CRLF padding. Let's find and replace the specific bytes.
# Looking for:  .gb-carousel-dots { ... left: 16px ... padding: 10px 6px ... border-radius: 20px; }
# We need to normalize the newlines for safe replacement.

# Strategy: read as text (handles CRLF), do string replacement
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# The padding-before pattern is: multiple CRLF combinations
# Let's just do targeted replacements

old1 = 'left: 16px;'
new1 = 'left: 0;'
old2 = 'padding: 10px 6px;'
new2 = 'padding: 10px 10px 10px 14px;'
old3 = 'border-radius: 20px;'
new3 = 'border-radius: 0 20px 20px 0;'

# Count occurrences before replacing
print('Before:')
print('  left: 16px occurrences:', content.count(old1))
print('  padding: 10px 6px occurrences:', content.count(old2))
print('  border-radius: 20px occurrences:', content.count(old3))

new_content = content
new_content = new_content.replace(old1, new1, 1)  # only first occurrence (in .gb-carousel-dots)
new_content = new_content.replace(old2, new2, 1)
new_content = new_content.replace(old3, new3, 1)

print('After:')
print('  left: 16px:', new_content.count(old1))
print('  left: 0;:', new_content.count(new1))
print('  padding: 10px 10px 10px 14px;:', new_content.count(new2))
print('  border-radius: 0 20px 20px 0;:', new_content.count(new3))

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Written. New size:', len(new_content))
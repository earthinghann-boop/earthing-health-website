with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', 'rb') as f:
    gb = f.read().decode('utf-8')

import re

# Extract CSS
m = re.search(r'<style>(.*?)</style>', gb, re.DOTALL)
css = m.group(1) if m else ''

# Extract inline carousel script
# It should be the one starting with (function() and containing CAROUSELS
m2 = re.search(r"<script>\s*\(function\(\)\s*\{.*?\}\)\(\);?\s*</script>", gb, re.DOTALL)
script = m2.group() if m2 else ''
print('CSS len:', len(css))
print('Script len:', len(script))
print()
print('--- first 500 of script ---')
print(script[:500])
print()
print('--- last 500 of script ---')
print(script[-500:])
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', 'rb') as f:
    t = f.read().decode('utf-8')

import re
m = re.search(r'<style>(.*?)</style>', t, re.DOTALL)
if m:
    with open(r'C:\Users\18574\.qclaw\workspace\earthingbedding_style.css', 'w', encoding='utf-8') as fp:
        fp.write(m.group(1))
    print('Style saved')

# Find body
m_body = re.search(r'<body[^>]*>(.*?)</body>', t, re.DOTALL)
if m_body:
    with open(r'C:\Users\18574\.qclaw\workspace\earthingbedding_body.html', 'w', encoding='utf-8') as fp:
        fp.write(m_body.group(1))
    print('Body saved')

# Find inline script (the one after </footer>)
m_script = re.search(r"<script>\(function\(\).*?</script>", t, re.DOTALL)
if m_script:
    with open(r'C:\Users\18574\.qclaw\workspace\earthingbedding_script.js', 'w', encoding='utf-8') as fp:
        fp.write(m_script.group())
    print('Inline script saved')
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html', 'rb') as f:
    t = f.read().decode('utf-8')

# Find CSS that we need to replicate
import re
m = re.search(r'<style>(.*?)</style>', t, re.DOTALL)
if m:
    print('Style block length:', len(m.group(1)))
    print()

# Count category sections
print('gb-category-section count:', t.count('class="gb-category-section'))
print('gb-carousel count:', t.count('class="gb-carousel"'))
print('gb-carousel-img count:', t.count('gb-carousel-img'))
print('window.goGB = goGB:', t.count('window.goGB = goGB'))
print('CAROUSELS = [] count:', t.count('CAROUSELS = ['))
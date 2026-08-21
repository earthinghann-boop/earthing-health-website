import os, re

p = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\groundingbedding.html'
with open(p, 'rb') as f:
    text = f.read().decode('utf-8')

# ============ Step 1: Replace CSS dots block (use regex tolerant to \r\r\n) ============
old_dots_pattern = re.compile(
    r'\.gb-carousel-dots\s*\{[^}]+\}\s*'          # .gb-carousel-dots { ... }
    r'\.gb-carousel-dot\s*\{[^}]+\}\s*'             # .gb-carousel-dot { ... }
    r'\.gb-carousel-dot\.active\s*\{[^}]+\}',       # .gb-carousel-dot.active { ... }
    re.DOTALL
)

new_dots_css = (
    '.gb-carousel-dots {\r\n'
    '            position: absolute;\r\n'
    '            left: 16px;\r\n'
    '            top: 50%;\r\n'
    '            transform: translateY(-50%);\r\n'
    '            display: flex;\r\n'
    '            flex-direction: column;\r\n'
    '            gap: 12px;\r\n'
    '            z-index: 3;\r\n'
    '            background: rgba(0,0,0,0.35);\r\n'
    '            padding: 10px 6px;\r\n'
    '            border-radius: 20px;\r\n'
    '        }\r\n'
    '        .gb-carousel-dot {\r\n'
    '            width: 10px; height: 10px;\r\n'
    '            border-radius: 50%;\r\n'
    '            background: rgba(255,255,255,0.5);\r\n'
    '            cursor: pointer;\r\n'
    '            border: none;\r\n'
    '            padding: 0;\r\n'
    '            transition: background 0.3s, transform 0.3s;\r\n'
    '        }\r\n'
    '        .gb-carousel-dot:hover { background: rgba(255,255,255,0.8); }\r\n'
    '        .gb-carousel-dot.active { background: #ffffff; transform: scale(1.3); }'
)

m = old_dots_pattern.search(text)
if m:
    text = text[:m.start()] + new_dots_css + text[m.end():]
    print('[OK] CSS dots block replaced (regex match)')
else:
    print('[FAIL] CSS dots block NOT found')

# ============ Step 2: Remove arrow buttons ============
# Use tolerant regex matching any whitespace
prev_pat = re.compile(r'<button class="gb-carousel-btn gb-carousel-prev"[^>]*>[^<]*</button>\s*', re.DOTALL)
next_pat = re.compile(r'<button class="gb-carousel-btn gb-carousel-next"[^>]*>[^<]*</button>\s*', re.DOTALL)

prev_count = len(prev_pat.findall(text))
next_count = len(next_pat.findall(text))
text = prev_pat.sub('', text)
text = next_pat.sub('', text)
print('[OK] Removed', prev_count, 'prev buttons and', next_count, 'next buttons')

# ============ Step 3: Replace btn CSS (tolerant) ============
old_btn_pattern = re.compile(
    r'\.gb-carousel-btn\s*\{[^}]+\}\s*'
    r'\.gb-carousel-btn:hover\s*\{[^}]+\}\s*'
    r'\.gb-carousel-prev\s*\{[^}]+\}\s*'
    r'\.gb-carousel-next\s*\{[^}]+\}',
    re.DOTALL
)
new_btn_css = '.gb-carousel-btn { display: none; }'

m2 = old_btn_pattern.search(text)
if m2:
    text = text[:m2.start()] + new_btn_css + text[m2.end():]
    print('[OK] CSS btn block replaced (regex match)')
else:
    print('[FAIL] CSS btn block NOT found')

# ============ Step 4: Fix dot click bug - expose goGB to window ============
old_js_pattern = re.compile(
    r'<script>\s*'
    r'\(function\(\)\s*\{.*?\}\)\(\);\s*'
    r'</script>',
    re.DOTALL
)

# Use a more reliable approach - find the exact known start
start_marker = '<script>'
end_marker = '</script>'
si = text.find(start_marker)
ei = text.find(end_marker, si)
if si >= 0 and ei >= 0:
    old_block = text[si:ei + len(end_marker)]
    new_block = '''<script>
(function(){
    var CAROUSELS = ['fittedCarousel','flatCarousel','pillowCarousel','duvetCarousel','kidsCarousel'];
    var timers = {};
    var current = {};

    function goGB(id, n) {
        var imgs = document.querySelectorAll('#' + id + ' .gb-carousel-img');
        var dots = document.querySelectorAll('#' + id + ' .gb-carousel-dot');
        if (!imgs.length) return;
        imgs.forEach(function(img){ img.classList.remove('active'); });
        dots.forEach(function(dot){ dot.classList.remove('active'); });
        current[id] = n;
        if (imgs[n]) imgs[n].classList.add('active');
        if (dots[n]) dots[n].classList.add('active');
        clearInterval(timers[id]);
        timers[id] = setInterval(function(){ autoNext(id); }, 3500);
    }

    function moveGB(id, dir) {
        var imgs = document.querySelectorAll('#' + id + ' .gb-carousel-img');
        var next = ((current[id] || 0) + dir + imgs.length) % imgs.length;
        goGB(id, next);
    }

    function autoNext(id) {
        var imgs = document.querySelectorAll('#' + id + ' .gb-carousel-img');
        var next = ((current[id] || 0) + 1) % imgs.length;
        goGB(id, next);
    }

    function initGB(id) {
        current[id] = 0;
        var el = document.getElementById(id);
        if (!el) return;
        el.addEventListener('mouseenter', function(){ clearInterval(timers[id]); });
        el.addEventListener('mouseleave', function(){ timers[id] = setInterval(function(){ autoNext(id); }, 3500); });
        timers[id] = setInterval(function(){ autoNext(id); }, 3500);
    }

    // Expose to global scope so onclick=\"goGB(...)\" inline handlers can find them
    window.goGB = goGB;
    window.moveGB = moveGB;

    CAROUSELS.forEach(initGB);
})();
</script>'''
    text = text[:si] + new_block + text[ei + len(end_marker):]
    print('[OK] JS block replaced (window.goGB exposed)')
else:
    print('[FAIL] JS block NOT found')

# ============ Write back ============
with open(p, 'w', encoding='utf-8') as f:
    f.write(text)

print()
print('New file size:', os.path.getsize(p), 'bytes')
print()
print('=== Verify ===')
for keyword in ['window.goGB = goGB', 'flex-direction: column', 'left: 16px', 'display: none']:
    cnt = text.count(keyword)
    print(' [', 'OK' if cnt > 0 else 'MISS', ']', cnt, 'x', repr(keyword))

print()
print('Prev arrows remaining:', text.count('gb-carousel-prev'))
print('Next arrows remaining:', text.count('gb-carousel-next'))
print('Btn CSS classes still in DOM (img tags):', text.count('class="gb-carousel-img'))
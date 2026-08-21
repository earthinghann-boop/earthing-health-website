import re

with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-mat.html', encoding='utf-8') as f:
    html = f.read()

print(f"Before: {len(html):,} chars")

# ── 1. Replace goGB function with one that detects dot vs prev/next ──
# If n is between 0 and (total-1), treat as absolute dot-jump
# If n is ±1, treat as prev/next (relative)
old_fn = '''function goGB(id, n) {
            var c = document.getElementById(id);
            if (!c) return;
            var imgs = c.querySelectorAll('.gb-carousel-img');
            var dots = c.querySelectorAll('.gb-carousel-dot');
            var total = imgs.length;
            var cur = 0;
            for (var i = 0; i < total; i++) {
                if (imgs[i].classList.contains('active')) { cur = i; break; }
            }
            var next = (cur + n + total) % total;
            imgs[cur].classList.remove('active');
            dots[cur].classList.remove('active');
            imgs[next].classList.add('active');
            dots[next].classList.add('active');
            var t = timers[id];
            if (t) { clearInterval(t); }
            timers[id] = setInterval(function() { goGB(id, 1); }, 3500);
        }'''

new_fn = '''function goGB(id, n) {
            var c = document.getElementById(id);
            if (!c) return;
            var imgs = c.querySelectorAll('.gb-carousel-img');
            var dots = c.querySelectorAll('.gb-carousel-dot');
            var total = imgs.length;
            var cur = 0;
            for (var i = 0; i < total; i++) {
                if (imgs[i].classList.contains('active')) { cur = i; break; }
            }
            var next;
            // If n is a small non-negative integer < total, treat as absolute dot index
            // Otherwise treat as relative offset (±1 for prev/next buttons)
            if (n >= 0 && n < total) {
                next = n;
            } else {
                next = (cur + n + total) % total;
            }
            imgs[cur].classList.remove('active');
            dots[cur].classList.remove('active');
            imgs[next].classList.add('active');
            dots[next].classList.add('active');
            var t = timers[id];
            if (t) { clearInterval(t); }
            timers[id] = setInterval(function() { goGB(id, 1); }, 3500);
        }'''

if old_fn in html:
    html = html.replace(old_fn, new_fn, 1)
    print("Replaced goGB function")
else:
    # Show what's actually there
    pos = html.find('function goGB')
    print(f"old_fn NOT found. goGB at {pos}:")
    print(repr(html[pos:pos+400]))

print(f"After: {len(html):,} chars")

# ── Save ──────────────────────────────────────────────────────────
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-mat.html', 'w', encoding='utf-8') as f:
    f.write(html)

# ── Verify ────────────────────────────────────────────────────────
with open(r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\grounding-mat.html', encoding='utf-8') as f:
    chk = f.read()

pos = chk.find('function goGB')
print("\n=== New goGB function ===")
print(chk[pos:pos+700])

print("\n=== Dot onclick handlers ===")
dots = re.findall(r'onclick="goGB\([^"]+"', chk)
for d in dots:
    print(f"  {d}")
print(f"Total: {len(dots)}")

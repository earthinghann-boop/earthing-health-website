"""
Patch get-price.html:
1. Replace .gp-hero background (gradient → factory-hero.jpg)
2. Add background-size, background-position, blur effect
3. Add text-protection dark overlay so white text stays readable
4. Keep size/padding EXACTLY the same
"""
import sys; sys.stdout.reconfigure(encoding='utf-8')

gp = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website\get-price.html'
html = open(gp, 'r', encoding='utf-8').read()

# ── Patch .gp-hero CSS ────────────────────────────────────────────────────
old_hero_css = '''        .gp-hero {
            background: linear-gradient(135deg, #3a5c2e 0%, #5a7c45 50%, #6b8c55 100%);
            padding: 60px 40px 70px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }'''

new_hero_css = '''        .gp-hero {
            /* Real factory photo with built-in blur effect */
            background:
                linear-gradient(rgba(40, 50, 35, 0.55), rgba(40, 50, 35, 0.55)),
                url("images/factory-hero.jpg") center 35% / cover no-repeat;
            /* Apply heavy blur to the background image only (kept behind the overlay) */
            filter: blur(0px); /* no filter here — pseudo-element does the blurring */
            padding: 60px 40px 70px;
            text-align: center;
            position: relative;
            overflow: hidden;
            isolation: isolate;
        }
        .gp-hero::before {
            /* the original decorative cross pattern — kept but darker */
            content: '';
            position: absolute;
            inset: 0;
            background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
            z-index: 1;
        }
        .gp-hero::after {
            /* separate blurred background layer so blur does not affect text */
            content: '';
            position: absolute;
            inset: -10px;
            background: url("images/factory-hero.jpg") center 35% / cover no-repeat;
            filter: blur(6px);
            z-index: 0;
        }
        .gp-hero > * { position: relative; z-index: 2; }'''

if old_hero_css in html:
    html = html.replace(old_hero_css, new_hero_css, 1)
    print('✅ Replaced .gp-hero CSS')
else:
    print('❌ Pattern not found!')
    sys.exit(1)

# ── Bump heading text-shadow for legibility over photo ───────────────────
old_h1 = '''        .gp-hero h1 {
            font-family: 'Playfair Display', serif; font-size: 48px; font-weight: 700;
            color: #fff; margin-bottom: 14px; line-height: 1.15;
        }'''
new_h1 = '''        .gp-hero h1 {
            font-family: 'Playfair Display', serif; font-size: 48px; font-weight: 700;
            color: #fff; margin-bottom: 14px; line-height: 1.15;
            text-shadow: 0 2px 16px rgba(0,0,0,0.45), 0 1px 2px rgba(0,0,0,0.3);
        }'''
if old_h1 in html:
    html = html.replace(old_h1, new_h1, 1)
    print('✅ Added text-shadow to h1')

old_p = '''        .gp-hero p { font-size: 17px; color: rgba(255,255,255,0.82); max-width: 520px; margin: 0 auto; }'''
new_p = '''        .gp-hero p { font-size: 17px; color: rgba(255,255,255,0.88); max-width: 520px; margin: 0 auto; text-shadow: 0 1px 8px rgba(0,0,0,0.4); }'''
if old_p in html:
    html = html.replace(old_p, new_p, 1)
    print('✅ Added text-shadow to p')

# Make the label stand out more over photo
old_label = '''        .gp-hero-label {
            display: inline-block; background: rgba(255,255,255,0.15);
            border: 1px solid rgba(255,255,255,0.3); color: rgba(255,255,255,0.9);
            font-size: 12px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;
            padding: 5px 16px; border-radius: 30px; margin-bottom: 18px;
        }'''
new_label = '''        .gp-hero-label {
            display: inline-block; background: rgba(255,255,255,0.18);
            border: 1px solid rgba(255,255,255,0.4); color: #fff;
            font-size: 12px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;
            padding: 5px 16px; border-radius: 30px; margin-bottom: 18px;
            backdrop-filter: blur(4px);
        }'''
if old_label in html:
    html = html.replace(old_label, new_label, 1)
    print('✅ Upgraded hero-label for photo background')

open(gp, 'w', encoding='utf-8').write(html)
print('\nDone — get-price.html patched, factory-hero.jpg ready')

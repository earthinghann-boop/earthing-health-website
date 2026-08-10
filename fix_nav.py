"""
1. Remove OEM/ODM from index.html nav
2. Rewrite get-price.html with matching nav (logo + same links + same style.css)
"""
import sys; sys.stdout.reconfigure(encoding='utf-8')
import re, os

WS = r'C:\Users\18574\.qclaw\workspace\earthinghealth-website'

# ── Step 1: Fix index.html ──────────────────────────────────────────────────
idx_html = open(f'{WS}\\index.html', 'r', encoding='utf-8').read()

old_nav = '<li><a href="#oem">OEM/ODM</a></li>\n                <li><a href="#contact">Contact</a></li>\n                <li><a href="get-price.html">Get Price</a></li>'
new_nav = '<li><a href="#contact">Contact</a></li>\n                <li><a href="get-price.html" class="nav-cta">Get Price</a></li>'

if old_nav not in idx_html:
    print('WARNING: OEM nav pattern not found in index.html')
    print(repr(idx_html[idx_html.find('oem')-50:idx_html.find('oem')+100]))
else:
    idx_html = idx_html.replace(old_nav, new_nav, 1)
    open(f'{WS}\\index.html', 'w', encoding='utf-8').write(idx_html)
    print('✅ index.html nav updated (OEM/ODM removed)')

# ── Step 2: Rewrite get-price.html ─────────────────────────────────────────
gp_path = f'{WS}\\get-price.html'

# Read the existing file to get the calc-body content and script
gp = open(gp_path, 'r', encoding='utf-8').read()

# Extract the calculator section (everything from calc-card to before gp-cta-strip)
calc_start = gp.find('<div class="calc-card">')
calc_end   = gp.find('<section class="gp-cta-strip">')
calc_section = gp[calc_start:calc_end]

# Extract script block
script_start = gp.find('<script>')
script_end   = gp.find('</script>', script_start) + len('</script>')
script_block  = gp[script_start:script_end]

# Build the complete new page
new_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Price — EARTHING</title>
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Playfair+Display:wght@500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    <style>
        /* ── Page-level overrides for get-price ──────────────────────────── */
        body {{ overflow-x: hidden; }}

        /* Hero banner */
        .gp-hero {{
            background: linear-gradient(135deg, #3a5c2e 0%, #5a7c45 50%, #6b8c55 100%);
            padding: 60px 40px 70px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }}
        .gp-hero::before {{
            content: '';
            position: absolute; inset: 0;
            background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.04'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
        }}
        .gp-hero-label {{
            display: inline-block; background: rgba(255,255,255,0.15);
            border: 1px solid rgba(255,255,255,0.3); color: rgba(255,255,255,0.9);
            font-size: 12px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;
            padding: 5px 16px; border-radius: 30px; margin-bottom: 18px;
        }}
        .gp-hero h1 {{
            font-family: 'Playfair Display', serif; font-size: 48px; font-weight: 700;
            color: #fff; margin-bottom: 14px; line-height: 1.15;
        }}
        .gp-hero p {{ font-size: 17px; color: rgba(255,255,255,0.82); max-width: 520px; margin: 0 auto; }}

        /* ── Calculator ─────────────────────────────────────────────────── */
        .gp-calculator {{
            max-width: 820px; margin: -40px auto 60px; padding: 0 20px; position: relative; z-index: 10;
        }}
        .calc-card {{
            background: #fff; border-radius: 20px;
            box-shadow: 0 8px 40px rgba(0,0,0,0.12); overflow: hidden;
        }}
        .calc-header {{
            background: linear-gradient(135deg, #3a5c2e, #4a6b3a);
            padding: 26px 36px; display: flex; align-items: center; gap: 14px;
        }}
        .calc-header-icon {{
            width: 44px; height: 44px; background: rgba(255,255,255,0.2);
            border-radius: 10px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;
        }}
        .calc-header-icon svg {{ color: #fff; }}
        .calc-header h2 {{ font-family: 'Playfair Display', serif; font-size: 22px; color: #fff; }}
        .calc-header h2 span {{ color: #d4ad3a; }}
        .calc-header p {{ font-size: 13px; color: rgba(255,255,255,0.72); margin-top: 2px; }}

        .calc-body {{ padding: 36px; }}

        .form-grid {{
            display: grid; grid-template-columns: 1fr 1fr; gap: 20px;
        }}
        .form-group {{ display: flex; flex-direction: column; }}
        .form-group.full-width {{ grid-column: 1 / -1; }}
        .form-group label {{
            font-size: 12px; font-weight: 700; color: #55553a;
            letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 7px;
        }}
        .form-group label .req {{ color: #b8902a; margin-left: 2px; }}
        .form-select, .form-input {{
            width: 100%; padding: 11px 16px; border: 1.5px solid #e0dbd0;
            border-radius: 8px; font-family: 'Nunito', sans-serif; font-size: 15px;
            color: #2c2c1e; background: #fff; transition: border-color 0.2s, box-shadow 0.2s;
            appearance: none; -webkit-appearance: none; cursor: pointer;
        }}
        .form-select {{
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%238a8870' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
            background-repeat: no-repeat; background-position: right 14px center; padding-right: 38px;
        }}
        .form-select:focus, .form-input:focus {{
            outline: none; border-color: #4a6b3a; box-shadow: 0 0 0 3px rgba(74,107,58,0.12);
        }}
        .form-input::placeholder {{ color: #b0aa98; }}
        .input-hint {{ font-size: 12px; color: #8a8870; margin-top: 5px; }}

        .price-display {{
            margin-top: 28px; padding: 22px 28px;
            background: linear-gradient(135deg, #f0ede5, #f8f5ef);
            border: 2px solid #e0dbd0; border-radius: 14px; text-align: center;
            min-height: 105px; display: flex; flex-direction: column;
            align-items: center; justify-content: center; transition: all 0.3s ease;
        }}
        .price-display.active {{
            background: linear-gradient(135deg, #eef5ea, #f4faf2);
            border-color: #4a6b3a;
        }}
        .price-display .price-placeholder {{
            color: #8a8870; font-size: 15px;
        }}
        .price-display .price-placeholder svg {{
            display: block; margin: 0 auto 10px; opacity: 0.4;
        }}
        .price-display.active .price-label {{
            font-size: 11px; font-weight: 700; letter-spacing: 1.5px;
            text-transform: uppercase; color: #4a6b3a; margin-bottom: 6px;
        }}
        .price-display.active .price-amount {{
            font-family: 'Playfair Display', serif; font-size: 38px; font-weight: 700;
            color: #3a5c2e; line-height: 1;
        }}
        .price-display.active .price-unit {{
            font-size: 14px; color: #8a8870; margin-top: 4px;
        }}
        .price-display.active .price-tier {{
            display: inline-block; background: #3a5c2e; color: #fff;
            font-size: 11px; font-weight: 700; letter-spacing: 1px;
            padding: 3px 12px; border-radius: 20px; margin-top: 8px;
        }}

        .tier-guide {{
            margin-top: 24px; padding-top: 24px; border-top: 1px solid #e0dbd0;
        }}
        .tier-guide h4 {{
            font-size: 12px; font-weight: 700; color: #55553a;
            letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 12px;
        }}
        .tier-table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
        .tier-table th {{
            background: #eee8dc; padding: 8px 12px; text-align: left;
            font-weight: 700; color: #55553a; font-size: 11px;
            text-transform: uppercase; letter-spacing: 0.5px;
        }}
        .tier-table td {{
            padding: 7px 12px; border-bottom: 1px solid #e0dbd0; color: #2c2c1e;
        }}
        .tier-table tr:last-child td {{ border-bottom: none; }}
        .tier-table .tier-highlight {{ background: #f4faf2; }}
        .tier-table .tier-badge {{
            display: inline-block; padding: 2px 8px; border-radius: 10px;
            font-size: 11px; font-weight: 700;
        }}
        .tier-badge.gold {{ background: #fdf3d0; color: #8a6c34; }}
        .tier-badge.green {{ background: #eef5ea; color: #3a5c2e; }}
        .tier-badge.blue {{ background: #e8f0fa; color: #3a5c8c; }}

        .calc-disclaimer {{
            margin-top: 16px; font-size: 12px; color: #8a8870; text-align: center; line-height: 1.6;
        }}

        /* ── CTA ────────────────────────────────────────────────────────── */
        .gp-cta-strip {{
            background: #eee8dc; border-top: 1px solid #e0dbd0;
            border-bottom: 1px solid #e0dbd0; padding: 50px 40px; text-align: center;
        }}
        .gp-cta-strip h3 {{ font-family: 'Playfair Display', serif; font-size: 28px; color: #2c2c1e; margin-bottom: 10px; }}
        .gp-cta-strip p {{ font-size: 15px; color: #8a8870; margin-bottom: 24px; }}
        .btn-primary {{
            display: inline-block; background: #4a6b3a; color: #fff;
            padding: 14px 36px; border-radius: 30px; font-size: 15px; font-weight: 700;
            text-decoration: none; letter-spacing: 0.3px; transition: background 0.2s, transform 0.2s, box-shadow 0.2s;
            border: none; cursor: pointer;
        }}
        .btn-primary:hover {{ background: #3a5c2e; transform: translateY(-1px); box-shadow: 0 6px 20px rgba(74,107,58,0.3); }}

        /* ── Footer ─────────────────────────────────────────────────────── */
        .site-footer {{ background: #3a5c2e; color: rgba(255,255,255,0.7); padding: 40px; text-align: center; font-size: 13px; }}
        .site-footer a {{ color: rgba(255,255,255,0.7); text-decoration: none; }}
        .site-footer a:hover {{ color: #fff; }}

        /* ── Responsive ──────────────────────────────────────────────────── */
        @media (max-width: 680px) {{
            .gp-hero h1 {{ font-size: 34px; }}
            .form-grid {{ grid-template-columns: 1fr; }}
            .calc-body {{ padding: 22px 18px; }}
            .calc-header {{ padding: 20px 20px; }}
            .tier-table {{ font-size: 12px; }}
            .gp-cta-strip {{ padding: 36px 20px; }}
        }}
    </style>
</head>
<body>

<!-- Navigation — exact copy of index.html navbar -->
<nav class="navbar" id="navbar">
    <div class="nav-container">
        <a href="index.html" class="logo">
            <img src="images/logo/earthing-logo.png" alt="EARTHING Logo">
        </a>
        <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Toggle menu">
            <span></span><span></span><span></span>
        </button>
        <ul class="nav-links" id="navLinks">
            <li><a href="index.html#home">Home</a></li>
            <li><a href="index.html#about">About</a></li>
            <li><a href="index.html#products">Products</a></li>
            <li><a href="index.html#technology">Technology</a></li>
            <li><a href="index.html#contact">Contact</a></li>
            <li><a href="get-price.html" class="nav-cta">Get Price</a></li>
        </ul>
    </div>
</nav>

<!-- Hero -->
<section class="gp-hero">
    <div class="gp-hero-label">Factory Direct Estimate</div>
    <h1>Get an Instant<br>Earthing Product Estimate</h1>
    <p>Select your product specifications and order quantity to view the applicable EXW tier pricing.</p>
</section>

<!-- Calculator -->
<div class="gp-calculator">
    <div class="calc-card">
        <div class="calc-header">
            <div class="calc-header-icon">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                    <rect x="2" y="3" width="20" height="14" rx="2"/>
                    <line x1="8" y1="21" x2="16" y2="21"/>
                    <line x1="12" y1="17" x2="12" y2="21"/>
                </svg>
            </div>
            <div>
                <h2>Product <span>Estimate</span></h2>
                <p>Online estimates available from 11 to 1,000 pieces per order</p>
            </div>
        </div>

        <div class="calc-body">
            <div class="form-grid">
                <div class="form-group">
                    <label>Product <span class="req">*</span></label>
                    <select class="form-select" id="productSelect" onchange="updateSizes()">
                        <option value="">Select a product</option>
                        <option value="fitted-sheet">Fitted Sheet (Bed Sheet)</option>
                        <option value="mattress-pad">Mattress Pad / Mat</option>
                        <option value="pillowcase">Pillowcase</option>
                        <option value="half-sheet">Half Sheet / Flat Sheet</option>
                        <option value="grounding-cord">Grounding Cord</option>
                        <option value="laundry-bag">Silver Fiber Laundry Bag</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Size / Specification <span class="req">*</span></label>
                    <select class="form-select" id="sizeSelect" onchange="calculatePrice()" disabled>
                        <option value="">Select a product first</option>
                    </select>
                </div>
                <div class="form-group full-width">
                    <label>Quantity (pcs) <span class="req">*</span></label>
                    <input type="number" class="form-input" id="qtyInput"
                           placeholder="Enter quantity (11 – 1,000 pcs)"
                           min="11" max="1000" value=""
                           oninput="calculatePrice()">
                    <p class="input-hint">Online estimates are available from 11 to 1,000 pieces per order</p>
                </div>
            </div>

            <div class="price-display" id="priceDisplay">
                <div class="price-placeholder">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                        <circle cx="12" cy="12" r="10"/>
                        <line x1="12" y1="8" x2="12" y2="12"/>
                        <line x1="12" y1="16" x2="12.01" y2="16"/>
                    </svg>
                    Complete the selections above to view your applicable wholesale tier.
                </div>
            </div>

            <div class="tier-guide">
                <h4>Wholesale Pricing Tiers (EXW, per piece)</h4>
                <table class="tier-table">
                    <thead>
                        <tr><th>Quantity</th><th>Tier</th><th>Discount vs. Sample</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>11 – 50 pcs</td><td><span class="tier-badge gold">Standard</span></td><td>—</td></tr>
                        <tr class="tier-highlight"><td>51 – 200 pcs</td><td><span class="tier-badge green">Small Batch</span></td><td>5 – 8% off</td></tr>
                        <tr><td>201 – 500 pcs</td><td><span class="tier-badge blue">Medium Batch</span></td><td>10 – 15% off</td></tr>
                        <tr class="tier-highlight"><td>501 – 1,000 pcs</td><td><span class="tier-badge green">Large Batch</span></td><td>15 – 20% off</td></tr>
                    </tbody>
                </table>
            </div>

            <p class="calc-disclaimer">
                Prices shown are EXW (Ex Works) and for reference only — not final quotations.<br>
                Final pricing varies by material specifications, silver fiber content, customization requirements and current exchange rates.<br>
                Contact us for a formal PI with confirmed EXW / FOB / CIF terms.
            </p>
        </div>
    </div>
</div>

<!-- CTA -->
<section class="gp-cta-strip">
    <h3>Need a Formal Quotation?</h3>
    <p>Contact us for customization, branding options and all-inclusive pricing — we respond within 24 hours.</p>
    <a href="mailto:sale@groundingsafe.com" class="btn-primary">Send us an Inquiry →</a>
</section>

<!-- Footer -->
<footer class="site-footer">
    <p>© 2026 Guangzhou Earthing Health Technology Co., Ltd. &nbsp;|&nbsp; <a href="index.html">EARTHING.</a></p>
</footer>

{script_block}

</body>
</html>'''

open(gp_path, 'w', encoding='utf-8').write(new_page)
print('✅ get-price.html nav + style rewritten to match index.html')

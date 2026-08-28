var fs = require('fs');
var fp = 'css/style.css';
var css = fs.readFileSync(fp, 'utf8');
var before = css;

// Remove existing 3 mobile blocks
// Find each @media block and remove
var mobileBlocks = [];

// Pattern: @media (max-width: 768px) { ... }  (with flexible brace matching)
var i = 0;
while ((i = css.indexOf('@media', i)) >= 0) {
  var braceStart = css.indexOf('{', i);
  if (braceStart < 0) break;
  // Count braces to find matching close
  var depth = 1;
  var j = braceStart + 1;
  while (j < css.length && depth > 0) {
    if (css[j] === '{') depth++;
    else if (css[j] === '}') depth--;
    j++;
  }
  var block = css.substring(i, j);
  if (block.indexOf('max-width: 768px') >= 0) {
    mobileBlocks.push({ start: i, end: j, block: block });
  }
  i = j;
}

console.log('Found', mobileBlocks.length, 'mobile blocks to remove');
console.log('Total bytes to remove:', mobileBlocks.reduce(function(s, b) { return s + b.end - b.start; }, 0));

// Remove all (from end backwards to preserve indices)
mobileBlocks.reverse().forEach(function(b) {
  css = css.substring(0, b.start) + css.substring(b.end);
});

// Build the new consolidated mobile block
var newBlock = '\n/* ========== Mobile Fullscreen Redesign (max-width: 768px) ========== */\n'
  + '@media (max-width: 768px) {\n'
  // Common tokens
  + '    :root { --section-padding: 50px; }\n\n'

  // ====== 1. Fullscreen hamburger nav ======
  + '    /* Fullscreen hamburger menu */\n'
  + '    .navbar { padding: 12px 0; }\n'
  + '    .nav-container { padding: 0 16px; }\n'
  + '    .logo img { height: 32px; }\n'
  + '    .nav-links {\n'
  + '        position: fixed;\n'
  + '        top: 0;\n'
  + '        right: 0;\n'
  + '        left: auto;\n'
  + '        width: 100%;\n'
  + '        height: 100vh;\n'
  + '        height: 100dvh;\n'
  + '        background: var(--color-white);\n'
  + '        flex-direction: column;\n'
  + '        padding: 80px 28px 40px;\n'
  + '        gap: 0;\n'
  + '        transform: translateX(100%);\n'
  + '        transition: transform 0.35s ease;\n'
  + '        box-shadow: none;\n'
  + '        overflow-y: auto;\n'
  + '        z-index: 999;\n'
  + '    }\n'
  + '    .nav-links.active { transform: translateX(0); }\n'
  + '    .nav-links > li {\n'
  + '        width: 100%;\n'
  + '        border-bottom: 1px solid var(--color-border);\n'
  + '    }\n'
  + '    .nav-links > li > a {\n'
  + '        font-size: 1.15rem;\n'
  + '        padding: 18px 0;\n'
  + '        font-weight: 500;\n'
  + '        display: block;\n'
  + '    }\n'
  + '    .nav-cta {\n'
  + '        margin-top: 24px;\n'
  + '        border: none;\n'
  + '        text-align: center;\n'
  + '    }\n'
  + '    .nav-dropdown-menu {\n'
  + '        position: static;\n'
  + '        opacity: 1;\n'
  + '        visibility: visible;\n'
  + '        transform: none;\n'
  + '        box-shadow: none;\n'
  + '        border: none;\n'
  + '        padding: 0 0 12px 16px;\n'
  + '        min-width: 0;\n'
  + '        background: transparent;\n'
  + '        display: none;\n'
  + '    }\n'
  + '    .nav-dropdown.open .nav-dropdown-menu { display: block; }\n'
  + '    .nav-dropdown-menu a {\n'
  + '        padding: 10px 0;\n'
  + '        font-size: 0.95rem;\n'
  + '        opacity: 0.7;\n'
  + '        border: none;\n'
  + '    }\n'
  + '    .mobile-menu-btn { display: flex; z-index: 1001; }\n'
  + '    .mobile-menu-btn.active span:nth-child(1) { transform: rotate(45deg) translate(5px, 5px); }\n'
  + '    .mobile-menu-btn.active span:nth-child(2) { opacity: 0; }\n'
  + '    .mobile-menu-btn.active span:nth-child(3) { transform: rotate(-45deg) translate(5px, -5px); }\n'
  + '    .lang-switcher-item {\n'
  + '        margin-top: 24px;\n'
  + '        border: none;\n'
  + '        justify-content: flex-start;\n'
  + '    }\n'
  + '    .lang-switcher {\n'
  + '        margin: 0;\n'
  + '        padding: 0;\n'
  + '        gap: 12px;\n'
  + '    }\n'
  + '    .lang-switcher a, .lang-switcher span {\n'
  + '        font-size: 1rem;\n'
  + '        padding: 8px 14px;\n'
  + '    }\n\n'

  // ====== 2. Hero fullscreen immersive ======
  + '    /* Hero fullscreen immersive */\n'
  + '    .hero {\n'
  + '        min-height: 100vh;\n'
  + '        min-height: 100dvh;\n'
  + '        background: #FFFFFF;\n'
  + '        padding: 0;\n'
  + '    }\n'
  + '    .hero-bg {\n'
  + '        width: 100%;\n'
  + '        height: 100vh;\n'
  + '        height: 100dvh;\n'
  + '        top: 0;\n'
  + '        right: 0;\n'
  + '        bottom: auto;\n'
  + '        opacity: 1;\n'
  + '        -webkit-mask-image: linear-gradient(to bottom, rgba(0,0,0,0.5) 0%, rgba(0,0,0,0.4) 50%, rgba(0,0,0,0.85) 100%);\n'
  + '        mask-image: linear-gradient(to bottom, rgba(0,0,0,0.5) 0%, rgba(0,0,0,0.4) 50%, rgba(0,0,0,0.85) 100%);\n'
  + '        clip-path: none;\n'
  + '    }\n'
  + '    .hero-content {\n'
  + '        position: absolute;\n'
  + '        top: 0;\n'
  + '        left: 0;\n'
  + '        right: 0;\n'
  + '        bottom: auto;\n'
  + '        height: 100vh;\n'
  + '        height: 100dvh;\n'
  + '        padding: 90px 24px 32px;\n'
  + '        margin: 0;\n'
  + '        max-width: none;\n'
  + '        background: transparent;\n'
  + '        display: flex;\n'
  + '        flex-direction: column;\n'
  + '        justify-content: flex-end;\n'
  + '        text-align: left;\n'
  + '        z-index: 2;\n'
  + '    }\n'
  + '    .hero-text {\n'
  + '        max-width: 100%;\n'
  + '        margin: 0;\n'
  + '    }\n'
  + '    .hero-title {\n'
  + '        font-size: 2.2rem;\n'
  + '        line-height: 1.15;\n'
  + '        margin-bottom: 14px;\n'
  + '        color: var(--color-white);\n'
  + '        text-shadow: 0 2px 12px rgba(0,0,0,0.4);\n'
  + '    }\n'
  + '    .hero-subtitle {\n'
  + '        font-size: 0.95rem;\n'
  + '        line-height: 1.6;\n'
  + '        margin-bottom: 24px;\n'
  + '        color: rgba(255, 255, 255, 0.92);\n'
  + '        text-shadow: 0 1px 6px rgba(0,0,0,0.4);\n'
  + '    }\n'
  + '    .hero-cta {\n'
  + '        flex-direction: column;\n'
  + '        align-items: stretch;\n'
  + '        gap: 10px;\n'
  + '    }\n'
  + '    .hero-cta .btn {\n'
  + '        width: 100%;\n'
  + '        padding: 14px 24px;\n'
  + '        backdrop-filter: blur(8px);\n'
  + '    }\n'
  + '    .hero-cta .btn-primary {\n'
  + '        background: var(--color-white);\n'
  + '        color: var(--color-primary);\n'
  + '        border-color: var(--color-white);\n'
  + '    }\n'
  + '    .hero-cta .btn-outline {\n'
  + '        background: rgba(255, 255, 255, 0.15);\n'
  + '        color: var(--color-white);\n'
  + '        border-color: rgba(255, 255, 255, 0.7);\n'
  + '    }\n'
  + '    .scroll-indicator { display: none; }\n\n'

  // ====== 3. Section common ======
  + '    /* Section common */\n'
  + '    .section-header { margin-bottom: 30px; }\n'
  + '    .section-label { font-size: 0.75rem; margin-bottom: 8px; }\n'
  + '    .section-title { font-size: 1.7rem; line-height: 1.25; }\n'
  + '    .section-desc, .section-intro { font-size: 0.95rem; line-height: 1.6; }\n\n'

  // ====== 4. Story ======
  + '    /* Story section */\n'
  + '    .brand-story { padding: 50px 0; }\n'
  + '    .story-grid {\n'
  + '        grid-template-columns: 1fr;\n'
  + '        gap: 30px;\n'
  + '    }\n'
  + '    .story-text { order: 2; }\n'
  + '    .story-image { order: 1; }\n'
  + '    .story-title { font-size: 1.7rem; }\n'
  + '    .story-content p { font-size: 0.95rem; line-height: 1.7; }\n'
  + '    .story-stats {\n'
  + '        flex-direction: row;\n'
  + '        gap: 12px;\n'
  + '        flex-wrap: wrap;\n'
  + '        justify-content: space-between;\n'
  + '        padding-top: 24px;\n'
  + '    }\n'
  + '    .stat { flex: 1; min-width: 30%; }\n'
  + '    .stat-number { font-size: 1.8rem !important; }\n'
  + '    .stat-unit { font-size: 1rem !important; }\n'
  + '    .stat-label { font-size: 0.75rem; margin-top: 4px; }\n\n'

  // ====== 5. Video ======
  + '    /* Video */\n'
  + '    .video-grid { grid-template-columns: 1fr; gap: 24px; }\n'
  + '    .video-item iframe { aspect-ratio: 16/9; }\n\n'

  // ====== 6. Products ======
  + '    /* Products */\n'
  + '    .products { padding: 50px 0; }\n'
  + '    .products-grid, .products-grid-small { grid-template-columns: 1fr; gap: 24px; }\n'
  + '    .product-card { border-radius: 12px; overflow: hidden; }\n'
  + '    .product-image { aspect-ratio: 4/3; }\n'
  + '    .product-info { padding: 16px; }\n'
  + '    .product-info h3 { font-size: 1.05rem; }\n'
  + '    .product-desc { font-size: 0.9rem; line-height: 1.6; }\n'
  + '    .product-features li { font-size: 0.85rem; }\n\n'

  // ====== 7. Tech ======
  + '    /* Technology */\n'
  + '    .technology { padding: 50px 0; }\n'
  + '    .tech-grid { grid-template-columns: 1fr; gap: 20px; }\n'
  + '    .tech-card { padding: 24px 20px; }\n'
  + '    .tech-icon { width: 44px; height: 44px; }\n'
  + '    .tech-card h3 { font-size: 1.05rem; margin: 14px 0 10px; }\n'
  + '    .tech-card p { font-size: 0.9rem; line-height: 1.6; }\n\n'

  // ====== 8. Certifications ======
  + '    /* Certifications */\n'
  + '    .certifications, .certs-section { padding: 50px 0; }\n'
  + '    .certs-layout { grid-template-columns: 1fr; gap: 30px; }\n'
  + '    .cert-carousel { max-width: 100%; }\n'
  + '    .cert-slide img { max-height: 280px; }\n\n'

  // ====== 9. Education ======
  + '    /* Education */\n'
  + '    .education { padding: 50px 0; }\n'
  + '    .edu-grid { grid-template-columns: 1fr; gap: 1.25rem; }\n'
  + '    .edu-card { padding: 1.5rem; }\n'
  + '    .edu-number { font-size: 2rem; }\n'
  + '    .edu-title { font-size: 1.25rem; }\n\n'

  // ====== 10. Contact ======
  + '    /* Contact */\n'
  + '    .contact { padding: 50px 0 90px; }\n'
  + '    .contact-grid { grid-template-columns: 1fr; gap: 30px; }\n'
  + '    .contact-form-wrapper { padding: 20px; }\n'
  + '    .form-row { grid-template-columns: 1fr; gap: 16px; }\n'
  + '    .contact-intro h2 { font-size: 1.7rem; }\n'
  + '    .contact-item { font-size: 0.9rem; }\n\n'

  // ====== 11. Footer ======
  + '    /* Footer */\n'
  + '    .footer { padding: 50px 0 90px; }\n'
  + '    .footer-grid { grid-template-columns: 1fr; gap: 30px; text-align: center; }\n'
  + '    .footer-brand { margin-bottom: 20px; }\n'
  + '    .footer-links h4 { margin-bottom: 12px; font-size: 1rem; }\n'
  + '    .footer-bottom { font-size: 0.8rem; padding-top: 20px; }\n\n'

  // ====== 12. Mobile CTA bar ======
  + '    /* Mobile fixed bottom CTA bar */\n'
  + '    .mobile-cta-bar { display: flex !important; }\n'
  + '    body { padding-bottom: 76px; }\n'
  + '}\n';

css += newBlock;

fs.writeFileSync(fp, css, 'utf8');
console.log('Mobile block written, size:', newBlock.length);
console.log('CSS file total size:', css.length);

// Remove temp script
fs.unlinkSync('list_classes.js');
console.log('Removed temp list_classes.js');
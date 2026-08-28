var fs = require('fs');

// Add CSS for mobile-cta-bar (display:none on desktop, fixed bottom on mobile)
var css = fs.readFileSync('css/style.css', 'utf8');
var ctaCss = '\n/* Mobile fixed bottom CTA bar */\n'
  + '.mobile-cta-bar {\n'
  + '    display: none;\n'
  + '    position: fixed;\n'
  + '    bottom: 0;\n'
  + '    left: 0;\n'
  + '    right: 0;\n'
  + '    background: var(--color-primary);\n'
  + '    padding: 12px 16px;\n'
  + '    z-index: 998;\n'
  + '    box-shadow: 0 -2px 20px rgba(0, 0, 0, 0.15);\n'
  + '    justify-content: center;\n'
  + '}\n'
  + '.mobile-cta-btn {\n'
  + '    flex: 1;\n'
  + '    background: var(--color-white);\n'
  + '    color: var(--color-primary);\n'
  + '    text-align: center;\n'
  + '    padding: 14px 24px;\n'
  + '    border-radius: 50px;\n'
  + '    font-weight: 600;\n'
  + '    text-decoration: none;\n'
  + '    font-size: 1rem;\n'
  + '    font-family: var(--font-body);\n'
  + '    letter-spacing: 0.5px;\n'
  + '}\n';

if (css.indexOf('.mobile-cta-bar') < 0) {
  // Append at end
  css += ctaCss;
  fs.writeFileSync('css/style.css', css, 'utf8');
  console.log('css/style.css: appended .mobile-cta-bar rule');
}

// Add HTML to index.html and zh/index.html
['index.html', 'zh/index.html'].forEach(function(fp) {
  var h = fs.readFileSync(fp, 'utf8');
  // Insert before </body>
  var ctaHtml = '<div class="mobile-cta-bar"><a href="get-price.html" class="mobile-cta-btn">立即获取报价 / Get Quote</a></div>\n';
  var target = '</body>';
  if (h.indexOf(target) < 0) target = '</body>\r\n';
  if (h.indexOf(target) < 0) {
    console.log(fp + ': no </body> found!');
    return;
  }
  if (h.indexOf('mobile-cta-bar') >= 0) {
    console.log(fp + ': already has mobile-cta-bar');
    return;
  }
  h = h.replace(target, ctaHtml + target);
  fs.writeFileSync(fp, h, 'utf8');
  console.log(fp + ': mobile-cta-bar HTML added');
});
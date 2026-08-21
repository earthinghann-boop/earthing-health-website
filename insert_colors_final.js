var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');

var colorsSection = '\r\n    <section class="gb-category-section" id="available-colors" style="background: #f8f5f0;">\r\n        <div class="container">\r\n            <div class="gb-category-header" style="text-align: center; margin-bottom: 32px;">\r\n                <h2 style="font-family: \'Cormorant Garamond\', serif; font-size: 2.2rem; color: #1a2e3a; font-weight: 500; margin: 0 0 16px;">Available Colors</h2>\r\n                <p style="color: #4a5a65; max-width: 640px; margin: 0 auto; line-height: 1.7;">Choose from our classic grounding bedding palette. Each color is woven with the same silver fiber technology — soft, breathable, and ready to ground you to earth\'s potential.</p>\r\n            </div>\r\n            <div style="text-align: center; padding: 24px 0 40px;">\r\n                <img src="images/products/groundingbedding/colors/colors.jpg" alt="Available Bedding Colors" style="max-width: 900px; width: 100%; height: auto; display: block; margin: 0 auto; border-radius: 12px; box-shadow: 0 12px 40px rgba(0,0,0,0.08);">\r\n            </div>\r\n            <div style="text-align: center; padding: 0 0 32px;">\r\n                <a href="get-price.html" class="btn btn-primary" style="background: #1a2e3a; color: #fff; padding: 12px 28px; border-radius: 100px; text-decoration: none; display: inline-block;">Request Color Samples</a>\r\n            </div>\r\n        </div>\r\n    </section>\r\n';

// Find divider section close (it's the only `</section>\r\n` right before the Footer comment block)
// Walk forward from divider open: find its matching close
var divOpen = h.indexOf('<section class="section-divider">');
console.log('divider opens:', divOpen);
var pos = divOpen;
var depth = 0;
while (pos < h.length) {
    var o = h.indexOf('<section', pos);
    var c = h.indexOf('</section>', pos);
    if (c === -1) break;
    if (o !== -1 && o < c) { depth++; pos = o + 8; }
    else { depth--; pos = c + 10; if (depth === 0) { var divClose = pos; break; } }
}
console.log('divider closes:', divClose);

// Insert colorsSection right after divider close (keep blank lines as separator)
var newH = h.slice(0, divClose) + colorsSection + h.slice(divClose);
fs.writeFileSync('groundingbedding.html', newH, 'utf8');
console.log('Inserted. New size:', newH.length);

// Verify order
var kidsIdx = newH.indexOf('<section class="gb-category-section" id="kids-bedding"');
var dividerIdx = newH.indexOf('<section class="section-divider">');
var colorsIdx = newH.indexOf('<section class="gb-category-section" id="available-colors"');
var footerIdx = newH.indexOf('<footer class="footer">');
console.log('\nkids:', kidsIdx, '\ndivider:', dividerIdx, '\ncolors:', colorsIdx, '\nfooter:', footerIdx);
console.log('Order correct (kids < divider < colors < footer):', kidsIdx < dividerIdx && dividerIdx < colorsIdx && colorsIdx < footerIdx);

// Verify only one footer comment block exists (should be same as before since we didn't touch)
console.log('<!-- Footer --> count:', (newH.match(/<!-- Footer -->/g) || []).length);